
CREATE TABLE categories (
	categoryid SERIAL NOT NULL, 
	categoryname VARCHAR(25), 
	description VARCHAR(255), 
	CONSTRAINT categories_pkey PRIMARY KEY (categoryid)
)



CREATE TABLE suppliers (
	supplierid SERIAL NOT NULL, 
	suppliername VARCHAR(50), 
	contactname VARCHAR(50), 
	address VARCHAR(50), 
	city VARCHAR(20), 
	postalcode VARCHAR(10), 
	country VARCHAR(15), 
	phone VARCHAR(15), 
	CONSTRAINT suppliers_pkey PRIMARY KEY (supplierid)
)



CREATE TABLE employees (
	employeeid SERIAL NOT NULL, 
	lastname VARCHAR(15), 
	firstname VARCHAR(15), 
	birthdate TIMESTAMP WITHOUT TIME ZONE, 
	photo VARCHAR(25), 
	notes VARCHAR(1024), 
	CONSTRAINT employees_pkey PRIMARY KEY (employeeid)
)



CREATE TABLE customers (
	customerid SERIAL NOT NULL, 
	customername VARCHAR(50), 
	contactname VARCHAR(50), 
	address VARCHAR(50), 
	city VARCHAR(20), 
	postalcode VARCHAR(10), 
	country VARCHAR(15), 
	CONSTRAINT customers_pkey PRIMARY KEY (customerid)
)



CREATE TABLE shippers (
	shipperid SERIAL NOT NULL, 
	shippername VARCHAR(25), 
	phone VARCHAR(15), 
	CONSTRAINT shippers_pkey PRIMARY KEY (shipperid)
)



CREATE TABLE products (
	productid SERIAL NOT NULL, 
	productname VARCHAR(50), 
	supplierid INTEGER, 
	categoryid INTEGER, 
	unit VARCHAR(25), 
	price NUMERIC, 
	CONSTRAINT products_pkey PRIMARY KEY (productid), 
	CONSTRAINT products_categoryid_fkey FOREIGN KEY(categoryid) REFERENCES categories (categoryid), 
	CONSTRAINT products_supplierid_fkey FOREIGN KEY(supplierid) REFERENCES suppliers (supplierid)
)



CREATE TABLE orders (
	orderid SERIAL NOT NULL, 
	customerid INTEGER, 
	employeeid INTEGER, 
	orderdate TIMESTAMP WITHOUT TIME ZONE, 
	shipperid INTEGER, 
	CONSTRAINT orders_pkey PRIMARY KEY (orderid), 
	CONSTRAINT orders_customerid_fkey FOREIGN KEY(customerid) REFERENCES customers (customerid), 
	CONSTRAINT orders_employeeid_fkey FOREIGN KEY(employeeid) REFERENCES employees (employeeid), 
	CONSTRAINT orders_shipperid_fkey FOREIGN KEY(shipperid) REFERENCES shippers (shipperid)
)



CREATE TABLE orderdetails (
	orderdetailid SERIAL NOT NULL, 
	orderid INTEGER, 
	productid INTEGER, 
	quantity INTEGER, 
	CONSTRAINT orderdetails_pkey PRIMARY KEY (orderdetailid), 
	CONSTRAINT orderdetails_orderid_fkey FOREIGN KEY(orderid) REFERENCES orders (orderid), 
	CONSTRAINT orderdetails_productid_fkey FOREIGN KEY(productid) REFERENCES products (productid)
)


