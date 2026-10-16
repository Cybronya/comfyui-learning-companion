# MiniMaxH3ReferenceVideoPrepare

## 节点类型

`MiniMaxH3ReferenceVideoPrepare`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source_video:VIDEO`（1 次）
- `source_frames:IMAGE`（1 次）
- `source_audio:AUDIO`（1 次）
- `length:INT`（1 次）
- `source_fps:FLOAT`（1 次）

## 输出

- `ref_video:IMAGE`（1 次）
- `source_audio:AUDIO`（1 次）
- `length:INT`（1 次）
- `status:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[124, 24]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
