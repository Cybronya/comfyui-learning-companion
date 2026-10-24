# LayerMask: ObjectDetectorYOLOWorld

## 节点类型

`LayerMask: ObjectDetectorYOLOWorld`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `prompt:STRING`（1 次）

## 输出

- `bboxes:BBOXES`（3 次）
- `preview:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["yolo_world/v2-x", 0.05, 0.3, "person", "left_to_right", "by_index", "0,"]`（1 次）
- `["yolo_world/v2-x", 0.05, 0.3, "person", "left_to_right", "by_index", "1,"]`（1 次）
- `["yolo_world/v2-x", 0.05, 0.3, "subject", "left_to_right", "all", "0,"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
