# UC_ResolutionSelectorExtended

## 节点类型

`UC_ResolutionSelectorExtended`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `aspect_ratio:COMBO`（3 次）
- `megapixels:FLOAT`（3 次）
- `multiple:INT`（3 次）
- `minimum:INT`（3 次）

## 输出

- `width:INT`（3 次）
- `height:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["9:16 (Tall Portrait)", 0.7, 32, 256]`（1 次）
- `["16:9 (Widescreen)", 0.7, 32, 256]`（1 次）
- `["9:16 (Tall Portrait)", 0.8, 32, 256]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
