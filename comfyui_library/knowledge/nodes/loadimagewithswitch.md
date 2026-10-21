# LoadImageWithSwitch

## 节点类型

`LoadImageWithSwitch`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:COMBO`（12 次）
- `upload:IMAGEUPLOAD`（12 次）
- `enabled:BOOLEAN`（12 次）

## 输出

- `image:IMAGE`（12 次）
- `mask:MASK`（12 次）
- `enabled:BOOLEAN`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["b50b2f436882110eb515d458eea446832077c918bac8e00bcee5f2776478f70a.png", "image", false]`（12 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
