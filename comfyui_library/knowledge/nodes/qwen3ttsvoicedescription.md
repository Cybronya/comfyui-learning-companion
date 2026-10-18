# Qwen3TTSVoiceDescription

## 节点类型

`Qwen3TTSVoiceDescription`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `上一个提示词:STRING`（3 次）
- `基础音色:COMBO`（3 次）
- `音色质感:COMBO`（3 次）
- `情感状态:COMBO`（3 次）
- `风格场景:COMBO`（3 次）
- `自定义描述:STRING`（3 次）

## 输出

- `提示词:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["男童", "清脆", "热情", "流畅", ""]`（2 次）
- `["中年男", "高亢", "不选择", "语速快", "有自信地，有一种说教感"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
