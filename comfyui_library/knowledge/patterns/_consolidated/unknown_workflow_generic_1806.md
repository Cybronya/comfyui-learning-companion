---
name: unknown_workflow_generic_1806
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8045
common_nodes: [Fast Groups Bypasser (rgthree), LoadAudio, MossTTSGenerate, MossTTSModelLoader, MossTTSVoiceDesign, SaveAudioMP3, Text]
problems: []
missing: []
members: [音频生成/音频生成/MOSS-TTS 设计声音 音色迁移 声音克隆 情绪克隆 效果逼真_2045081836572905473.json, 音频生成/音频生成/声音设计，声音克隆，音效生成 全家桶 Moss TTS_2076910745689874433.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1806

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/MOSS-TTS 设计声音 音色迁移 声音克隆 情绪克隆 效果逼真_2045081836572905473.json、音频生成/音频生成/声音设计，声音克隆，音效生成 全家桶 Moss TTS_2076910745689874433.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `MossTTSGenerate`
- `MossTTSModelLoader`
- `MossTTSVoiceDesign`
- `SaveAudioMP3`
- `Text`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `AudioSeparation` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `MossSoundEffectV2Generate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
