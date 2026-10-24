# workflow/flux模型加载

## 节点类型

`workflow/flux模型加载`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）
- `Latent:LATENT`（1 次）
- `随机种:INT`（1 次）

## 输出

- `CLIP:CLIP`（1 次）
- `模型:MODEL`（1 次）
- `VAE:VAE`（1 次）
- `Latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["t5xxl_fp8_e4m3fn.safetensors", "sd3/clip_l.safetensors", "flux", "default", "flux1-depth-dev.safetensors", "fp8_e4m3fn`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
