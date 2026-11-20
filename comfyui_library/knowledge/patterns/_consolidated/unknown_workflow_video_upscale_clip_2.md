---
name: unknown_workflow_video_upscale_clip_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.966
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GuHaiAutoImageSplit, INTConstant, Image Blank, ImageCompositeMasked, ImageResizeKJv2, Label (rgthree), LoadImage, RepeatImageBatch, SAM3_Detect, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/小肥猴的百宝箱工作流_2073809731734564865.json, 平台全量/百宝箱工作流_2071942360543621122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_clip_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/小肥猴的百宝箱工作流_2073809731734564865.json、平台全量/百宝箱工作流_2071942360543621122.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `GuHaiAutoImageSplit`
- `INTConstant`
- `Image Blank`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `Label (rgthree)`
- `LoadImage`
- `RepeatImageBatch`
- `SAM3_Detect`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
