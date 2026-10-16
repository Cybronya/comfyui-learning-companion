# MiniMaxH3ChainExternalVideo

## 节点类型

`MiniMaxH3ChainExternalVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `plan:H3_CHAIN_PLAN`（4 次）
- `source_video:VIDEO`（4 次）
- `source_frames:IMAGE`（4 次）
- `source_audio:AUDIO`（4 次）
- `source_fps:FLOAT`（4 次）
- `prepend_original:BOOLEAN`（4 次）

## 输出

- `external_context:H3_CHAIN_EXTERNAL_CONTEXT`（4 次）
- `status:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, true]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
