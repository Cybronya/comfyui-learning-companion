# MeshyImageToModelNode

## 节点类型

`MeshyImageToModelNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `should_texture.texture_image:IMAGE`（3 次）

## 输出

- `model_file:STRING`（3 次）
- `meshy_task_id:MESHY_TASK_ID`（3 次）
- `GLB:FILE_3D_GLB`（3 次）
- `FBX:FILE_3D_FBX`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["meshy-7.1", "true", "triangle", 300000, "auto", "true", false, "", "2k", "", 978222859, "randomize", false, "2k"]`（1 次）
- `["meshy-7.1", "true", "triangle", 300000, "auto", "true", false, "", "2k", "", 10793226, "randomize", false, "2k"]`（1 次）
- `["meshy-6", "true", "triangle", 300000, "auto", "true", false, "", "2k", "", 0, "randomize", false, "2k"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
