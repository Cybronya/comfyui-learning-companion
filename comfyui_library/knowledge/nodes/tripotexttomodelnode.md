# TripoTextToModelNode

## 节点类型

`TripoTextToModelNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输出

- `model_file:STRING`（3 次）
- `model task_id:MODEL_TASK_ID`（3 次）
- `GLB:FILE_3D_GLB`（3 次）
- `FBX:FILE_3D_FBX`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Create a 3D game monster design, majestic and powerful creature, muscular build, imposing stature, heroic proportions,`（1 次）
- `["armored knight kneeling with sword, ornate silver-gold plate armor, white cape", "", "v3.1-20260211", "None", true, tr`（1 次）
- `["Generate a 3D model of a steampunk-inspired spider drone with brass legs, steam vents, and a camera eye, set in a crou`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
