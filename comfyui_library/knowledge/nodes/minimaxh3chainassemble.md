# MiniMaxH3ChainAssemble

## 节点类型

`MiniMaxH3ChainAssemble`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `manifest:H3_CHAIN_MANIFEST`（2 次）
- `source_audio:AUDIO`（2 次）
- `audio_source:COMBO`（2 次）
- `filename:STRING`（2 次）
- `audio_bitrate:INT`（2 次）
- `copy_to_output:BOOLEAN`（2 次）
- `output_subfolder:STRING`（2 次）
- `source_timeline:H3_SOURCE_TIMELINE`（2 次）
- `blend_video_vae:VAE`（2 次）

## 输出

- `video_path:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["plan", "t2v_normal_recovered_%date:yyyy-MM-dd%", 256, false, ""]`（1 次）
- `["plan", "t2v_normal_%date:yyyy-MM-dd%", 256, false, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
