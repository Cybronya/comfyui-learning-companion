# VoxCPM_SRT_Processor

## 节点类型

`VoxCPM_SRT_Processor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:VOXCPM_MODEL`（1 次）
- `cache_group:CACHE_GROUP`（1 次）
- `srt_text:STRING`（1 次）
- `normalize_text:BOOLEAN`（1 次）
- `stretch_method:COMBO`（1 次）
- `stretch_n_fft:INT`（1 次）
- `stretch_hop_length:INT`（1 次）
- `keep_model_loaded:BOOLEAN`（1 次）
- `cfg_value:FLOAT`（1 次）
- `inference_timesteps:INT`（1 次）

## 输出

- `AUDIO:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["\n1\n00:00:00,100 --> 00:00:04,500\n我要分享给你所有的金钱法则，让你无需天赋、\n\n2\n00:00:04,500 --> 00:00:07,200\n运气或信托基金也能致富。\n\n3\n00:0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
