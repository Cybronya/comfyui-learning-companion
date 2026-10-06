# UpscaleModelLoader

## 节点类型

`UpscaleModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 23 个 workflow 中。

## 输入

- `model_name:COMBO`（28 次）

## 输出

- `UPSCALE_MODEL:UPSCALE_MODEL`（28 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4x-UltraSharp.pth"]`（8 次）
- `["2xNomosUni_esrgan_multijpg.pth"]`（7 次）
- `["1xSkinContrast-High-SuperUltraCompact.pth"]`（6 次）
- `["2xNomosUni_span_multijpg_ldl.pth"]`（2 次）
- `["实时照片写实增强-4xRealWebPhoto_v4_dat2.pth"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
