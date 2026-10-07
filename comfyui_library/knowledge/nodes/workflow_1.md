# workflow>1

## 节点类型

`workflow>1`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `条件:CONDITIONING`（2 次）
- `Latent:LATENT`（2 次）
- `vae_name:COMBO`（2 次）
- `clip_name1:COMBO`（2 次）
- `clip_name2:COMBO`（2 次）
- `type:COMBO`（2 次）
- `device:COMBO`（2 次）
- `unet_name:COMBO`（2 次）
- `weight_dtype:COMBO`（2 次）
- `文本:STRING`（2 次）

## 输出

- `CLIP:CLIP`（2 次）
- `图像:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ae.sft", "clip_l.safetensors", "t5xxl_fp16.safetensors", "flux", "default", "flux1-krea-dev.safetensors", "fp8_e4m3fn"`（1 次）
- `["ae.sft", "clip_l.safetensors", "t5xxl_fp16.safetensors", "flux", "default", "flux1-krea-dev.safetensors", "fp8_e4m3fn"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
