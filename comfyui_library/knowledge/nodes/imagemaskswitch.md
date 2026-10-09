# ImageMaskSwitch

## 节点类型

`ImageMaskSwitch`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images1:IMAGE`（2 次）
- `mask1_opt:MASK`（2 次）
- `images2_opt:IMAGE`（2 次）
- `mask2_opt:MASK`（2 次）
- `images3_opt:IMAGE`（2 次）
- `mask3_opt:MASK`（2 次）
- `images4_opt:IMAGE`（2 次）
- `mask4_opt:MASK`（2 次）
- `select:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
