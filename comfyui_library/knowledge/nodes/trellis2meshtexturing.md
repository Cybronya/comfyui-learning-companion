# Trellis2MeshTexturing

## 节点类型

`Trellis2MeshTexturing`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pipeline:TRELLIS2PIPELINE`（2 次）
- `image:IMAGE`（2 次）
- `trimesh:TRIMESH`（2 次）
- `seed:INT`（2 次）
- `texture_steps:INT`（2 次）
- `texture_guidance_strength:FLOAT`（2 次）
- `texture_guidance_rescale:FLOAT`（2 次）
- `texture_rescale_t:FLOAT`（2 次）
- `resolution:COMBO`（2 次）
- `texture_size:INT`（2 次）

## 输出

- `trimesh:TRIMESH`（2 次）
- `base_color_texture:IMAGE`（2 次）
- `metallic_roughness_texture:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[123456, "fixed", 12, 3, 0.2, 3, 1536, 2048, "OPAQUE", false, 0, 0.9, 4, false, false, 60, "euler"]`（1 次）
- `[12345, "fixed", 50, 3, 0.2, 3, 1536, 4096, "OPAQUE", false, 0, 0.9, 4, false, false, 40, "euler"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
