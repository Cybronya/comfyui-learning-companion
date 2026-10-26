---
name: unknown_workflow_sampler_clip_unet_60
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.893643
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 单图编辑【用于绘世comfyui批量管理系统】_2089195480411623426.json, 图片生成/图生图/Klein-i2i_2089727593099649025.json, 图片生成/图生图/Klein-is2i_2068689580571844609.json, 图片生成/图生图/Klein-一致性编辑_2086324766218215426.json, 图片生成/图生图/Klein9B一键生成姿态变换 改变姿势_2071187621459619841.json, 图片生成/图生图/Klein9B一键生成姿态变换 改变姿势图生图_2071957948699602945.json, 图片生成/图生图/Klein9B图片编辑_深度+线稿+法线+硬边缘控制_2070761465564459010.json, 图片生成/图生图/Klein9B姿态变换_2070588045203693570.json, 图片生成/图生图/Klein9B姿态变换_2070762335559577601.json, 图片生成/图生图/Klein9B姿态变换_2070886463251771394.json, 图片生成/图生图/Klein9B控制图片编辑6种LORA合集_2070689409061703682.json, 图片生成/图生图/flux Klein 图像编辑版 fluxklein克莱因图像编辑，图生图_2016676554306232322.json, 图片生成/图生图/flux单图v2_2103034191372963842.json, 图片生成/图生图/人物换发型_2036784926481190914.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Klein 单图编辑【用于绘世comfyui批量管理系统】_2089195480411623426.json、图片生成/图生图/Klein-i2i_2089727593099649025.json、图片生成/图生图/Klein-is2i_2068689580571844609.json、图片生成/图生图/Klein-一致性编辑_2086324766218215426.json、图片生成/图生图/Klein9B一键生成姿态变换 改变姿势_2071187621459619841.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 13/14 个有
- `ConditioningZeroOut` —— 12/14 个有
- `ImageScaleToTotalPixels` —— 12/14 个有
- `GetImageSize` —— 10/14 个有
- `PreviewImage` —— 10/14 个有
- `LoraLoaderModelOnly` —— 9/14 个有
- `AIO_Preprocessor` —— 7/14 个有
- `ImageConcatMulti` —— 6/14 个有
- `CR Text` —— 3/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/14 个有
- `PrimitiveStringMultiline` —— 3/14 个有
- `Fast Groups Bypasser (rgthree)` —— 2/14 个有
- `EasySizeSimpleImage` —— 1/14 个有
- `EmptyLatentImage` —— 1/14 个有
- `FillMaskedArea_UTK` —— 1/14 个有
- `GrowMask` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `ImageBatch` —— 1/14 个有
- `ImageResize+` —— 1/14 个有
- `LayerColor: ColorAdapter` —— 1/14 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
