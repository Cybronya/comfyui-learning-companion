---
name: unknown_workflow_controlnet_inpaint_sampler_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7785
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncodeFlux, ControlNetInpaintingAliMamaApply, ControlNetLoader, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, DualCLIPLoader, EmptySD3LatentImage, Florence2Run, Florence2toCoordinates, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageCompositeMasked, JjkText, KSamplerSelect, LoadImage, MaskToImage, PreviewImage, RandomNoise, Sam2Segmentation, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, Switch mask [Crystools], Text Concatenate (JPS), UNETLoader, VAEDecode, VAELoader, easy imageSwitch]
problems: []
missing: []
members: [图片生成/图生图/Flux修复换装—Auto Mask Florence_1892461032827490305.json, 平台全量/Flux Inpainting Controlnet Beta (自动蒙板+重绘)_1838941595046715393.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux修复换装—Auto Mask Florence_1892461032827490305.json、平台全量/Flux Inpainting Controlnet Beta (自动蒙板+重绘)_1838941595046715393.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncodeFlux`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Florence2Run`
- `Florence2toCoordinates`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `RandomNoise`
- `Sam2Segmentation`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `Switch mask [Crystools]`
- `Text Concatenate (JPS)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSwitch`

**可变部分**（部分 workflow 才有）：
- `RH_Prompter` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
