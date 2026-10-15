# RVC-Studio.PreviewAudio

## 节点类型

`RVC-Studio.PreviewAudio`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO,VHS_AUDIO`（1 次）
- `filename:STRING`（1 次）
- `save_format:COMBO`（1 次）
- `save_channels:COMBO`（1 次）
- `overwrite_existing:BOOLEAN`（1 次）
- `autoplay:BOOLEAN`（1 次）

## 输出

- `output_path:STRING`（1 次）
- `vhs_audio:VHS_AUDIO`（1 次）
- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["test", "mp3", 1, true, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
