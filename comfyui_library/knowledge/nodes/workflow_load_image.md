# workflow>load image

## 节点类型

`workflow>load image`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）
- `longer_edge:INT`（1 次）

## 输出

- `MASK:MASK`（1 次）
- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["53b1deb6025b8c6e1bad10db5a56005978ff102c84c5769a5be10a05c42afb1a.jpg", "image", 1024]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
