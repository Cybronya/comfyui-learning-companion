# workflow>光影优化V3

## 节点类型

`workflow>光影优化V3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（2 次）
- `vae_name:COMBO`（2 次）
- `sampler_name:COMBO`（2 次）
- `clip_name:COMBO`（2 次）
- `type:COMBO`（2 次）
- `device:COMBO`（2 次）
- `noise_seed:INT`（2 次）
- `text:STRING`（2 次）
- `unet_name:COMBO`（2 次）
- `weight_dtype:COMBO`（2 次）

## 输出

- `显示帮助:STRING`（2 次）
- `宽度:INT`（2 次）
- `高度:INT`（2 次）
- `batch_size:INT`（2 次）
- `降噪输出:LATENT`（2 次）
- `图像:IMAGE`（2 次）
- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux2-vae.safetensors", "euler_ancestral", "qwen_3_8b.safetensors", "flux2", "default", 274619068013102, "randomize", `（1 次）
- `["flux2-vae.safetensors", "euler_ancestral", "qwen_3_8b.safetensors", "flux2", "default", 68353210357643, "randomize", "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
