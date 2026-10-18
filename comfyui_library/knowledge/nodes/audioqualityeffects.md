# AudioQualityEffects

## 节点类型

`AudioQualityEffects`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `pitch_shift:FLOAT`（1 次）
- `speed_factor:FLOAT`（1 次）
- `sox_path:STRING`（1 次）
- `gain_db:FLOAT`（1 次）
- `use_limiter:BOOLEAN`（1 次）
- `normalize_audio:BOOLEAN`（1 次）
- `add_reverb:BOOLEAN`（1 次）
- `reverb_amount:FLOAT`（1 次）
- `reverb_room_scale:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1, "C:\\Program Files (x86)\\sox-14-4-2\\sox.exe", 0, true, false, true, 50, 50, false, 0.5, 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
