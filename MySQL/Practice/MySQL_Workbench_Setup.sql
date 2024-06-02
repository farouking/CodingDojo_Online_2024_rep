use names;
select * from names;
/* INSERT statement*/
insert into names (name) values ("Farouk SOUISSI");
/* multi INSERT in one statement*/
insert into names (name) values ("Ali ALAYA"),("Yasmin ALAYA"),("Yaya DEMBELE");
/* Delete statement*/
delete from names where id =2;

/* Update statement*/
update  names 
set name = "Nihel GUEBSI"
where id =3;

