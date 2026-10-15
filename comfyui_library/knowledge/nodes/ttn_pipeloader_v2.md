# ttN pipeLoader_v2

## 节点类型

`ttN pipeLoader_v2`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_override:MODEL`（1 次）
- `clip_override:CLIP`（1 次）
- `optional_lora_stack:LORA_STACK`（1 次）
- `optional_controlnet_stack:CONTROL_NET_STACK`（1 次）
- `prepend_positive:STRING`（1 次）
- `prepend_negative:STRING`（1 次）

## 输出

- `pipe:PIPE_LINE`（1 次）
- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `vae:VAE`（1 次）
- `clip:CLIP`（1 次）
- `seed:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["epicrealism_pureEvolutionV5.safetensors", "Default", "Baked VAE", -1, "", "Canadian Forest, serene landscape", "none",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
