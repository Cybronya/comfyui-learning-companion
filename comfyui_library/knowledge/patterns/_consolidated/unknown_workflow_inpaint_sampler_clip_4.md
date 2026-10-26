---
name: unknown_workflow_inpaint_sampler_clip_4
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.831692
common_nodes: [BasicGuider, BlockifyMask, Bool, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), ImageScale, ImpactMakeAnyList, ImpactNeg, InpaintCropImproved, Int, KSamplerSelect, LayerColor: BrightnessContrastV2, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, MaskPreview, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SmartColorMatch, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageSize, easy isMaskEmpty, 取色器_孤海, 图像接缝]
problems: []
missing: []
members: [图片生成/图生图/26.04最佳换装工作流_klein局部换装_bole_2046967301148250113.json, 图片生成/图生图/F.2klein换装工作流局部换装_2057786570861793281.json, 图片生成/图生图/Flux2-klein-万物迁移-添加物品-局部重绘_2038900975137726465.json, 图片生成/图生图/Flux2-klein-小批量万物迁移（零偏移）_2015214215778275330.json, 图片生成/图生图/Flux2-klein-小批量最强万物迁移生图工作流_2053011716950249474.json, 图片生成/图生图/Flux2-klein-小批量最强万物迁移生图工作流_2053089255521570817.json, 图片生成/图生图/Flux2-klein-小物件迁移贴身衣物换装等（零偏移）_2074896943041564674.json, 图片生成/图生图/Flux2-klein-小物件迁移贴身衣物换装等（零偏移）_2082289012022267905.json, 图片生成/图生图/Klein万物迁移（零偏移）_2049015744599433217.json, 图片生成/图生图/一致性换装工作流klein局部换装_2047879539073748994.json, 图片生成/图生图/万物迁移-添加物品-局部重绘_2039149753463742465.json, 图片生成/图生图/超好用🔥批量万物迁移-提高工作效率_2053480818001104897.json, 图片生成/图生图/超好用🔥批量万物迁移-提高工作效率_2063909849330708481.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/26.04最佳换装工作流_klein局部换装_bole_2046967301148250113.json、图片生成/图生图/F.2klein换装工作流局部换装_2057786570861793281.json、图片生成/图生图/Flux2-klein-万物迁移-添加物品-局部重绘_2038900975137726465.json、图片生成/图生图/Flux2-klein-小批量万物迁移（零偏移）_2015214215778275330.json、图片生成/图生图/Flux2-klein-小批量最强万物迁移生图工作流_2053011716950249474.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BlockifyMask`
- `Bool`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImpactMakeAnyList`
- `ImpactNeg`
- `InpaintCropImproved`
- `Int`
- `KSamplerSelect`
- `LayerColor: BrightnessContrastV2`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
- `MaskPreview`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SmartColorMatch`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `easy isMaskEmpty`
- `取色器_孤海`
- `图像接缝`

**可变部分**（部分 workflow 才有）：
- `easy compare` —— 11/13 个有
- `easy imageSizeBySide` —— 11/13 个有
- `easy int` —— 11/13 个有
- `Fast Groups Bypasser (rgthree)` —— 10/13 个有
- `CR Text` —— 8/13 个有
- `ConditioningRebalanceKrea2` —— 2/13 个有
- `ImageConcatMulti` —— 2/13 个有
- `LayerMask: MaskPreview` —— 2/13 个有
- `LoraLoaderModelOnly` —— 2/13 个有
- `Preview from image [Crystools]` —— 2/13 个有
- `YuanColorMatch` —— 2/13 个有
- `孤海注释` —— 2/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
