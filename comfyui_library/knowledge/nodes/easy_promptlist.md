# easy promptList

## 节点类型

`easy promptList`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `optional_prompt_list:LIST`（4 次）
- `prompt_1:STRING`（4 次）
- `prompt_2:STRING`（4 次）
- `prompt_3:STRING`（4 次）
- `prompt_4:STRING`（4 次）
- `prompt_5:STRING`（4 次）

## 输出

- `prompt_list:LIST`（4 次）
- `prompt_strings:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一位中国年轻女性侧身凝望远方，乌黑长发自然垂落肩头，身穿缀满红色亮片的露肩礼服，在幽深林间静谧伫立；她佩戴着精致金色项链和耳环，中央镶嵌椭圆形翠绿色宝石，左手轻触锁骨处珠宝，无名指戴有同款戒指，肌肤细腻光泽柔和；画面采用近景特写构图，焦`（1 次）
- `["怪力乱神窥视镜头，武侠渺小的站在楼上看着，巨物压迫，恐怖，点翠，民族风，超多细节，仰拍，动态，戏剧张力，大片高级感，电影美学，虚幻引擎5渲染，超写实", "中式怪异，黑暗神秘风格融合中式美学，完美细节，多重管线渲染，完美建模。西游记背景`（1 次）
- `["{\"rewritten_prompt\": \"msj The image is a wide real-time game engine environment render of a Song dynasty Chinese ti`（1 次）
- `["一位中国年轻女性侧身凝望远方，发型以参考图为准，服装以参考图为准，在幽深林间静谧伫立；她佩戴着精致金色项链和耳环，中央镶嵌椭圆形翠绿色宝石，左手轻触锁骨处珠宝，无名指戴有同款戒指，肌肤细腻光泽柔和；画面采用近景特写构图，焦点精准落在人物`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
