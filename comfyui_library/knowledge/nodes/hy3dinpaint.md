# Hy3DInPaint

## 节点类型

`Hy3DInPaint`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:HY3DPIPELINE`（1 次）
- `albedo:NPARRAY`（1 次）
- `albedo_mask:NPARRAY`（1 次）
- `mr:NPARRAY`（1 次）
- `mr_mask:NPARRAY`（1 次）
- `output_mesh_name:STRING`（1 次）

## 输出

- `pipeline:HY3DPIPELINE`（1 次）
- `albedo:IMAGE`（1 次）
- `mr:IMAGE`（1 次）
- `trimesh:TRIMESH`（1 次）
- `output_glb_path:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
