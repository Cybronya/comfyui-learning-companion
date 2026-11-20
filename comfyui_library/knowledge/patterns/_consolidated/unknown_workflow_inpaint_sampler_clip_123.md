---
name: unknown_workflow_inpaint_sampler_clip_123
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7835
common_nodes: [Any Switch (rgthree), BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, FluxKontextImageScale, GetImageSize, GroundingDinoModelLoader_SDPose, ImageScaleBy, ImageScaleToTotalPixels, InpaintCropImproved, KSamplerSelect, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, SaveImage, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy sleep]
problems: []
missing: []
members: [平台全量/flux2-klein-婚纱摄影师-虚拟影楼_2022320775746822145.json, 平台全量/服饰动作姿势迁移 Flux2-Klein9b 婚纱摄影师 虚拟影楼_2022910382142136322.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/flux2-klein-婚纱摄影师-虚拟影楼_2022320775746822145.json、平台全量/服饰动作姿势迁移 Flux2-Klein9b 婚纱摄影师 虚拟影楼_2022910382142136322.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `FluxKontextImageScale`
- `GetImageSize`
- `GroundingDinoModelLoader_SDPose`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `InpaintCropImproved`
- `KSamplerSelect`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy sleep`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
