# workflow/joy

## 节点类型

`workflow/joy`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `噪波生成:NOISE`（1 次）
- `引导:GUIDER`（1 次）
- `Sigmas:SIGMAS`（1 次）
- `Latent:LATENT`（1 次）
- `文本_3:STRING`（1 次）
- `文本_4:STRING`（1 次）

## 输出

- `STRING:STRING`（1 次）
- `输出:LATENT`（1 次）
- `降噪输出:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler", "unsloth/Meta-Llama-3.1-8B-Instruct", true, false, false, false, false, false, false, false, false, false, fal`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
