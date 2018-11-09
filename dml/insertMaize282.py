#!/bin/python
# This script contains most of the code executed to insert all of the Maize282 dataset into the GWAS database.
# It uses functions from the other modules in the BaxDB code -- insert functions from insert.py, find functions from find.py, helper functions from parsinghelpers.py, classes defined in models.py, and connection/configuration functions from dbconnect.py

import pandas as pd
import numpy as np
import psycopg2
import csv
import insert
import find
from dbconnect import config, connect
from models import species, population, line, chromosome, variant, genotype, trait, phenotype, growout_type, growout, location, gwas_algorithm, genotype_version, imputation_method, kinship_algorithm, kinship, population_structure_algorithm, population_structure, gwas_run, gwas_result


if __name__ == '__main__':
  conn = connect()

  # ADD HARD-CODED VALUES FOR INDEPENDENT TABLES/OBJECTS

  # ADD LOCATIONS
  locations = []
  locations.append(location("United States", "Indiana", "West Lafayette", "PU"))
  locations.append(location("United States", "New York", None, "NY"))
  locations.append(location("United States", "Florida", None, "FL"))
  locations.append(location("United States", "Puerto Rico", None, "PR"))
  locations.append(location("United States", "North Carolina", None, "NC"))
  locations.append(location("South Africa", None, None, "SA"))
  locations.append(location("United States", "Missouri", None, "MO"))
  for place in locations:
    insert.insert_location(conn, place)
  # LOOK UP ID OF A HARD-CODED LOCATION USING find_chromosome()
  PUlocID = find.find_location(conn, 'PU')
  NYlocID = find.find_location(conn, "NY")
  FLlocID = find.find_location(conn, "FL")
  PRlocID = find.find_location(conn, "PR")
  NClocID = find.find_location(conn, "NC")
  SAlocID = find.find_location(conn, "SA")
  MOlocID = find.find_location(conn, "MO")

  # ADD A HARD-CODED SPECIES TO DB USING insert_species()
  mySpecies = species('maize', 'Zea mays', None, None)
  insertedSpeciesID = insert.insert_species(conn, mySpecies)
  print("[ INSERT ]\t(%s)\t%s" % (insertedSpeciesID, str(mySpecies)))
  maizeSpeciesID = find.find_species(conn, 'maize')
  print("[ FIND ]\t(%s)\t%s" % (maizeSpeciesID, '< species: maize >'))

  # ADD A HARD-CODED POPULATION TO DB USING insert_population()
  myPopulation = population('Maize282', maizeSpeciesID)
  insertedPopulationID = insert.insert_population(conn, myPopulation)
  print("[ INSERT ]\t(%s)\t%s" % (insertedPopulationID, str(myPopulation)))
  maize282popID = find.find_population(conn, 'Maize282')
  print("[ FIND ]\t(%s)\t%s" % (maize282popID, '< population: Maize282 >'))

  # ADD A HARD-CODED LINE TO DB USING insert_line()
  myLine = line(line_name='282set_B73', line_population=maize282popID)
  insertedLineID = insert.insert_line(conn, myLine)
  print("[ INSERT ]\t(%s)\t%s" % (insertedLineID, str(myLine)))
  B73lineID = find.find_line(conn, '282set_B73', maize282popID)
  print("[ FIND ]\t(%s)\t%s" % (B73lineID, '< line: Maize282 >'))

  # ADD NEW HARD-CODED GENOTYPE_VERSION TO DB
  myGenotypeVersion = genotype_version(genotype_version_name='B73 RefGen_v4_AGPv4_Maize282',
                                       genotype_version=315, reference_genome=B73lineID, genotype_version_population=maize282popID)
  B73_agpv4_maize282_versionID = insert.insert_genotype_version(conn, myGenotypeVersion)
  print("[ INSERT ]\t(%s)\t%s" % (B73lineID, str(myGenotypeVersion)))

  # ADD ALL CHROMOSOMES FOR A SPECIES TO DB
  insertedChromosomeIDs = insert.insert_all_chromosomes_for_species(conn, 10, maizeSpeciesID)
  print("[ INSERT ]\t%s\t%s" % (insertedChromosomeIDs, '\t10 (sID: %s)' % maizeSpeciesID))
  maizeChr10ID = find.find_chromosome(conn, 'chr10', maizeSpeciesID)
  print("[ FIND ]\t(%s)\t%s" % (maizeChr10ID, '< chromsome: chr10 >'))
  
  # GET LINES FROM SPECIFIED 012.indv FILE AND ADD TO DB
  insertedLineIDs = insert.insert_lines_from_file(conn, '../data/chr10_282_agpv4.012.indv', maize282popID)
  print("[ INSERT ]\t%s\t%s\t(pID:  %s)" % (insertedLineIDs, '../data/chr10_282_agpv4.012.indv', maize282popID))

  # ADD ALL GENOTYPES FROM A ONE-CHROMOSOME .012 FILE TO DB
  insertedGenotypeIDs = insert.insert_genotypes_from_file(conn,'../data/chr10_282_agpv4.012' , '../data/chr10_282_agpv4.012.indv', maizeChr10ID, maize282popID, B73lineID)
  print("Inserted genotype IDs:")
  print(insertedGenotypeIDs)
  print("[ INSERT ]\t%s\t%s\t(cID: %s, pID: %s, lID: %s)" % (insertedGenotypeIDs,
                                                             'chr10_282_agpv4.012 & indv', str(maizeChr10ID), str(maize282popID), str(B73lineID)))

  # GET VARIANTS FROM .012.pos FILE AND ADD TO  DB
  insertedVariantIDs = insert.insert_variants_from_file(conn, '../data/chr10_282_agpv4.012.pos', maizeSpeciesID, maizeChr10ID)
  print("num inserted variants:")
  print(len(insertedVariantIDs))

  # PARSE TRAITS FROM PHENOTYPE FILE AND ADD TO DB
  phenotypeRawData = pd.read_csv('../data/5.mergedWeightNorm.LM.rankAvg.longFormat.csv', index_col=0)
  traits = list(phenotypeRawData)
  insertedTraitIDs = insert.insert_traits_from_traitlist(conn, traits)
  print("num inserted traits:")
  print(len(insertedTraitIDs))
  print("Inserted trait IDs:")
  print(insertedTraitIDs)
  
  # PARSE PHENOTYPES FROM FILE AND ADD TO DB
  # NOTE(timp): Cannot find file
  insertedPhenoIDs = insert.insert_phenotypes_from_file(conn, '../data/5.mergedWeightNorm.LM.rankAvg.longFormat.csv', maize282popID)
  print("num phenotypes inserted:")
  print(len(insertedPhenoIDs))
  print("phenoIDs:")
  print(insertedPhenoIDs)

  # ADD NEW HARD-CODED GROWOUT_TYPE TO DB
  greenhouse_GrowoutType = growout_type("greenhouse")
  greenhouse_GrowoutTypeID = insert.insert_growout_type(conn, greenhouse_GrowoutType)

  phenotyper_GrowoutType = growout_type("phenotyper")
  phenotyper_GrowoutTypeID = insert.insert_growout_type(conn, phenotyper_GrowoutType)

  field_GrowoutType = growout_type("field")
  field_GrowoutTypeID = insert.insert_growout_type(conn, field_GrowoutType)

  # LOOK UP ID OF A HARD-CODED GROWOUT_TYPE USING find_chromosome()
  fieldGrowoutTypeID = find.find_growout_type(conn, 'field')
  print("[ FIND ]\t(%s)\t%s" % (fieldGrowoutTypeID, '< growout_type: field >'))

  # ADD NEW HARD-CODED GROWOUT TO DB
  growouts = []
  growouts.append(growout("PU09", maize282popID, PUlocID, 2009, fieldGrowoutTypeID))
  growouts.append(growout("NY06", maize282popID, NYlocID, 2006, fieldGrowoutTypeID))
  growouts.append(growout("NY10", maize282popID, NYlocID, 2010, fieldGrowoutTypeID))
  growouts.append(growout("FL06", maize282popID, FLlocID, 2006, fieldGrowoutTypeID))
  growouts.append(growout("PR06", maize282popID, PRlocID, 2006, fieldGrowoutTypeID))
  growouts.append(growout("NC06", maize282popID, NClocID, 2006, fieldGrowoutTypeID))
  growouts.append(growout("PU10", maize282popID, PUlocID, 2010, fieldGrowoutTypeID))
  growouts.append(growout("SA06", maize282popID, SAlocID, 2006, fieldGrowoutTypeID))
  growouts.append(growout("MO06", maize282popID, MOlocID, 2006, fieldGrowoutTypeID))
  insertedGrowoutIDs = []
  for growout in growouts:
    print("-------------\t%s" % str(growout))
    insertedGrowoutIDs.append(insert.insert_growout(conn, growout))
  print("[ INSERT ]\t%s\t(new growout)" % (insertedGenotypeIDs) )
  
  # ADD NEW HARD-CODED GWAS_ALGORITHM TO DB
  gwasAlgorithms = []
  gwasAlgorithms.append(gwas_algorithm("MLMM"))
  gwasAlgorithms.append(gwas_algorithm("EMMAx"))
  gwasAlgorithms.append(gwas_algorithm("GAPIT"))
  gwasAlgorithms.append(gwas_algorithm("FarmCPU"))
  newGWASalgorithmIDs = []
  for algorithm in gwasAlgorithms:
    insert.insert_gwas_algorithm(conn, algorithm)
  print("[ INSERT ]\t%s\t(new gwas algorithm IDs)" % (newGWASalgorithmIDs) )
  newGWASalgorithm = find.find_gwas_algorithm(conn, 'MLMM')


  # ADD NEW HARD-CODED IMPUTATION_METHOD TO DB
  newImputationMethod = imputation_method("impute to major allele")
  #newImputationMethod = imputation_method("impute to minor allele")
  #newImputationMethod = imputation_method("impute to average allele")
  #newImputationMethod = imputation_method("IMPUTE")
  #newImputationMethod = imputation_method("BEAGLE")
  newImputationMethodID = insert.insert_imputation_method(conn, newImputationMethod)
  print("Imputatin Method ID:")
  print(newImputationMethodID)

  
  # ADD NEW HARD-CODED KINSHIP_ALGORITHM TO DB
  kinshipAlgorithms = []
  kinshipAlgorithms.append(kinship_algorithm("loiselle"))
  kinshipAlgorithms.append(kinship_algorithm("van raden"))
  kinshipAlgorithms.append(kinship_algorithm("Synbreed_realizedAB"))
  newKinshipAlgorithmIDs = []
  for algorithm in kinshipAlgorithms:
    newKinshipAlgorithmIDs.append(
        insert.insert_kinship_algorithm(conn, algorithm))
  print("[ INSERT ]\t%s\t(new kinship algorithm IDs)" % (newKinshipAlgorithmIDs))
  # LOOK UP ID OF A HARD-CODED KINSHIP_ALGORITHM USING find_kinship_algorithm()
  VanRadenID = find.find_kinship_algorithm(conn, "van raden")
  print("Van Raden kinship alg ID:")
  print(VanRadenID)  

  # ADD NEW HARD-CODED KINSHIP TO DB
  # NOTE(timp): Cannot find file
  newKinship = kinship(VanRadenID, "../data/4.AstleBalding.synbreed.kinship.csv")
  newKinshipID = insert.insert_kinship(conn, newKinship)
  print("New kinship ID:")
  print(newKinshipID)

  # ADD NEW HARD-CODED POPULATION_STRUCTURE_ALGORITHM TO DB
  newPopulationStructureAlgorithm = population_structure_algorithm("Eigenstrat")
  newPopulationStructureAlgorithm = population_structure_algorithm("STRUCTURE")
  newPopulationStructureAlgorithm = population_structure_algorithm("FastSTRUCTURE")
  newPopulationStructureAlgorithmID = insert.insert_population_structure_algorithm(conn, newPopulationStructureAlgorithm)
  print("pop structure algorithm ID:")
  print(newPopulationStructureAlgorithmID)

  # LOOK UP ID OF A HARD-CODED POPULATION_STRUCTURE_ALGORITHM USING find_population_structure_algorithm()
  EigenstratID = find.find_population_structure_algorithm(conn, "Eigenstrat")
  print("Eigenstrat pop str alg ID:")
  print(EigenstratID)

  # ADD NEW HARD-CODED POPULATION_STRUCTURE TO DB
  newPopulationStructure = population_structure(EigenstratID, "../data/4.Eigenstrat.population.structure.10PCs.csv")
  newPopulationStructureID = insert.insert_population_structure(conn, newPopulationStructure)
  print("New population structure ID:")
  print(newPopulationStructureID)

  # LOOK UP ID OF A HARD-CODED GWAS_ALGORITHM
  MLMMalgorithmID = find.find_gwas_algorithm(conn, "MLMM")
  print("MLMM algorithm ID:")
  print(MLMMalgorithmID)

  # LOOK UP ID OF A HARD-CODED GENOTYPE_VERSION
  B73_agpv4_maize282_versionID = find.find_genotype_version(conn, "B73 RefGen_v4_AGPv4_Maize282")
  print("B73 agpv4 maize282 genotype version: ")
  print(B73_agpv4_maize282_versionID)  

  # LOOK UP ID OF A HARD-CODED IMPUTATION_METHOD
  majorAlleleImputationID = find.find_imputation_method(conn, "impute to major allele")
  print("major allele imputation ID: ")
  print(majorAlleleImputationID)  

  # LOOK UP ID OF A HARD-CODED KINSHIP
  # NOTE(timp): I could not find this file, but I found a R data file (.rda) that may contain the information.
  #             Although, the data may not be in the correct format.
  #             The temporary file is the one with 'export' in its name.
  # kinshipID = find.find_kinship(conn, "/opt/BaxDB/file_storage/kinship_files/4.AstleBalding.synbreed.kinship.csv")
  kinshipID = find.find_kinship(conn, "../data/4.AstleBalding.synbreed.kinship.csv")
  print("kinshipID: ")
  print(kinshipID)  

  # LOOK UP ID OF A HARD-CODED POPULATION_STRUCTURE
  populationStructureID = find.find_population_structure(conn, "../data/4.Eigenstrat.population.structure.10PCs.csv")
  print("population structure ID: ")
  print(populationStructureID)

  # PARSE GWAS_RUNS FROM FILE AND ADD TO DB
  # NOTE(timp): Could not find file or possible equivalent
  insertedGwasRunIDs = insert.insert_gwas_runs_from_gwas_results_file(conn, '../data/9.mlmmResults.csv', MLMMalgorithmID, B73_agpv4_maize282_versionID, 0.2, 0.2, 0.1, majorAlleleImputationID, kinshipID, populationStructureID)
  print("Inserted gwas_run IDs:")
  print(insertedGwasRunIDs)

  # PARSE GWAS_RESULTS FROM FILE AND ADD TO DB
  # NOTE(timp): Could not find file or possible equivalent
  insertedGwasResultIDs = insert.insert_gwas_results_from_file(conn, maizeSpeciesID, '../data/9.mlmmResults.csv', MLMMalgorithmID, 0.2, 0.2, majorAlleleImputationID, B73_agpv4_maize282_versionID, kinshipID, populationStructureID, 0.1)
  print("Inserted gwas result IDs: ")
  print(insertedGwasResultIDs)
