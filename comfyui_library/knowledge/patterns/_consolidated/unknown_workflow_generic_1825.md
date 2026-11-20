---
name: unknown_workflow_generic_1825
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.949
common_nodes: [Apply Whisper, AudioCrop, CR Text, LoadAudio, PreviewAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio, ShowText|pysssss, SoundFlow_Concatenator, SynVowTextSplitter, TextPreview]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3TTS（文本分为3段）_2033793004783276034.json, 音频生成/音频生成/千问语音合成（文本分段）_2032834024103743490.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1825

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3TTS（文本分为3段）_2033793004783276034.json、音频生成/音频生成/千问语音合成（文本分段）_2032834024103743490.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `AudioCrop`
- `CR Text`
- `LoadAudio`
- `PreviewAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`
- `ShowText|pysssss`
- `SoundFlow_Concatenator`
- `SynVowTextSplitter`
- `TextPreview`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
