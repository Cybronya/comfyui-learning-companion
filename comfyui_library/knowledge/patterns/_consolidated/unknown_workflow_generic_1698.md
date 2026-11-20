---
name: unknown_workflow_generic_1698
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.929
common_nodes: [BitwiseAndMask, CR Text, Display Any (rgthree), GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageBatchGet, ImageBorder, ImageScale, ImageToMask, LayerUtility: LaMa, LoadImage, MaskFromColor+, MaskToImage, Masks Combine Regions, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, RH_LLMAPI_NODE, SAMModelLoader (segment anything), SaveImage, SeedVR2, SeedVR2BlockSwap, VHS_DuplicateMasks, easy cleanGpuUsed, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy imageCount, easy imageSize, easy int, easy showAnything, ttN concat]
problems: []
missing: []
members: [图片生成/图生图/去水印+高清放大批量工作流_1983749663184592898.json, 平台全量/seedvr2图片高清去rh水印高清放大批量图片打包zip批量高清处理去rh水印工作流_2011773260723134465.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1698

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/去水印+高清放大批量工作流_1983749663184592898.json、平台全量/seedvr2图片高清去rh水印高清放大批量图片打包zip批量高清处理去rh水印工作流_2011773260723134465.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BitwiseAndMask`
- `CR Text`
- `Display Any (rgthree)`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageBatchGet`
- `ImageBorder`
- `ImageScale`
- `ImageToMask`
- `LayerUtility: LaMa`
- `LoadImage`
- `MaskFromColor+`
- `MaskToImage`
- `Masks Combine Regions`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `RH_LLMAPI_NODE`
- `SAMModelLoader (segment anything)`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `VHS_DuplicateMasks`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy imageSize`
- `easy int`
- `easy showAnything`
- `ttN concat`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
