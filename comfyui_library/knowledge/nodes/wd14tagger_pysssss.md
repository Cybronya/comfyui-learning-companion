# WD14Tagger|pysssss

## 节点类型

`WD14Tagger|pysssss`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image:IMAGE`（5 次）
- `model:COMBO`（5 次）
- `threshold:FLOAT`（5 次）
- `character_threshold:FLOAT`（5 次）
- `replace_underscore:BOOLEAN`（5 次）
- `trailing_comma:BOOLEAN`（5 次）
- `exclude_tags:STRING`（5 次）

## 输出

- `STRING:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wd-v1-4-moat-tagger-v2", 0.35, 0.85, false, false, ""]`（2 次）
- `["wd-v1-4-moat-tagger-v2", 0.35, 0.35000000000000003, false, false, "", "souryuu_asuka_langley, eva_02, 1girl, long_hair`（1 次）
- `["wd-v1-4-moat-tagger-v2", 0.35, 0.35000000000000003, false, false, ""]`（1 次）
- `["wd-eva02-large-tagger-v3", 0.4000000000000001, 0.85, true, false, "", "1girl, solo, long hair, looking at viewer, blue`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
