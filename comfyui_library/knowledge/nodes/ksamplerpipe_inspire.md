# KSamplerPipe //Inspire

## 节点类型

`KSamplerPipe //Inspire`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `basic_pipe:BASIC_PIPE`（2 次）
- `latent_image:LATENT`（2 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（2 次）

## 输出

- `LATENT:LATENT`（2 次）
- `VAE:VAE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[445761961111119, "randomize", 25, 6, "euler_ancestral", "karras", 1, "GPU(=A1111)", "incremental", 0, 0]`（1 次）
- `[158899589223481, "randomize", 15, 4, "euler", "karras", 0.4000000000000001, "GPU(=A1111)", "incremental", 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
