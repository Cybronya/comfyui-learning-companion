---
name: unknown_workflow_generic_925
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.801
common_nodes: [CR Text, ImageScaleToTotalPixels, LayerUtility: PurgeVRAM, LoadImage, Qwen3_VQA, SaveAudio, easy saveText, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/AA--图生声音--自动反推Qwen3TTS声音设计--抽（声音）卡！_2017627896218656769.json, 音频生成/音频生成/图生声音！VoxCPM2声音设计+Qwen3图片反推_2042769705978568706.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_925

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/AA--图生声音--自动反推Qwen3TTS声音设计--抽（声音）卡！_2017627896218656769.json、音频生成/音频生成/图生声音！VoxCPM2声音设计+Qwen3图片反推_2042769705978568706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `ImageScaleToTotalPixels`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Qwen3_VQA`
- `SaveAudio`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `Qwen3TTSModelLoader` —— 1/2 个有
- `Qwen3TTSVoiceDesign` —— 1/2 个有
- `RunningHub_VoxCPM_Generate` —— 1/2 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
