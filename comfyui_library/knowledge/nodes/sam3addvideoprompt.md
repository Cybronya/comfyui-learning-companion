# SAM3AddVideoPrompt

## 节点类型

`SAM3AddVideoPrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `session:SAM3_VIDEO_SESSION`（2 次）
- `boxes:SAM3_BOXES_PROMPT`（2 次）
- `points:SAM3_POINTS_PROMPT`（2 次）
- `frame_index:INT`（2 次）
- `text_prompt:STRING`（2 次）
- `obj_id:INT`（2 次）

## 输出

- `session:SAM3_VIDEO_SESSION`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "", 1]`（1 次）
- `[0, "motorcycle", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
