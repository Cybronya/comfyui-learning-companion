---
name: unknown_workflow_sampler_clip_unet_57
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.956929
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX克莱因指令编辑_2019953559508361217.json, 图片生成/图生图/Flux 2 klein 4b 强力换头_2038542238401171457.json, 图片生成/图生图/Flux 2 klein 4b 换头工作流_2012867203107917825.json, 图片生成/图生图/Flux 2 klein 9b 100% 只换脸工作流_2016484736058793986.json, 图片生成/图生图/Flux 2 klein 9b 换脸非换头工作流_2017157128376557570.json, 图片生成/图生图/Flux klein100%换脸工作流（不改发型）_2030855449922248705.json, 图片生成/图生图/Flux2 Klein 单图编辑9B版_2012107262248095745.json, 图片生成/图生图/Flux2 Klein 图像编辑4B版V1_2012059257029533698.json, 图片生成/图生图/Flux2 Klein 图像编辑9B版V1_2012042587716194306.json, 图片生成/图生图/Flux2 Klein 图像编辑9B版_2012348312397029378.json, 图片生成/图生图/Flux2 Klein 图像编辑9B版（15s出图）_2012157839531315202.json, 图片生成/图生图/Flux2-Klein-9B双图效果图洗图_2018610383409389569.json, 图片生成/图生图/Flux2-Klein-9B双图编辑_2013423771364888578.json, 图片生成/图生图/亚秒级40秒100%换脸工作流 V1.00404_2040329795237584898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_57

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/FLUX克莱因指令编辑_2019953559508361217.json、图片生成/图生图/Flux 2 klein 4b 强力换头_2038542238401171457.json、图片生成/图生图/Flux 2 klein 4b 换头工作流_2012867203107917825.json、图片生成/图生图/Flux 2 klein 9b 100% 只换脸工作流_2016484736058793986.json、图片生成/图生图/Flux 2 klein 9b 换脸非换头工作流_2017157128376557570.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 13/14 个有
- `GetImageSize` —— 12/14 个有
- `Image Comparer (rgthree)` —— 9/14 个有
- `CR Text` —— 8/14 个有
- `ImageConcanate` —— 6/14 个有
- `LayerColor: Brightness & Contrast` —— 4/14 个有
- `LayerUtility: CropByMask V2` —— 4/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `MaskPreview` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `ycFaceMaskCreator` —— 3/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/14 个有
- `easy int` —— 2/14 个有
- `easy seed` —— 2/14 个有
- `FaceToMask` —— 1/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `ImageResize+` —— 1/14 个有
- `JjkText` —— 1/14 个有
- `LayerMask: RemBgUltra` —— 1/14 个有
- `LoraLoaderModelOnly` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
