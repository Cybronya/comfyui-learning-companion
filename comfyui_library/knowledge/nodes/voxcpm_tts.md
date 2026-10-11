# VoxCPM_TTS

## 节点类型

`VoxCPM_TTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt_audio:AUDIO`（1 次）
- `model_name:COMBO`（1 次）
- `text:STRING`（1 次）
- `cfg_value:FLOAT`（1 次）
- `inference_timesteps:INT`（1 次）
- `normalize_text:BOOLEAN`（1 次）
- `seed:INT`（1 次）
- `force_offload:BOOLEAN`（1 次）
- `device:COMBO`（1 次）
- `retry_max_attempts:INT`（1 次）

## 输出

- `Generated Audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["VoxCPM1.5", "", 2, 10, true, 688762067371974, "randomize", false, "cuda", 3, 6, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
