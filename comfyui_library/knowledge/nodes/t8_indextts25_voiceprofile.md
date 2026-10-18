# T8_IndexTTS25_VoiceProfile

## 节点类型

`T8_IndexTTS25_VoiceProfile`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `speaker_audio:AUDIO`（36 次）
- `emotion:T8_INDEXTTS25_EMOTION`（36 次）
- `role_name:STRING`（36 次）
- `language:COMBO`（36 次）

## 输出

- `角色音色:T8_INDEXTTS25_VOICE`（36 次）
- `音色信息:STRING`（36 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["角色A", "ZH"]`（17 次）
- `["角色B", "ZH"]`（16 次）
- `["旁白", "ZH"]`（1 次）
- `["12", "ZH"]`（1 次）
- `["角色C", "ZH"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
