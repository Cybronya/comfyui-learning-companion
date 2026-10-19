---
name: unknown_workflow_generic_755
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9335
common_nodes: [LoadAudio, LoadImage, LoadVideo, RH_RhartVideoSparkvideo20FastImageToVideo, RH_RhartVideoSparkvideo20FastMultimodalVideo, RH_RhartVideoSparkvideo20FastTextToVideo, RH_RhartVideoSparkvideo20ImageToVideo, RH_RhartVideoSparkvideo20MultimodalVideo, RH_RhartVideoSparkvideo20TextToVideo, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/Seedance 2.0 文生+图生+全能参考视频合集 含标准版与Fest版_2046116322349686786.json, 视频生成/文生视频/Seedance2.0 Fast+Seedance2.0视频七合一_2053655017139253249.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_755

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Seedance 2.0 文生+图生+全能参考视频合集 含标准版与Fest版_2046116322349686786.json、视频生成/文生视频/Seedance2.0 Fast+Seedance2.0视频七合一_2053655017139253249.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `RH_RhartVideoSparkvideo20FastImageToVideo`
- `RH_RhartVideoSparkvideo20FastMultimodalVideo`
- `RH_RhartVideoSparkvideo20FastTextToVideo`
- `RH_RhartVideoSparkvideo20ImageToVideo`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `RH_RhartVideoSparkvideo20TextToVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `RH_SparkVideoAssetCreate` —— 1/2 个有
- `RH_SparkVideoAssetIdsMerge` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
