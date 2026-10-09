# Hy3DRenderMultiView

## 节点类型

`Hy3DRenderMultiView`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `trimesh:TRIMESH`（2 次）
- `camera_config:HY3DCAMERA`（2 次）
- `render_size:INT`（2 次）
- `texture_size:INT`（2 次）
- `normal_space:COMBO`（2 次）

## 输出

- `normal_maps:IMAGE`（2 次）
- `position_maps:IMAGE`（2 次）
- `renderer:MESHRENDER`（2 次）
- `masks:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 2048, "world"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
