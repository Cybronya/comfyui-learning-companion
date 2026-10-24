# easy kSamplerInpainting

## 节点类型

`easy kSamplerInpainting`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（2 次）
- `model:MODEL`（2 次）
- `mask:MASK`（2 次）

## 输出

- `pipe:PIPE_LINE`（2 次）
- `image:IMAGE`（2 次）
- `vae:VAE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[6, "Preview", 0, "ComfyUI", "None", ""]`（1 次）
- `[20, "Preview", 0, "ComfyUI", "None", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
