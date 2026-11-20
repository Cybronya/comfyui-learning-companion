---
name: unknown_workflow_sampler_clip_unet_210
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.861571
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/30removewatermark_2049728020415520770.json, 图片生成/图生图/FLUX2 Klein 多图编辑工作流_2091477521320734722.json, 图片生成/图生图/FLUX2-Klein扩图_2044259641374281729.json, 图片生成/图生图/FLUX2Klein一次性批量扩图_2053020098847354882.json, 图片生成/图生图/FLUX2去水印万能改图单图版保持原图不变_2059054774292664321.json, 图片生成/图生图/FLUX2去水印万能改图单图版保持原图不变_2062027536372166658.json, 平台全量/FLUX2去水印+万能改图单图版（保持原图不变）_2048961797847257089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_210

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/30removewatermark_2049728020415520770.json、图片生成/图生图/FLUX2 Klein 多图编辑工作流_2091477521320734722.json、图片生成/图生图/FLUX2-Klein扩图_2044259641374281729.json、图片生成/图生图/FLUX2Klein一次性批量扩图_2053020098847354882.json、图片生成/图生图/FLUX2去水印万能改图单图版保持原图不变_2059054774292664321.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `GrowMaskWithBlur` —— 4/7 个有
- `ImageCompositeMasked` —— 4/7 个有
- `ImageCrop+` —— 4/7 个有
- `JjkText` —— 4/7 个有
- `LayerUtility: ImageMaskScaleAs` —— 4/7 个有
- `SetLatentNoiseMask` —— 4/7 个有
- `EmptyFlux2LatentImage` —— 3/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `easy imageSize` —— 3/7 个有
- `DrawMaskOnImage` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `ImagePadForOutpaint` —— 2/7 个有
- `ImpactMakeAnyList` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
