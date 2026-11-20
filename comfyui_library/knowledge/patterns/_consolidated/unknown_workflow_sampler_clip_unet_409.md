---
name: unknown_workflow_sampler_clip_unet_409
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.737667
common_nodes: [BasicGuider, BlockifyMask, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), ImageColorMatch+, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy compare, easy ifElse, easy imageSizeBySide, easy int, easy isMaskEmpty]
problems: []
missing: []
members: [图片生成/图生图/flux2-klein-万能局部修复流_2021781227988062210.json, 平台全量/flux2-klein-万物消除-水印去除-小批量处理_2013177101100257281.json, 平台全量/万物移除消除 万能局部重绘flux2 klein+z-image-turbo  皮肤质感修复  优化_2022905505198383106.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_409

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux2-klein-万能局部修复流_2021781227988062210.json、平台全量/flux2-klein-万物消除-水印去除-小批量处理_2013177101100257281.json、平台全量/万物移除消除 万能局部重绘flux2 klein+z-image-turbo  皮肤质感修复  优化_2022905505198383106.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy compare`
- `easy ifElse`
- `easy imageSizeBySide`
- `easy int`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Text` —— 2/3 个有
- `取色器_孤海` —— 2/3 个有
- `CustomSamplerDetailerHookProvider` —— 1/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `INPAINT_InpaintWithModel` —— 1/3 个有
- `INPAINT_LoadInpaintModel` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `ImpactMakeAnyList` —— 1/3 个有
- `JDC_GaussianBlur` —— 1/3 个有
- `LayerColor: BrightnessContrastV2` —— 1/3 个有
- `LayerUtility: ColorPicker` —— 1/3 个有
- `LayerUtility: ImageBlend V2` —— 1/3 个有
- `MaskDetailerPipe` —— 1/3 个有
- `MaskPreview` —— 1/3 个有
- `PreviewBridge` —— 1/3 个有
- `SamplerEulerAncestralCFGPP` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `ToBasicPipe` —— 1/3 个有
- `easy imageSize` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
