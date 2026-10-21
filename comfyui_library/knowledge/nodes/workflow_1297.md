# workflow>高清节点

## 节点类型

`workflow>高清节点`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `cache_model:MODEL`（5 次）
- `torch_compile_args:SEEDVR2_TORCH_COMPILE`（5 次）
- `SeedVR2LoadDiTModel cache_model:MODEL`（5 次）
- `SeedVR2LoadDiTModel torch_compile_args:SEEDVR2_TORCH_COMPILE`（5 次）
- `图像:IMAGE`（5 次）
- `输入任何:*`（5 次）
- `tile_debug:COMBO`（5 次）
- `offload_device:COMBO`（5 次）
- `model:COMBO`（5 次）
- `device:COMBO`（5 次）

## 输出

- `count:INT`（5 次）
- `output:*`（5 次）
- `easy showAnything output:*`（5 次）
- `宽度:INT`（5 次）
- `高度:INT`（5 次）
- `GetImageSize+ count:INT`（5 次）
- `easy showAnything 12 output:*`（5 次）
- `easy showAnything 13 output:*`（5 次）
- `ImageResize+ 宽度:INT`（5 次）
- `ImageResize+ 高度:INT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["false", "none", "ema_vae_fp16.safetensors", "cuda:0", false, 256, 32, false, 256, 32, "seedvr2_ema_7b_fp16.safetensors`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
