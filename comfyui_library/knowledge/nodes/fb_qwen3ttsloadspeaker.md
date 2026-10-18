# FB_Qwen3TTSLoadSpeaker

## 节点类型

`FB_Qwen3TTSLoadSpeaker`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `filename:COMBO`（3 次）

## 输出

- `voice_clone_prompt:VOICE_CLONE_PROMPT`（3 次）
- `audio:AUDIO`（3 次）
- `ref_text:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["萝莉音.wav"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
