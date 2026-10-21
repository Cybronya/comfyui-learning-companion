# RH_YouchuanTextToImageNiji6

## 节点类型

`RH_YouchuanTextToImageNiji6`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `cref:IMAGE`（1 次）
- `sref:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `chaos:INT`（1 次）
- `quality:COMBO`（1 次）
- `stylize:INT`（1 次）
- `weird:INT`（1 次）
- `raw:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["新中式水墨肌理插画，把意大利托斯卡纳起伏绿色草坡转化为层叠晕染青绿水墨山丘，柔和粉笔笔触质感，淡粉色花田色块点缀山坡，大面积纯白留白；画面上方三只黑色燕子剪影飞过，山腰站立一头黑色水牛，远景水面漂浮一叶扁舟，舟上穿蓝衣撑篙的极简小人；低`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
