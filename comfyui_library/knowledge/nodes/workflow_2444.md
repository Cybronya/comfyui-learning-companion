# workflow>人物皮肤高清

## 节点类型

`workflow>人物皮肤高清`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `captions:STRING`（1 次）
- `value:INT`（1 次）
- `ckpt_name:COMBO`（1 次）
- `model_name:COMBO`（1 次）
- `CheckpointLoaderSimple ckpt_name:COMBO`（1 次）
- `UpscaleModelLoader model_name:COMBO`（1 次）
- `interpolation:COMBO`（1 次）
- `method:COMBO`（1 次）
- `condition:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `ColorMatch 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1360, "flux1-dev-fp8.safetensors", "x1_ITF_SkinDiffDetail_Lite_v1.pth", "dreamshaperXL_lightningDPMSDE.safetensors", "4`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
