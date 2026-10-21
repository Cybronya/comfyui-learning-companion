---
name: unknown_workflow_generic_818
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [Apply Whisper, AudioCrop, FB_Qwen3TTSVoiceClone, IndexTTS2Run, LoadAudio, PreviewAudio, PrimitiveStringMultiline, SaveAudioMP3, Text, 忽略多组孤海]
problems: []
missing: []
members: [数字人/数字人/声音克隆二合一｜Index TTS2 + Qwen3 TTS｜音色参考｜语气情感控制_2096188886392328193.json, 音频生成/音频生成/声音克隆二合一｜Index TTS2 + Qwen3 TTS｜音色参考｜语气情感控制_2094932655317020673.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_818

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/声音克隆二合一｜Index TTS2 + Qwen3 TTS｜音色参考｜语气情感控制_2096188886392328193.json、音频生成/音频生成/声音克隆二合一｜Index TTS2 + Qwen3 TTS｜音色参考｜语气情感控制_2094932655317020673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `AudioCrop`
- `FB_Qwen3TTSVoiceClone`
- `IndexTTS2Run`
- `LoadAudio`
- `PreviewAudio`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`
- `Text`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 1/2 个有
- `EmptyAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
