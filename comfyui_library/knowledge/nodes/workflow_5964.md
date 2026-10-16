# workflow>四宫格拆图

## 节点类型

`workflow>四宫格拆图`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）
- `rows:INT`（1 次）
- `cols:INT`（1 次）
- `row_split_method:COMBO`（1 次）
- `col_split_method:COMBO`（1 次）
- `batch_index:INT`（1 次）
- `length:INT`（1 次）
- `ImageFromBatch batch_index:INT`（1 次）
- `ImageFromBatch length:INT`（1 次）

## 输出

- `遮罩:MASK`（1 次）
- `IMAGE:IMAGE`（1 次）
- `图像:IMAGE`（1 次）
- `ImageFromBatch 图像:IMAGE`（1 次）
- `ImageFromBatch 4 图像:IMAGE`（1 次）
- `ImageFromBatch 5 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["c5c8956de838027a1ee5f04350ad4c9e50cd191df6648005eba0e82d03fc7f57.png", "image", 2, 2, "uniform", "uniform", 0, 1, 1, 1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
