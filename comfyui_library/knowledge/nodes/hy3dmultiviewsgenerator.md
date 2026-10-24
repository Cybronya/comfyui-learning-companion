# Hy3DMultiViewsGenerator

## 节点类型

`Hy3DMultiViewsGenerator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `trimesh:TRIMESH`（2 次）
- `camera_config:HY3D21CAMERA`（2 次）
- `image:IMAGE`（2 次）

## 输出

- `pipeline:HY3DPIPELINE`（2 次）
- `albedo:IMAGE`（2 次）
- `mr:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[768, 10, 3, 1024, false, 429649847672371, "randomize"]`（1 次）
- `[768, 10, 3, 1024, false, 636023397259178, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
