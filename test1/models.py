from db.BaseModel import *
from django.db import models


class CagManager(models.Manager):
    # 根据用户名查询用户
    def get_caginfo_by_name(self, cags_name):

        try:
            return self.get(cag_name=cags_name)
        except Category.DoesNotExist:
            return None


class Category(BaseModel):
    cag_name = models.CharField(max_length=30);
    cag_link = models.CharField(max_length=100);

    objects = CagManager()


class GoodsList(BaseModel):
    goods_name = models.CharField(max_length=30)
    goods_link = models.CharField(max_length=100)
    goods_cag = models.ForeignKey(Category)

# desc test1_category;
# +-------------+--------------+------+-----+---------+----------------+
# | Field       | Type         | Null | Key | Default | Extra          |
# +-------------+--------------+------+-----+---------+----------------+
# | id          | int(11)      | NO   | PRI | NULL    | auto_increment |
# | create_time | datetime(6)  | NO   |     | NULL    |                |
# | update_time | datetime(6)  | NO   |     | NULL    |                |
# | is_delete   | tinyint(1)   | NO   |     | NULL    |                |
# | cag_name    | varchar(30)  | NO   |     | NULL    |                |
# | cag_link    | varchar(100) | NO   |     | NULL    |                |
# +-------------+--------------+------+-----+---------+----------------+
#
#  desc test1_goodslist;
# +--------------+--------------+------+-----+---------+----------------+
# | Field        | Type         | Null | Key | Default | Extra          |
# +--------------+--------------+------+-----+---------+----------------+
# | id           | int(11)      | NO   | PRI | NULL    | auto_increment |
# | create_time  | datetime(6)  | NO   |     | NULL    |                |
# | update_time  | datetime(6)  | NO   |     | NULL    |                |
# | is_delete    | tinyint(1)   | NO   |     | NULL    |                |
# | goods_name   | varchar(30)  | NO   |     | NULL    |                |
# | goods_link   | varchar(100) | NO   |     | NULL    |                |
# | goods_cag_id | int(11)      | NO   | MUL | NULL    |                |
# +--------------+--------------+------+-----+---------+----------------+

