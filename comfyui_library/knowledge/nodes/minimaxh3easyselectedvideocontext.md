# MiniMaxH3EasySelectedVideoContext

## 节点类型

`MiniMaxH3EasySelectedVideoContext`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `h3_bundle:MINIMAX_H3_BUNDLE`（1 次）
- `selected_video:VIDEO`（1 次）
- `media:*`（1 次）
- `mode:COMBO`（1 次）
- `prompt:STRING`（1 次）
- `segment_mode:COMBO`（1 次）
- `segment_cuts:STRING`（1 次）
- `context_length:INT`（1 次）
- `continuity_mode:COMBO`（1 次）
- `advanced:BOOLEAN`（1 次）

## 输出

- `model:MODEL`（1 次）
- `h3_context:MINIMAX_H3_CONTEXT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["参考生视频", "subject_definitions:\n<Subject 1> is the young woman in <Picture 1>, with shoulder-length dark hair with bang`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
