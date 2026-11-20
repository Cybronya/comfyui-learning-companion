---
name: unknown_workflow_sampler_93
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.793
common_nodes: [1hew_AudioDuration, CR Prompt Text, LayerUtility: PurgeVRAM, LoadImage, RunningHub SoulX-FlashHead Loader, RunningHub SoulX-FlashHead Sampler, SaveVideo, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/AA--情感控制数字人-超快FlashHead+index声音克隆（8种情感控制）_2030585203055398914.json, 数字人/数字人/AA--预设声音超快数字人-FlashHead+QwenTTS -一张图9种语音_2030658043398070273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_93

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/AA--情感控制数字人-超快FlashHead+index声音克隆（8种情感控制）_2030585203055398914.json、数字人/数字人/AA--预设声音超快数字人-FlashHead+QwenTTS -一张图9种语音_2030658043398070273.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `1hew_AudioDuration`
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `RunningHub SoulX-FlashHead Loader`
- `RunningHub SoulX-FlashHead Sampler`
- `SaveVideo`
- `easy cleanGpuUsed`
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
