# AceMusicSettings

## 节点类型

`AceMusicSettings`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `duration:FLOAT`（4 次）
- `vocal_language:COMBO`（4 次）
- `bpm:INT`（4 次）
- `timesignature:COMBO`（4 次）
- `keyscale:COMBO`（4 次）
- `instrumental:BOOLEAN`（4 次）
- `inference_steps:INT`（4 次）
- `guidance_scale:FLOAT`（4 次）
- `seed:INT`（4 次）

## 输出

- `settings:ACEMUSIC_SETTINGS`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, "ja", 120, "4/4", "", false, 27, 15, 753427483, "randomize"]`（1 次）
- `[30, "ja", 120, "4/4", "", false, 27, 15, 1265049492, "randomize"]`（1 次）
- `[150, "ja", 120, "4/4", "", false, 27, 15, 1820295140, "randomize"]`（1 次）
- `[60, "zh", 240, "4/4", "", false, 27, 15, 1213805668, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
