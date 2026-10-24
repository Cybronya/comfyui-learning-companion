---
name: unknown_workflow_generic_806
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [AudioSeparation, CR Prompt Text, HeartMuLa_Transcribe, LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio, ShowText]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音_2015077485054005249.json, 音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音_2016360207449853953.json, 音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音_2069025671023779842.json, 音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音（自用）_2020884043537059842.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_806

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音_2015077485054005249.json、音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音_2016360207449853953.json、音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音_2069025671023779842.json、音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音（自用）_2020884043537059842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
- `CR Prompt Text`
- `HeartMuLa_Transcribe`
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`
- `ShowText`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `AudioCrop` —— 1/4 个有
- `Float` —— 1/4 个有
- `Int` —— 1/4 个有
- `ShowAnything|Mie` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
