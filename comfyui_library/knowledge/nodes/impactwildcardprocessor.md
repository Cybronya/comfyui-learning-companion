# ImpactWildcardProcessor

## 节点类型

`ImpactWildcardProcessor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `wildcard_text:STRING`（2 次）
- `populated_text:STRING`（2 次）
- `mode:COMBO`（2 次）
- `seed:INT`（2 次）
- `Select to add Wildcard:COMBO`（2 次）

## 输出

- `processed text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["newest, masterpiece, best quality, score_7,\n1girl, solo, ", "newest, masterpiece, best quality, score_7,\n1girl, solo`（1 次）
- `["worst quality, low quality, lowres, score_1, score_2, score_3, blurry, jpeg artifacts, bad anatomy, watermark, artist `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
