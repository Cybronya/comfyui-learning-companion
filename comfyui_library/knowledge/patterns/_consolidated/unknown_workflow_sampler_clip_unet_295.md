---
name: unknown_workflow_sampler_clip_unet_295
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.925
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, FastCanvas, FastCanvasTool, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 双图编辑 极速4步模特换衣换装溶图光影融合_2014176840830685186.json, 图片生成/图生图/Flux2 Klein 编辑多合一版  多图保持人物一致性丨产品光影融合_2022519193781936129.json, 图片生成/图生图/Klein 编辑多合一版  多图保持人物一致性丨产品光影融合 林耀_2014020601354133505.json, 图片生成/文生图/Klein 编辑多合一版_2073302428295983105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_295

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 双图编辑 极速4步模特换衣换装溶图光影融合_2014176840830685186.json、图片生成/图生图/Flux2 Klein 编辑多合一版  多图保持人物一致性丨产品光影融合_2022519193781936129.json、图片生成/图生图/Klein 编辑多合一版  多图保持人物一致性丨产品光影融合 林耀_2014020601354133505.json、图片生成/文生图/Klein 编辑多合一版_2073302428295983105.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `FastCanvas`
- `FastCanvasTool`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `AILab_QwenVL` —— 3/4 个有
- `AIO_Preprocessor` —— 3/4 个有
- `CR Prompt List` —— 3/4 个有
- `ColorMatch` —— 3/4 个有
- `DrawMaskOnImage` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `BiRefNetRMBG` —— 1/4 个有
- `DetailTransfer` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LayerMask: MaskGrow` —— 1/4 个有
- `LayerMask: MaskPreview` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
