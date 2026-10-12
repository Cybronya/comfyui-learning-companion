# ImagePadForOutpaintMasked_UTK

## 节点类型

`ImagePadForOutpaintMasked_UTK`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（6 次）
- `mask:MASK`（6 次）
- `data_mode:COMBO`（6 次）
- `left:INT`（6 次）
- `top:INT`（6 次）
- `right:INT`（6 次）
- `bottom:INT`（6 次）
- `feathering:INT`（6 次）
- `background_color:COMBO`（6 次）

## 输出

- `IMAGE:IMAGE`（6 次）
- `MASK:MASK`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["pixel", 0, 200, 0, 0, 0, "white"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
