---
name: unknown_workflow_generic_838
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.915
common_nodes: [Fast Groups Muter (rgthree), LoadImage, LoadVideo, RH_RhartVideoSparkvideo20ImageToVideo, RH_RhartVideoSparkvideo20MultimodalVideo, RH_RhartVideoSparkvideo20TextToVideo, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/2037504187344363522.json, 视频生成/图生视频/2038078670346133505.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_838

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2037504187344363522.json、视频生成/图生视频/2038078670346133505.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `LoadVideo`
- `RH_RhartVideoSparkvideo20ImageToVideo`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `RH_RhartVideoSparkvideo20TextToVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `RH_SparkVideoAssetCreate` —— 1/2 个有
- `RH_SparkVideoAssetIdsMerge` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
