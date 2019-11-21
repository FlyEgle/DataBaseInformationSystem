# 社团信息
create database SHETUANXINXIDATABASE;
use SHETUANXINXIDATABASE;
create table IF NOT EXISTS association_information(
  association_id INT UNSIGNED AUTO_INCREMENT,
  association_name varchar(40) NOT NULL ,
  association_location varchar(100) not null ,
  association_phone INT,
  PRIMARY KEY (association_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
show tables;
INSERT INTO association_information VALUES
( 1,'学生会','活动中心101', 10);
INSERT INTO association_information VALUES
( 2,'射箭俱乐部','活动中心102',80);
INSERT INTO association_information VALUES
( 3,'羽毛球俱乐部','活动中心103',100);
INSERT INTO association_information VALUES
( 4,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 5,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 6,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 7,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 8,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 9,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 10,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 11,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 12,'游泳俱乐部','活动中心104',1001);
INSERT INTO association_information VALUES
( 13,'游泳俱乐部','活动中心104',1001);
# ( 5,'户外俱乐部','活动中心105',13122223388),
# ( 6,'英语俱乐部','活动中心106',13122223300),
# ( 7,'跳舞俱乐部','活动中心107',13122223399),
# ( 8,'登山俱乐部','活动中心108',13122226666),
# ( 9,'科技俱乐部','活动中心109',13122228888),
# ( 10,'辩论俱乐部','活动中心110',13122225555);
select * from association_information;
# select count(*) from association_information;

# 2、财务管理
create database CAIWUGUANLIDATABASE;
use CAIWUGUANLIDATABASE;
create table if not exists money_information(
  money_id int not null ,
  money_title varchar(100) not null ,
  money_cost long not null ,
  money_time varchar(100) not null ,
  primary key (money_id)
)engine=InnoDB default charset=utf8;
show tables ;
insert into money_information values (
    110, '北京大学', 1000, '20181201'
);
insert into money_information values (
    111, '清华大学', 2000, '20181202'
);
insert into money_information values (
    112, '北京邮电', 3000, '20181203'
);
select * from money_information;

# 3、社员
create database SHEYUANDATABASE;
use SHEYUANDATABASE;
create table if not exists person_information(
  person_id int not null ,
  person_name varchar(100) not null ,
  person_sex varchar(100) not null ,
  person_locate varchar(100) not null ,
  person_iphone varchar(100) not null ,
  primary key (person_id)
)engine=InnoDB default charset=utf8;
show tables ;
insert into person_information values (
    200, '张三', '男', '计算机', '1324687'
);
insert into person_information values (
    201, '赵红', '女', '计算机', '4678911'
);
insert into person_information values (
    202, '张三', '男', '土木', '111111'
);
select * from person_information;

# 4、活动信息
create database ACTIVATEDATABASE;
use ACTIVATEDATABASE;
create table if not exists activate_information(
  activate_locate varchar(100) not null ,
  activate_time varchar(100) not null ,
  activate_content varchar(100) not null ,
  primary key (activate_locate)
)engine=InnoDB default charset=utf8;
show tables ;
insert into activate_information values (
    '活动中心1', '20181201', '跳绳'
);
insert into activate_information values (
    '活动中心2', '20181202', '打游戏'
);
insert into activate_information values (
    '活动中心3', '20181203', '篮球'
);
select * from activate_information order by activate_content ASC ;

# 5、系统管理

# 6、社团团长
create database SHETUANTUANZHANGDATABASE;
use SHETUANTUANZHANGDATABASE;
create table if not exists shetuantuanzhang_information(
  shetuantuanzhang_id int not null ,
  shetuantuanzhang_name varchar(100) not null ,
  shetuantuanzhang_sex varchar(100) not null ,
  shetuantuanzhang_locate varchar(100) not null ,
  shetuantuanzhang_iphone varchar(100) not null ,
  primary key (shetuantuanzhang_id)
)engine=InnoDB default charset=utf8;
show tables ;
insert into shetuantuanzhang_information values (
    200, '张三', '男', '计算机', '1324687'
);
insert into shetuantuanzhang_information values (
    201, '赵红', '女', '计算机', '4678911'
);
insert into shetuantuanzhang_information values (
    202, '张三', '男', '土木', '111111'
);
select * from shetuantuanzhang_information;
# 7、合作单位
create database HEZUODANWEIDATABASE;
use HEZUODANWEIDATABASE;
create table if not exists hezuodanwei_information(
  hezuodanwei_name varchar(100) not null ,
  hezuodanwei_locate varchar(100) not null ,
  hezuodanwei_iphone varchar(100) not null ,
  hezuodanwei_project varchar(100) not null ,
  primary key (hezuodanwei_name)
)engine=InnoDB default charset=utf8;
show tables ;
insert into hezuodanwei_information values (
    '华为', '深圳', '123456', '大数据'
);
insert into hezuodanwei_information values (
    '腾讯', '深圳', '234567', '云计算'
);
insert into hezuodanwei_information values (
    '阿里', '杭州', '345678', '硬件'
);
select * from hezuodanwei_information;
# 8、指导老师
create database TEACHERDATABASE;
use TEACHERDATABASE;
create table if not exists teacher_information(
  teacher_id int not null ,
  teacher_name varchar(100) not null ,
  teacher_prof varchar(100) not null ,
  teacher_locate varchar(100) not null ,
  teacher_home varchar(100) not null ,
  primary key (teacher_id)
)engine=InnoDB default charset=utf8;
show tables ;
insert into teacher_information values (
   1 ,'王五', '教授', '土木', '工学一号馆'
);
insert into teacher_information values (
   2, '李林', '副教授', '计算机', '工学二号馆'
);
insert into teacher_information values(
   3, '马刀', '讲师', '计算机', '工学一号馆'
);
select * from teacher_information;

# 5 系统管理
create database SYSTEMBASE;
use SYSTEMBASE;
create table if not exists system_information(
  system_id int not null ,
  system_account varchar(100) not null ,
  system_password varchar(100) not null ,
  primary key (system_id)
);
show tables ;
insert into system_information values(
  1, 'admin1', '123456'
);
insert into system_information values(
  2, 'admin2', '234567'
);
insert into system_information values(
  3, 'admin3', '345678'
);
select * from system_information;
# SELECT COUNT(*) FROM system_information;
