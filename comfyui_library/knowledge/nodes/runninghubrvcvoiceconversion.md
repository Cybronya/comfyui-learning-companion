# RunningHubRVCVoiceConversion

## 节点类型

`RunningHubRVCVoiceConversion`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `rvc_model:RVC_MODEL`（3 次）
- `audio:AUDIO`（3 次）
- `speaker_id:INT`（3 次）
- `f0_up_key:INT`（3 次）
- `f0_method:COMBO`（3 次）
- `index_path:STRING`（3 次）
- `index_rate:FLOAT`（3 次）
- `filter_radius:INT`（3 次）
- `resample_sr:INT`（3 次）
- `rms_mix_rate:FLOAT`（3 次）

## 输出

- `audio:AUDIO`（3 次）
- `info:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, "harvest", "", 0.6600000000000001, 3, 0, 1, 0.33000000000000007]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
