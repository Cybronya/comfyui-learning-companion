# workflow/flux模型

## 节点类型

`workflow/flux模型`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（1 次）
- `neg_conditioning:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `controlnet_condition:ControlNetCondition`（1 次）

## 输出

- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux1-dev-fp8-Kijai.safetensors", "default", 324242532548, "fixed", 25, 1, 3.5, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
