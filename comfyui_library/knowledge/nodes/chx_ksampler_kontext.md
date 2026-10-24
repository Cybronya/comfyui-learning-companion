# chx_Ksampler_Kontext

## 节点类型

`chx_Ksampler_Kontext`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `context:RUN_CONTEXT`（13 次）
- `image:IMAGE`（13 次）
- `mask:MASK`（13 次）
- `pos:STRING`（7 次）
- `pos:0`（3 次）

## 输出

- `context:RUN_CONTEXT`（13 次）
- `image:IMAGE`（13 次）
- `latent:LATENT`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[589490067010894, "randomize", 0.5000000000000001, 25, 1, false, "Preview", "change background to in beach with blue sea`（1 次）
- `[669674766434110, "randomize", 0.5000000000000001, 25, 1, false, "Preview", "Put a  blue sun hat on the woman's head"]`（1 次）
- `[418126830444791, "randomize", 0.5000000000000001, 25, 1, false, "Preview", "Change women dress in a white light gauze s`（1 次）
- `[401113137533443, "randomize", 0.5000000000000001, 25, 1, false, "Preview", "", ""]`（1 次）
- `[568291120001301, "randomize", 0.5000000000000001, 25, 1, false, "Preview", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
