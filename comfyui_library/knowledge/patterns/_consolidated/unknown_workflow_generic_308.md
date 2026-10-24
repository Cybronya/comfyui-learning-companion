---
name: unknown_workflow_generic_308
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8645
common_nodes: [LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/QWEN3 TTS 声音设计、克隆_2014873824315056129.json, 音频生成/音频生成/Qwen3 TTS 声音克隆-3秒克隆你的声音_2014677921528553473.json, 音频生成/音频生成/Qwen3 TTS 音频生成 -【 克隆_捏造 】_2014995925600571393.json, 音频生成/音频生成/Qwen3 TTS多功能多语言语音克隆 情感设计音色设计_2014937675089846273.json, 音频生成/音频生成/Qwen3-TTS声音设计+语音克隆+自定义声音_2014574800219414529.json, 音频生成/音频生成/Qwen3-TTS语音生成_2016416998938386433.json, 音频生成/音频生成/人物声音设计_2067086412553478146.json, 音频生成/音频生成/影视配音+游戏角色配音+有声读物+多角色+情感控制（qwen3-tts三合一）_2014646085758754818.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_308

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（音频生成/音频生成/QWEN3 TTS 声音设计、克隆_2014873824315056129.json、音频生成/音频生成/Qwen3 TTS 声音克隆-3秒克隆你的声音_2014677921528553473.json、音频生成/音频生成/Qwen3 TTS 音频生成 -【 克隆_捏造 】_2014995925600571393.json、音频生成/音频生成/Qwen3 TTS多功能多语言语音克隆 情感设计音色设计_2014937675089846273.json、音频生成/音频生成/Qwen3-TTS声音设计+语音克隆+自定义声音_2014574800219414529.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 7/8 个有
- `Qwen3TTSVoiceDesign` —— 7/8 个有
- `AudioCrop` —— 5/8 个有
- `CR Text` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `ShowText|pysssss` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `Qwen3TTSCustomVoice` —— 3/8 个有
- `SaveAudioMP3` —— 2/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
