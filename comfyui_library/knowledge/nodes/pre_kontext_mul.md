# pre_Kontext_mul

## 节点类型

`pre_Kontext_mul`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `context:RUN_CONTEXT`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `mask1:MASK`（1 次）
- `mask2:MASK`（1 次）
- `mask3:MASK`（1 次）
- `mask4:MASK`（1 次）
- `mask5:MASK`（1 次）

## 输出

- `context:RUN_CONTEXT`（1 次）
- `positive:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Green baseball cap", "Black sunglasses", "", "", "", 0.5, 0.5, 0.5, 0.5, 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
