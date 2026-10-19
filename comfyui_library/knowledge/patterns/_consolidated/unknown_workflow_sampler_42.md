---
name: unknown_workflow_sampler_42
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.793
common_nodes: [1hew_AudioDuration, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, RunningHub FlashTalk Loader, RunningHub FlashTalk Sampler, SaveVideo, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/AA--FlashTalk数字人+Qwen TTS声音预设-一张图生成数字主播_2029760205487087617.json, 音频生成/音频生成/AA--FlashTalk数字人+声音克隆（情感控制）_2029525701015117826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_42

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/AA--FlashTalk数字人+Qwen TTS声音预设-一张图生成数字主播_2029760205487087617.json、音频生成/音频生成/AA--FlashTalk数字人+声音克隆（情感控制）_2029525701015117826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `1hew_AudioDuration`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `RunningHub FlashTalk Loader`
- `RunningHub FlashTalk Sampler`
- `SaveVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2Run` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `Qwen3TTSCustomVoice` —— 1/2 个有
- `Qwen3TTSModelLoader` —— 1/2 个有
- `SaveAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
