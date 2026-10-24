# easy controlnetLoader

## 节点类型

`easy controlnetLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（1 次）
- `image:IMAGE`（1 次）
- `control_net:CONTROL_NET`（1 次）

## 输出

- `pipe:PIPE_LINE`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Flux.1-dev-Controlnet-Upscaler-jasperai.safetensors", 0.6000000000000001, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
