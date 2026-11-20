# CR Module Pipe Loader

## 节点类型

`CR Module Pipe Loader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `pos:CONDITIONING`（1 次）
- `neg:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `vae:VAE`（1 次）
- `clip:CLIP`（1 次）
- `controlnet:CONTROL_NET`（1 次）
- `image:IMAGE`（1 次）
- `seed:INT`（1 次）

## 输出

- `pipe:PIPE_LINE`（1 次）
- `show_help:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[787066945739332, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
