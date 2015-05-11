# -*- coding: utf-8 -*-
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

seg_list = jieba.cut("爭議多時的北投纜車，台北市長柯文哲10日明確表示反對開發，要和廠商坐下來談退場機制，柯強調，這是北纜政策大轉彎。開發商儷山林表示，還沒收到正式公文通知，對於從報紙得知北市府決策感到傻眼，認為「不能你一句話說不蓋就不蓋」，整起事件恐怕仍得歹戲拖棚下去。", cut_all=False) 
print(", ".join(seg_list))