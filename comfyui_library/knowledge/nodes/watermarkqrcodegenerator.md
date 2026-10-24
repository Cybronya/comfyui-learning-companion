# WatermarkQRCodeGenerator

## 节点类型

`WatermarkQRCodeGenerator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text:STRING`（1 次）
- `qr_size:INT`（1 次）
- `error_correction:COMBO`（1 次）
- `border:INT`（1 次）
- `invert:BOOLEAN`（1 次）

## 输出

- `qr_image:IMAGE`（1 次）
- `info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://u.wechat.com/MI3kmLva7kIRckdAnWoyoX4?s=4", 128, "M (15%)", 2, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
