---
name: unknown_workflow_inpaint_sampler_clip_2
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.836238
common_nodes: [BasicGuider, BlockifyMask, Bool, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), ImageScale, ImpactNeg, InpaintCropImproved, Int, KSamplerSelect, LayerColor: BrightnessContrastV2, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, MaskPreview, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SmartColorMatch, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageSize, easy isMaskEmpty, 取色器_孤海, 图像接缝]
problems: []
missing: []
members: [图片生成/图生图/26.04最佳换装工作流_klein局部换装_bole_2046967301148250113.json, 图片生成/图生图/F.2klein换装工作流局部换装_2057786570861793281.json, 图片生成/图生图/Flux2-klein-万物迁移-添加物品-局部重绘_2038900975137726465.json, 图片生成/图生图/Flux2-klein-小批量万物迁移（零偏移）_2015214215778275330.json, 图片生成/图生图/Flux2-klein-小批量最强万物迁移生图工作流_2053011716950249474.json, 图片生成/图生图/Flux2-klein-小批量最强万物迁移生图工作流_2053089255521570817.json, 图片生成/图生图/Flux2-klein-小物件迁移贴身衣物换装等（零偏移）_2074896943041564674.json, 图片生成/图生图/Flux2-klein-小物件迁移贴身衣物换装等（零偏移）_2082289012022267905.json, 图片生成/图生图/Klein万物迁移（零偏移）_2049015744599433217.json, 图片生成/图生图/一致性换装工作流klein局部换装_2047879539073748994.json, 图片生成/图生图/万物迁移-添加物品-局部重绘_2039149753463742465.json, 图片生成/图生图/超好用🔥批量万物迁移-提高工作效率_2053480818001104897.json, 图片生成/图生图/超好用🔥批量万物迁移-提高工作效率_2063909849330708481.json, 平台全量/F.2klein换装工作流局部换装_2054565282970128386.json, 平台全量/Flux2-Klein 一键局部换装_2077560166907727874.json, 平台全量/Flux2-klein 万物迁移 添加物品 局部重绘 电商产品迁移 人物模特服饰 珠宝首饰迁移 产品_2020033260436328449.json, 平台全量/flux2-klein-万物迁移-添加物品-局部重绘_2013411647783706626.json, 平台全量/佩戴耳饰 耳饰上身_1868368860264153090.json, 平台全量/模特 局部重绘 全方位互换4K直出 多图编辑+高清修复_2059079195296354306.json, 平台全量/电商换装换脸换头 模特换衣换装 万物迁移-添加物品 局部重绘 4K直出 多图编辑+高清修复_2054724427526492161.json, 平台全量/电商首饰 耳环佩戴+指定模特 局部重绘 佩戴耳饰+耳饰上身_2058754812338073602.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/26.04最佳换装工作流_klein局部换装_bole_2046967301148250113.json、图片生成/图生图/F.2klein换装工作流局部换装_2057786570861793281.json、图片生成/图生图/Flux2-klein-万物迁移-添加物品-局部重绘_2038900975137726465.json、图片生成/图生图/Flux2-klein-小批量万物迁移（零偏移）_2015214215778275330.json、图片生成/图生图/Flux2-klein-小批量最强万物迁移生图工作流_2053011716950249474.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BlockifyMask`
- `Bool`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageScale`
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
- `ImpactMakeAnyList` —— 19/21 个有
- `Text Multiline` —— 19/21 个有
- `easy compare` —— 19/21 个有
- `easy imageSizeBySide` —— 19/21 个有
- `easy int` —— 19/21 个有
- `Fast Groups Bypasser (rgthree)` —— 14/21 个有
- `CR Text` —— 8/21 个有
- `ConditioningRebalanceKrea2` —— 2/21 个有
- `ImageConcatMulti` —— 2/21 个有
- `LayerMask: MaskPreview` —— 2/21 个有
- `LoraLoaderModelOnly` —— 2/21 个有
- `Preview from image [Crystools]` —— 2/21 个有
- `YuanColorMatch` —— 2/21 个有
- `孤海注释` —— 2/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
