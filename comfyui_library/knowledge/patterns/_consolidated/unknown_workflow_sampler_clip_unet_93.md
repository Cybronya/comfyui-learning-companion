---
name: unknown_workflow_sampler_clip_unet_93
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.938545
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2.Klein图像编辑与扩图重绘_2014617059883225089.json, 图片生成/图生图/Flux2Klein 单图编辑 指定画面比例_2013884566422949890.json, 图片生成/图生图/Flux2Klein 单图编辑_2012572910803755010.json, 图片生成/图生图/Flux2Klein 去水印马赛克_2013545657268703234.json, 图片生成/图生图/Flux2Klein 高清化_2013543196827066370.json, 图片生成/图生图/Flux2Klein图像编辑终极版角色一致性_2060283231865495553.json, 图片生成/图生图/Flux2Klein图像编辑终极版角色一致性_2062072605993168898.json, 图片生成/图生图/Flux2_Klein_9B印花提取_2104442102175322114.json, 图片生成/图生图/Flux2_Klein_9B模特换脸工作流_2019648494549602305.json, 图片生成/图生图/【去文字】flux-2-klein-9b_2104893740522491906.json, 图片生成/图生图/扩图工作流（FK2）_2091708039295496194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux2.Klein图像编辑与扩图重绘_2014617059883225089.json、图片生成/图生图/Flux2Klein 单图编辑 指定画面比例_2013884566422949890.json、图片生成/图生图/Flux2Klein 单图编辑_2012572910803755010.json、图片生成/图生图/Flux2Klein 去水印马赛克_2013545657268703234.json、图片生成/图生图/Flux2Klein 高清化_2013543196827066370.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `ImageScaleToTotalPixels` —— 8/11 个有
- `ConditioningZeroOut` —— 4/11 个有
- `Image Comparer (rgthree)` —— 4/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `ImagePadForOutpaint` —— 3/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `DifferentialDiffusion` —— 2/11 个有
- `DrawMaskOnImage` —— 2/11 个有
- `IdentityFeatureTransferV3` —— 2/11 个有
- `AdjustBrightnessContrastSaturationNode` —— 1/11 个有
- `ColorMatchV2` —— 1/11 个有
- `EmptyUnitGenerator_UTK` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `ImageStitch` —— 1/11 个有
- `InpaintModelConditioning` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `easy imageConcat` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
