INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000000', 'Carolin Castano', '200', '150', 'red', 'black', '100 street Edmonton', 'f', TO_DATE('1950/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000001', 'Jorge Jaques', '199', '151', 'blue', 'black', '101 street Edmonton', 'm', TO_DATE('1951/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000002', 'Bernardina Buchanon', '198', '152', 'blue', 'black', '102 street Edmonton', 'f', TO_DATE('1952/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000003', 'Alanna Agular', '197', '153', 'green', 'black', '103 street Edmonton', 'f', TO_DATE('1953/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000004', 'Eric Ertle', '196', '154', 'green', 'black', '104 street Edmonton', 'm', TO_DATE('1954/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000005', 'Felipa Faires', '195', '155', 'red', 'blonde', '105 street Edmonton', 'f', TO_DATE('1955/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000006', 'Jamel Josephs', '194', '156', 'blue', 'blonde', '106 street Edmonton', 'm', TO_DATE('1956/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000007', 'Dusti Dong', '193', '157', 'blue', 'blonde', '107 street Edmonton', 'f', TO_DATE('1957/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000008', 'Gwenn Guerrette', '192', '158', 'green', 'blonde', '108 street Edmonton', 'f', TO_DATE('1958/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000009', 'Theda Tsuji', '191', '159', 'green', 'blonde', '109 street Edmonton', 'f', TO_DATE('1959/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000010', 'Geraldo Gurr', '190', '160', 'brown', 'brown', '110 street Edmonton', 'm', TO_DATE('1960/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000011', 'Jerold Jilek', '189', '161', 'brown', 'brown', '111 street Calgary', 'm', TO_DATE('1961/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000012', 'Lissette Lunn', '188', '162', 'brown', 'brown', '112 street Calgary', 'f', TO_DATE('1962/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000013', 'Mohamed Maese', '187', '163', 'brown', 'brown', '113 street Red Deer', 'f', TO_DATE('1963/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000014', 'Candida Crum', '188', '164', 'brown', 'brown', '114 street Edmonton', 'm', TO_DATE('1964/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000015', 'Adan Albrecht', '187', '165', 'brown', 'brown', '115 street Vancouver', 'f', TO_DATE('1965/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000016', 'Mirella Merced', '186', '166', 'brown', 'brown', '116 street Edmonton', 'm', TO_DATE('1966/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000017', 'Jolyn Jordon', '185', '167', 'brown', 'brown', '117 street Edson', 'f', TO_DATE('1967/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000018', 'Geneva Gales', '184', '168', 'brown', 'brown', '118 street Edmonton', 'f', TO_DATE('1968/07/09', 'yyyy/mm/dd')); 
INSERT INTO people(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
VALUES ('100000019', 'Leida Liebold', '183', '169', 'brown', 'brown', '119 street Edmonton', 'f', TO_DATE('1969/07/09', 'yyyy/mm/dd')); 

INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-100', '100000000', 'nondriving', TO_DATE('1968/07/09', 'yyyy/mm/dd'), TO_DATE('2012/03/06', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-101', '100000001', 'nondriving', TO_DATE('2000/01/01', 'yyyy/mm/dd'), TO_DATE('2014/04/08', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-102', '100000002', 'nondriving', TO_DATE('2000/01/02', 'yyyy/mm/dd'), TO_DATE('2018/05/19', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-103', '100000003', 'nondriving', TO_DATE('2000/01/03', 'yyyy/mm/dd'), TO_DATE('2000/01/29', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-104', '100000004', 'nondriving', TO_DATE('2000/01/04', 'yyyy/mm/dd'), TO_DATE('2001/02/19', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-105', '100000005', '7', TO_DATE('2000/01/05', 'yyyy/mm/dd'), TO_DATE('2015/02/01', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-106', '100000006', '7', TO_DATE('2011/01/06', 'yyyy/mm/dd'), TO_DATE('2016/04/02', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-107', '100000007', '7', TO_DATE('2010/01/07', 'yyyy/mm/dd'), TO_DATE('2017/05/03', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-108', '100000008', '7', TO_DATE('2010/01/08', 'yyyy/mm/dd'), TO_DATE('2012/08/04', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-109', '100000009', '7', TO_DATE('2010/01/09', 'yyyy/mm/dd'), TO_DATE('1979/07/05', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-110', '100000010', '5', TO_DATE('2010/01/11', 'yyyy/mm/dd'), TO_DATE('2013/04/06', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-111', '100000011', '5', TO_DATE('2004/02/01', 'yyyy/mm/dd'), TO_DATE('2016/07/09', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-112', '100000012', '5', TO_DATE('2004/02/02', 'yyyy/mm/dd'), TO_DATE('2017/03/19', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-113', '100000013', '5', TO_DATE('2004/02/03', 'yyyy/mm/dd'), TO_DATE('2017/03/19', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-114', '100000014', '5', TO_DATE('2004/02/04', 'yyyy/mm/dd'), TO_DATE('2018/02/11', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-115', '100000015', '5', TO_DATE('2004/02/05', 'yyyy/mm/dd'), TO_DATE('2017/03/19', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-116', '100000016', 'GDL', TO_DATE('2004/02/06', 'yyyy/mm/dd'), TO_DATE('2025/02/11', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-117', '100000017', 'GDL', TO_DATE('2004/02/07', 'yyyy/mm/dd'), TO_DATE('2018/02/11', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-118', '100000018', 'GDL', TO_DATE('2004/02/08', 'yyyy/mm/dd'), TO_DATE('2018/02/11', 'yyyy/mm/dd'));
INSERT INTO drive_licence(LICENCE_no, sin, class, issuing_date, expiring_date)
VALUES ('123456-119', '100000019', 'GDL', TO_DATE('1968/07/09', 'yyyy/mm/dd'), TO_DATE('1979/07/09', 'yyyy/mm/dd'));

INSERT INTO vehicle_type(type_id, type)
VALUES ('1', 'SUV');
INSERT INTO vehicle_type(type_id, type)
VALUES ('2', 'CAR');
INSERT INTO vehicle_type(type_id, type)
VALUES ('3', 'LIMO');
INSERT INTO vehicle_type(type_id, type)
VALUES ('4', 'EV');
INSERT INTO vehicle_type(type_id, type)
VALUES ('5', 'TRUCK');

INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1000', 'MAZDA', 'x4', '2010', 'red', '1');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1001', 'TOYOTA', 'crossover', '2011', 'blue', '1');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1002', 'HUMMER', '3', '2012', 'green', '1');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1003', 'MAZDA', 'x4', '2011', 'red', '1');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1004', 'TOYOTA', 'crossover', '2012', 'blue', '1');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1005', 'HUMMER', '3', '2012', 'green', '1');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1006', 'TOYOTA', 'PRIUS', '2009', 'green', '2');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1007', 'FORD', '4x4', '2012', 'black', '5');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1008', 'FORD', '4x4', '2011', 'green', '5');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1009', 'FORD', '4x4', '2010', 'red', '5');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1010', 'MAZDA', 'Electric', '2010', 'gold', '4');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1011', 'CHEVY', 'VOLT', '2011', 'blue', '4');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1012', 'TESLA', 'MODEL S', '2014', 'red', '2');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1013', 'BENTLEY', 'LIMO', '1992', 'black', '3');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1014', 'TOYOTA', 'crossover', '2012', 'blue', '1');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1015', 'HUMMER', '3', '2012', 'green', '1');
INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)
VALUES ('1016', 'TOYOTA', 'PRIUS', '2009', 'green', '2');

INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000005', '1000', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000005', '1001', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000005', '1002', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000006', '1003', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000006', '1004', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000006', '1005', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000007', '1000', 'n');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000007', '1001', 'n');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000008', '1003', 'n');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000009', '1006', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000010', '1007', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000011', '1008', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000012', '1009', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000013', '1010', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000014', '1011', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000015', '1012', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000016', '1013', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000017', '1014', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000018', '1015', 'y');
INSERT INTO owner(owner_id, vehicle_id, is_primary_owner)
VALUES ('100000019', '1016', 'y');

INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('1', '100000005', '100000001', '1000', TO_DATE('2010/04/01', 'yyyy/mm/dd'), '12345');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('2', '100000005', '100000001', '1001', TO_DATE('2011/04/01', 'yyyy/mm/dd'), '12342');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('3', '100000005', '100000001', '1002', TO_DATE('2012/04/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('4', '100000006', '100000001', '1003', TO_DATE('2010/02/01', 'yyyy/mm/dd'), '12345');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('5', '100000006', '100000001', '1004', TO_DATE('2011/02/01', 'yyyy/mm/dd'), '12342');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('6', '100000006', '100000001', '1005', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('7', '100000009', '100000001', '1006', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('8', '1000000010', '100000001', '1007', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('9', '1000000011', '100000001', '1008', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('10', '100000012', '100000001', '1009', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('11', '100000013', '100000001', '1010', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('12', '100000014', '100000001', '1011', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('13', '100000015', '100000001', '1012', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('14', '100000016', '100000001', '1013', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('15', '100000017', '100000001', '1014', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('16', '100000018', '100000001', '1015', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');
INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price)
VALUES ('17', '100000019', '100000001', '1016', TO_DATE('2012/02/01', 'yyyy/mm/dd'), '12343');

INSERT INTO ticket_type(vtype, fine)
VALUES ('parking', '500');
INSERT INTO ticket_type(vtype, fine)
VALUES ('speeding', '100');
INSERT INTO ticket_type(vtype, fine)
VALUES ('DUI', '800');

INSERT INTO ticket(ticket_no, violator_no, vehicle_id, office_no, vtype, vdate, place, descriptions)
VALUES ('1', '100000005', '1000', '1', 'parking', TO_DATE('2012/02/01', 'yyyy/mm/dd'), 'edmonton', 'parked bad');
INSERT INTO ticket(ticket_no, violator_no, vehicle_id, office_no, vtype, vdate, place, descriptions)
VALUES ('2', '100000005', '1001', '1', 'speeding', TO_DATE('2012/02/01', 'yyyy/mm/dd'), 'edmonton', 'speeded bad');
