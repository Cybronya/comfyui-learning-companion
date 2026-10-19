---
name: unknown_workflow_video_sampler_32
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.688
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, Fast Groups Muter (rgthree), FlashVSRNode, ImageConcanate, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, MaskToImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VHS_VideoInfoLoaded, easy compare, easy ifElse, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1993299080321368065.json, 视频生成/图生视频/1993311600947953666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1993299080321368065.json、视频生成/图生视频/1993311600947953666.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `Fast Groups Muter (rgthree)`
- `FlashVSRNode`
- `ImageConcanate`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VHS_VideoInfoLoaded`
- `easy compare`
- `easy ifElse`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
