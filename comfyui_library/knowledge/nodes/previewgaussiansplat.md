# PreviewGaussianSplat

## 节点类型

`PreviewGaussianSplat`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model_3d:FILE_3D_SPLAT_ANY,FILE_3D_PLY,FILE_3D_SPLAT,FILE_3D_SPZ,FILE_3D_KSPLAT`（2 次）
- `model_3d_info:LOAD3D_MODEL_INFO`（2 次）
- `camera_info:LOAD3D_CAMERA`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `viewport_state:LOAD_3D`（1 次）

## 输出

- `model_3d:FILE_3D_SPLAT_ANY`（2 次）
- `model_3d_info:LOAD3D_MODEL_INFO`（2 次）
- `camera_info:LOAD3D_CAMERA`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1024, 1025, 1024, 1024]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
