# Qwen3TTSMaster

## 节点类型

`Qwen3TTSMaster`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `参考音频:AUDIO`（2 次）
- `角色预设:QWEN3_TTS_ROLE_PRESETS`（2 次）
- `文本:STRING`（2 次）
- `工作模式:COMBO`（2 次）
- `内置模型:COMBO`（2 次）
- `运行设备:COMBO`（2 次）
- `精度:COMBO`（2 次）
- `提示词:STRING`（2 次）
- `角色预设模式:COMBO`（2 次）
- `本地预设文件:COMBO`（2 次）

## 输出

- `音频:AUDIO`（2 次）
- `角色预设:QWEN3_TTS_VOICE_PROMPT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["小张：你好，这是一段测试文本。\n小号：好的我现在测试一下看看。\n小累：你们这是在干什么？", "智能对话 (Auto Dialogue)", "自动 (Auto)", "cuda", "fp16", "A gentle female`（1 次）
- `["你好，这是一段测试文本。", "智能对话 (Auto Dialogue)", "自动 (Auto)", "auto", "fp16", "A gentle female voice.", "自动角色预设", "None", "", "V`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
