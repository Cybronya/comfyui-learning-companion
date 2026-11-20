# EasyLoadImage

## 节点类型

`EasyLoadImage`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（2 次）
- `upload:IMAGEUPLOAD`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["affb18f07ad9a37aca4f781b079188cee85b0884a98809e43a7294baceba3528.png", "image"]`（1 次）
- `["b17507d6990c3754a256de6c7006f3e44011c29d6aa069eece7ce3ef7ef035d5.png", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
