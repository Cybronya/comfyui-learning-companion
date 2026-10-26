---
name: unknown_workflow_video_sampler_checkpoint_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [ImageOnlyCheckpointLoader, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, SaveAudio, SeedVCRun, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/一键AI翻唱数字人SeedVc V2+Sonic_2029594346034569218.json, 音频生成/音频生成/一键AI翻唱数字人SeedVc V2+Sonic_1932990691872215042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/一键AI翻唱数字人SeedVc V2+Sonic_2029594346034569218.json、音频生成/音频生成/一键AI翻唱数字人SeedVc V2+Sonic_1932990691872215042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SaveAudio`
- `SeedVCRun`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 1/2 个有
- `MergeAudioNode` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
