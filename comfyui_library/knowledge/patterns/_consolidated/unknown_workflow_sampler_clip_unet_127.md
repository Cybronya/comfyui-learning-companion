---
name: unknown_workflow_sampler_clip_unet_127
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.965333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全能证件照Flux2-Klein9b，一致性最强_2020492624783740930.json, 图片生成/图生图/动漫转写实真人快速版_2042420411459182593.json, 图片生成/图生图/动漫转真人Klein 9b工作流_2032463178499624961.json, 图片生成/图生图/去AI塑料感与真实肤质_2051201941220405249.json, 图片生成/图生图/双图编辑_2065803421642481665.json, 图片生成/图生图/双图编辑_2066850392478146562.json, 图片生成/图生图/双模放大_2076211416096399362.json, 图片生成/图生图/图像编辑：超强一致性比肩某全能图像模型！Flux2 Klein_2030101405222047745.json, 图片生成/图生图/扩图工作流（FK2）_2091708039295496194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_127

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/全能证件照Flux2-Klein9b，一致性最强_2020492624783740930.json、图片生成/图生图/动漫转写实真人快速版_2042420411459182593.json、图片生成/图生图/动漫转真人Klein 9b工作流_2032463178499624961.json、图片生成/图生图/去AI塑料感与真实肤质_2051201941220405249.json、图片生成/图生图/双图编辑_2065803421642481665.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
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
- `Flux2Scheduler` —— 8/9 个有
- `GetImageSize` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `CR Text` —— 5/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `Int` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `AdjustBrightnessContrastSaturationNode` —— 1/9 个有
- `BasicScheduler` —— 1/9 个有
- `ColorMatchV2` —— 1/9 个有
- `DapaoImageAspectRatioResizeNode` —— 1/9 个有
- `DrawMaskOnImage` —— 1/9 个有
- `FluxKontextImageScale` —— 1/9 个有
- `ImagePadForOutpaint` —— 1/9 个有
- `easy promptConcat` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
