---
name: unknown_workflow_sampler_clip_unet_35
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.854579
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2 Klein 局部重绘工作流_2091475570843541506.json, 图片生成/图生图/FLUX2-KLEIN-局部重绘_2086451671395291138.json, 图片生成/图生图/FLUX2-Klein局部重绘_2042440525696995329.json, 图片生成/图生图/Flux2 Klein 单图编辑 超i真实_2012736153442590722.json, 图片生成/图生图/Flux2 Klein 图像编辑_2012796994577764354.json, 图片生成/图生图/Flux2+Klein+单图像编辑（单图）_2013840360472059905.json, 图片生成/图生图/Flux2+Klein+图像编辑（单图）_2013803586651693057.json, 图片生成/图生图/flux2-klein-转绘各种效果，效果好，速度快，百分百场景一致性，全能型_2018953900497313793.json, 图片生成/图生图/【建筑&室内&景观】超实用工作流合集-基于FLUX2-KLEIN_2014522302368587778.json, 图片生成/图生图/【建筑&室内&景观】超实用工作流合集-基于FLUX2-KLEIN_2081670375993335809.json, 图片生成/图生图/【建筑&室内&景观】超实用工作流合集-基于FLUX2-KLEIN_2094715505419579394.json, 图片生成/图生图/【建筑&室内&景观】超实用工作流合集-基于FLUX2-KLEIN_2111682766764077058.json, 图片生成/图生图/【超实用工作流合集】-建筑&室内&景观-可按需调整_2056623443910684673.json, 图片生成/图生图/局部修改重绘_2062470852343590914.json, 图片生成/图生图/局部重绘工作流_2095404630556631041.json, 图片生成/图生图/建筑&室内&景观FLUX2-KLEIN_指定位置替换指定物品_2081674408481083394.json, 图片生成/图生图/建筑&室内&景观FLUX2-KLEIN_指定位置替换指定物品_2097163934771015681.json, 图片生成/图生图/建筑&室内&景观FLUX2-KLEIN_指定位置替换指定物品_2097504190967926786.json, 图片生成/文生图/【建筑&室内&景观】超实用工作流合集-基于FLUX2-KLEIN_2060292542750613506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_35

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/FLUX2 Klein 局部重绘工作流_2091475570843541506.json、图片生成/图生图/FLUX2-KLEIN-局部重绘_2086451671395291138.json、图片生成/图生图/FLUX2-Klein局部重绘_2042440525696995329.json、图片生成/图生图/Flux2 Klein 单图编辑 超i真实_2012736153442590722.json、图片生成/图生图/Flux2 Klein 图像编辑_2012796994577764354.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 19 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `Image Comparer (rgthree)` —— 18/19 个有
- `ImageResizeKJv2` —— 16/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/19 个有
- `PrimitiveStringMultiline` —— 16/19 个有
- `PlaySound|pysssss` —— 15/19 个有
- `PreviewImage` —— 15/19 个有
- `EmptyFlux2LatentImage` —— 14/19 个有
- `InpaintModelConditioning` —— 14/19 个有
- `ColorMatch` —— 13/19 个有
- `INPAINT_ExpandMask` —— 13/19 个有
- `ImageAndMaskPreview` —— 13/19 个有
- `ImageCompositeMasked` —— 13/19 个有
- `GetImageSize` —— 12/19 个有
- `DrawMaskOnImage` —— 9/19 个有
- `Fast Groups Bypasser (rgthree)` —— 9/19 个有
- `ImagePadForOutpaint` —— 9/19 个有
- `PrimitiveInt` —— 6/19 个有
- `FluxKontextImageScale` —— 3/19 个有
- `LayerUtility: ImageReel` —— 3/19 个有
- `LayerUtility: ImageReelComposit` —— 3/19 个有
- `RH_Translator` —— 2/19 个有
- `DifferentialDiffusion` —— 1/19 个有
- `SetNode` —— 1/19 个有
- `easy imageConcat` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
