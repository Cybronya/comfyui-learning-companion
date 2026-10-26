# SDVN IC Lora Layout

## 节点类型

`SDVN IC Lora Layout`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `mask1:MASK`（2 次）
- `mask2:MASK`（2 次）
- `height_size:INT`（2 次）

## 输出

- `ic_layout:IMAGE`（2 次）
- `mask_layout:MASK`（2 次）
- `crop_image1:CROP`（2 次）
- `crop_image2:CROP`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
