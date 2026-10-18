# T8_IndexTTS25_DialogueGenerate

## 节点类型

`T8_IndexTTS25_DialogueGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `model:T8_INDEXTTS25_MODEL`（18 次）
- `role_library:T8_INDEXTTS25_ROLE_LIBRARY`（18 次）
- `dialogue_script:T8_INDEXTTS25_DIALOGUE_SCRIPT`（18 次）
- `sampling:T8_INDEXTTS25_SAMPLING`（18 次）
- `seed:INT`（18 次）
- `timeline_policy:COMBO`（18 次）
- `fit_srt_slots:BOOLEAN`（18 次）
- `fit_tolerance_ms:INT`（18 次）
- `batch_gap_ms:INT`（18 次）
- `slot_duration_mode:COMBO`（16 次）

## 输出

- `合并音频:AUDIO`（18 次）
- `逐句音频:AUDIO`（18 次）
- `生成报告 JSON:STRING`（18 次）
- `自动回写 SRT:STRING`（16 次）
- `可视化时间轴 JSON:STRING`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20260818, "fixed", "shift", true, 180, 200, 200, "off", 1, false, "auto", "base", "auto", 0.82, "actual", "asr_passed",`（7 次）
- `[20260818, "fixed", "shift", false, 180, 200, 200, "off", 1, false, "auto", "base", "auto", 0.82, "actual", "asr_passed"`（4 次）
- `[359939132457797, "randomize", "shift", false, "pad", 180, 200, "off", 1, false, "auto", "base", "auto", 0.82, "actual",`（2 次）
- `[201236961180857, "randomize", "shift", false, "pad", 180, 200, "off", 1, false, "auto", "base", "auto", 0.82, "actual",`（1 次）
- `[20260810, "decrement", "shift", true, 120, 200]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
