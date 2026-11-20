---
name: unknown_workflow_sampler_92
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8575
common_nodes: [CR Prompt Text, CR Text, ImageScaleToTotalPixels, LayerUtility: PurgeVRAM, LoadImage, Qwen3TTSModelLoader, Qwen3TTSVoiceDesign, Qwen3_VQA, SaveAudio, easy saveText, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/AA--全自动超快数字人-FlashHead+Qwen声音设计-一张图自动反推-数字人抽卡！_2030589859588476930.json, 音频生成/音频生成/AA--图生声音--自动反推Qwen3TTS声音设计--抽（声音）卡！_2017627896218656769.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_92

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/AA--全自动超快数字人-FlashHead+Qwen声音设计-一张图自动反推-数字人抽卡！_2030589859588476930.json、音频生成/音频生成/AA--图生声音--自动反推Qwen3TTS声音设计--抽（声音）卡！_2017627896218656769.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CR Text`
- `ImageScaleToTotalPixels`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceDesign`
- `Qwen3_VQA`
- `SaveAudio`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RunningHub SoulX-FlashHead Loader` —— 1/2 个有
- `RunningHub SoulX-FlashHead Sampler` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
