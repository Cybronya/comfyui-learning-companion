# SoulXPodcastInputParser

## 节点类型

`SoulXPodcastInputParser`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `soulx_model:SOULX_MODEL`（2 次）
- `S1_prompt_audio:AUDIO`（2 次）
- `S2_prompt_audio:AUDIO`（2 次）
- `input_mode:COMBO`（2 次）
- `dialogue_script:STRING`（2 次）
- `json_config:STRING`（2 次）

## 输出

- `PODCAST_INPUT:PODCAST_INPUT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["simple", "[S1]前两天滔博打T1大家都看了没，<|breathing|>给我气得睡不着觉。<|breathing|>虽然赛前就知道滔博要被抽陀螺，但也没想到拉了这么一坨大的。<|breathing|>别的不说，就说kanav`（1 次）
- `["json", "[S1] 作者是QQ842850240", "{\n    \"speakers\": {\n      \"S1\": {\n        \"prompt_audio\": \"example/audios/fem`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
