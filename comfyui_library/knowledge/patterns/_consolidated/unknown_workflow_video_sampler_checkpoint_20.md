---
name: unknown_workflow_video_sampler_checkpoint_20
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.859
common_nodes: [ImageOnlyCheckpointLoader, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, PrimitiveStringMultiline, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/新SONIC照片数字人+INDEX TTS1.5配音(无限制）效果太好_1894944054985752577.json, 视频生成/图生视频/新版SONIC+INDEX TTS照片数字人(无限制版）_1929379921658023937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/新SONIC照片数字人+INDEX TTS1.5配音(无限制）效果太好_1894944054985752577.json、视频生成/图生视频/新版SONIC+INDEX TTS照片数字人(无限制版）_1929379921658023937.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `IndexTTSNode` —— 1/2 个有
- `IndexTTSRun` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
