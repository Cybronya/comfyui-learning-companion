---
name: unknown_workflow_video_sampler_22
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.622
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, Fast Groups Bypasser (rgthree), GetImageSize, ImageConcanate, ImageFromBatch+, ImageResizeKJv2, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, RH_Sora2_I2V_PRO, RH_Sora2_I2V_Realistic, RH_Sora2_T2V_PRO, RH_Sora2_T2V_Realistic, RepeatImageBatch, SaveVideo, Text, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy cleanGpuUsed, easy compare, easy ifElse, easy showAnything]
problems: []
missing: [ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, easy compare]
members: [视频生成/图生视频/1972124351518666753.json, 视频生成/文生视频/1972124351518666753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1972124351518666753.json、视频生成/文生视频/1972124351518666753.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImageToMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `RH_Sora2_I2V_PRO`
- `RH_Sora2_I2V_Realistic`
- `RH_Sora2_T2V_PRO`
- `RH_Sora2_T2V_Realistic`
- `RepeatImageBatch`
- `SaveVideo`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`
- `easy compare`
- `easy ifElse`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、LayerUtility: ImageScaleByAspectRatio V2、easy cleanGpuUsed、easy compare
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
