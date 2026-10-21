# workflow>扩图V2

## 节点类型

`workflow>扩图V2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `图像:IMAGE`（4 次）
- `vae_name:COMBO`（4 次）
- `sampler_name:COMBO`（4 次）
- `clip_name:COMBO`（4 次）
- `type:COMBO`（4 次）
- `device:COMBO`（4 次）
- `noise_seed:INT`（4 次）
- `unet_name:COMBO`（4 次）
- `weight_dtype:COMBO`（4 次）
- `width:INT`（4 次）

## 输出

- `宽度:INT`（4 次）
- `高度:INT`（4 次）
- `batch_size:INT`（4 次）
- `降噪输出:LATENT`（4 次）
- `图像:IMAGE`（4 次）
- `IMAGE:IMAGE`（4 次）
- `MASK:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux2-vae.safetensors", "euler_ancestral", "qwen_3_8b.safetensors", "flux2", "default", 580555745639320, "randomize", `（1 次）
- `["flux2-vae.safetensors", "euler_ancestral", "qwen_3_8b.safetensors", "flux2", "default", 385311236105495, "randomize", `（1 次）
- `["flux2-vae.safetensors", "euler_ancestral", "qwen_3_8b.safetensors", "flux2", "default", 615892605061943, "randomize", `（1 次）
- `["flux2-vae.safetensors", "euler_ancestral", "qwen_3_8b.safetensors", "flux2", "default", 854507388907394, "randomize", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
