---
name: unknown_workflow_sampler_88
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [Apply Whisper, CR Prompt Text, LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio]
problems: []
missing: []
members: [图片生成/文生图/Qwen3-TTS克隆音色_2014976486570205186.json, 音频生成/音频生成/Qwen3 TTS语音复刻（阿里最新开源）_2014610323709366274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_88

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen3-TTS克隆音色_2014976486570205186.json、音频生成/音频生成/Qwen3 TTS语音复刻（阿里最新开源）_2014610323709366274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `CR Prompt Text`
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
