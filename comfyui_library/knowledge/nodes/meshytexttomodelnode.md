# MeshyTextToModelNode

## 节点类型

`MeshyTextToModelNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输出

- `model_file:STRING`（3 次）
- `meshy_task_id:MESHY_TASK_ID`（3 次）
- `GLB:FILE_3D_GLB`（3 次）
- `FBX:FILE_3D_FBX`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["meshy-7.1", "Isometric low-poly 3D diorama of a rustic white farmhouse with a blue gabled roof, on an isolated square `（1 次）
- `["meshy-7", "Anubis, jackal-headed god of the dead, full body, black obsidian body with gold trim, ornate ankh staff, st`（1 次）
- `["meshy-6", "Death Knight", "realistic", "true", "triangle", 300000, "auto", "", 0, "randomize", false, "2k"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
