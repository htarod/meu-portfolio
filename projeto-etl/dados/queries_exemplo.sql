
-- Média geral por estado
SELECT uf, ROUND(AVG(media_geral), 2) AS media_uf
FROM enem_escolas
GROUP BY uf
ORDER BY media_uf DESC;

-- Proporção de escolas privadas por estado
SELECT uf,
       COUNT(CASE WHEN tipo_escola = 'Privada' THEN 1 END) * 1.0 / COUNT(*) AS proporcao_privada
FROM enem_escolas
GROUP BY uf
ORDER BY proporcao_privada DESC;

-- Top 10 municípios com maior média geral
SELECT municipio, uf, ROUND(AVG(media_geral), 2) AS media_municipio
FROM enem_escolas
GROUP BY municipio, uf
ORDER BY media_municipio DESC
LIMIT 10;
