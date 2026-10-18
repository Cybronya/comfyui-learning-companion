# AuKGenerateEdit

## 节点类型

`AuKGenerateEdit`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `engine:AUK_ENGINE`（6 次）
- `input_audio:AUDIO`（6 次）
- `task:COMBO`（6 次）
- `primary:STRING`（6 次）
- `secondary:STRING`（6 次）
- `generation_seconds:FLOAT`（6 次）
- `seed:INT`（6 次）
- `nfe_steps:INT`（6 次）
- `cfg_strength:FLOAT`（6 次）
- `sway_sampling_coef:FLOAT`（6 次）

## 输出

- `生成音频:AUDIO`（6 次）
- `最终指令:STRING`（6 次）
- `运行参数 JSON:STRING`（6 次）
- `实际目标时长（秒）:FLOAT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["语音文字编辑", "把“把夜色这么美”改成“今晚那么美”", "", 12, 716062525334435, "randomize", 32, 2, -1]`（1 次）
- `["语音文字编辑", "把“把夜色这么美”改成“今晚那么美”", "", 12, 437275233125224, "randomize", 32, 2, -1, "自动适配（按任务规则）"]`（1 次）
- `["语音文字编辑", "把“把夜色这么美”改成“今晚那么美”", "", 12, 160513612066718, "randomize", 32, 2, -1, "自动适配（按任务规则）"]`（1 次）
- `["语音文字编辑", "把“把夜色这么美”改成“今晚那么美”", "", 12, 39052579102412, "randomize", 32, 2, -1, "自动适配（按任务规则）"]`（1 次）
- `["歌词编辑", "把“把夜色这么美”改成“今晚那么美”", "", 12, 144664179349332, "randomize", 32, 2, -1, "自动适配（按任务规则）"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
