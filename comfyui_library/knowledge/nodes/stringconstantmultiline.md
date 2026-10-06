# StringConstantMultiline

## 节点类型

`StringConstantMultiline`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `string:STRING`（19 次）
- `strip_newlines:BOOLEAN`（19 次）

## 输出

- `STRING:STRING`（19 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", true]`（6 次）
- `["<|im_start|>system\n# Edit Prompt Enhancer — General (v2, 精简版)\n\n**FIRST — there are TWO separate language decisions.`（3 次）
- `["<|im_start|>system\n\n # Image Prompt Rewriting Expert\n\nYou turn a user's image request into one long English paragr`（2 次）
- `["生成一张高质量中文电商详情页长图，适用于高端保温杯产品，风格干净、真实、有品质感，像真实天猫/京东产品详情页。\n\n产品名称：\n“轻量真空保温杯”\n\n内容结构必须从上到下包含：\n\n1. 顶部主KV\n- 大幅产品图\n- 中`（2 次）
- `["一位成年亚裔女性真人时尚写真，人物是成年女性。她的辨识点是全黑漆皮机能装、棕黑松散丸子头、眼下银色蝴蝶形水钻，以及手中那把中世纪长剑；这四处是认出她的依据，缺一处就不是同一个人。\n\n烟雾里跪姿起身的横构图全身人像 × 私密感时尚 e`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
