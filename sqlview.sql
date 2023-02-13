create view pedidos_por_preco_maior_que_20
begin
    select id, data, valor, sum(coluna) from pedidos where valor > 20
    group by data,id,valor
end


select * from pedidos_por_preco_maior_que_20



select count(1) from pedidos