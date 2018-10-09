SELECT  t1.gwas_result_chromosome
        ,t1.basepair
        ,t1.gwas_result_gwas_run
        ,t2.gwas_run_genotype_version
        ,t2.gwas_run_trait
        ,t3.trait_name
        ,t4.phenotype_line
        ,t4.phenotype_value
        ,t5.line_name 
FROM gwas_result t1
    INNER JOIN gwas_run t2
        ON t1.gwas_result_gwas_run=t2.gwas_run_id 
    INNER JOIN trait t3
        ON t2.gwas_run_trait=t3.trait_id 
    INNER JOIN phenotype t4
        ON t3.trait_id = t4.phenotype_trait 
    INNER JOIN line t5
        ON t4.phenotype_line=t5.line_id
WHERE t1.gwas_result_id=35550;
