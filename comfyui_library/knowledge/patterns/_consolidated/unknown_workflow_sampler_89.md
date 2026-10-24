---
name: unknown_workflow_sampler_89
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, RunningHub FlashTalk Loader, RunningHub FlashTalk Sampler, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/FlashTalk无限时长数字人工作流_2057455596126953474.json, 音频生成/音频生成/FlashTalk数字人_2037417128906723329.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_89

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/FlashTalk无限时长数字人工作流_2057455596126953474.json、音频生成/音频生成/FlashTalk数字人_2037417128906723329.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `RunningHub FlashTalk Loader`
- `RunningHub FlashTalk Sampler`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有
- `WujiCleaner` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
