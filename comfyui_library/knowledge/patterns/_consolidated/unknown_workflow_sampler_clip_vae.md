---
name: unknown_workflow_sampler_clip_vae
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.885708
common_nodes: [CFGGuider, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/1.人物换装_2050619333541412866.json, 图片生成/图生图/20260722一致性personal_2079764596788912130.json, 图片生成/图生图/9.批量精修白底图_2050773369066401794.json, 图片生成/图生图/F.2Klein9B万物迁移_2066737707379945473.json, 图片生成/图生图/FLUX-Klein-图像编辑-10秒急速出图_2012126304631529473.json, 图片生成/图生图/FLUX.Klein-9B一致性lora单图编辑_2033155455794548737.json, 图片生成/图生图/Flux-2-Klein-9b 万物迁移_2065056521217728513.json, 图片生成/图生图/Flux2 Klein 双重增强现实_2067152624360706049.json, 图片生成/图生图/Flux2 Klein 增强现实LoRA_2020393021082181633.json, 图片生成/图生图/Flux2 Klein 增强现实LoRA_2033162072971812866.json, 图片生成/图生图/Flux2 Klein 增强现实（超还原cosplay)_2026115898070798337.json, 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 加强了一致性 林耀3.6_2029755418074947585.json, 图片生成/图生图/Klein - 万物迁移_2051859267984084993.json, 图片生成/图生图/Klein - 万物迁移_2065714934046089217.json, 图片生成/图生图/Klein - 万物迁移光影_2065342945917755393.json, 图片生成/图生图/Klein_-_万物迁移重新打光_2082641469969616898.json, 图片生成/图生图/Klein_-_万物迁移重新打光_2082650177730600962.json, 图片生成/图生图/万物迁移-Flux-2Klein-9b_2064567178598371329.json, 图片生成/图生图/光影迁移-打光色调复刻_kelin打光工作流_2068244841733115905.json, 图片生成/图生图/图片换背景工作流+全节点注释_2086268740781559809.json, 图片生成/图生图/真人感换装_2105190551246172161.json, 图片生成/图生图/素描手绘风格迁移-Flux2 Klien_2065681291726643202.json, 图片生成/图生图/风格迁移-精准画风还原_Flux2 Klien_2066710064941060097.json, 图片生成/文生图/Klein - 万物迁移自用_2064658422053818370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/1.人物换装_2050619333541412866.json、图片生成/图生图/20260722一致性personal_2079764596788912130.json、图片生成/图生图/9.批量精修白底图_2050773369066401794.json、图片生成/图生图/F.2Klein9B万物迁移_2066737707379945473.json、图片生成/图生图/FLUX-Klein-图像编辑-10秒急速出图_2012126304631529473.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 24 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 23/24 个有
- `ConditioningZeroOut` —— 23/24 个有
- `GetImageSize` —— 23/24 个有
- `ImageScaleToTotalPixels` —— 23/24 个有
- `LoadImage` —— 23/24 个有
- `LoraLoaderModelOnly` —— 23/24 个有
- `UNETLoader` —— 23/24 个有
- `CR Text` —— 22/24 个有
- `LayerUtility: ImageReel` —— 22/24 个有
- `LayerUtility: ImageReelComposit` —— 22/24 个有
- `PreviewImage` —— 22/24 个有
- `Image Comparer (rgthree)` —— 19/24 个有
- `ImageStitch` —— 15/24 个有
- `PrimitiveFloat` —— 14/24 个有
- `ImageScaleToMaxDimension` —— 2/24 个有
- `AILab_QwenVL` —— 1/24 个有
- `CR Text Concatenate` —— 1/24 个有
- `ClothesSegment` —— 1/24 个有
- `ColorMatchToReference` —— 1/24 个有
- `CustomAddLabel` —— 1/24 个有
- `HAIGC_LoadImagesFromZip` —— 1/24 个有
- `ImageCompositeMasked` —— 1/24 个有
- `JWFloat` —— 1/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/24 个有
- `LoadDiffusionModelShared //Inspire` —— 1/24 个有
- `LoadTextEncoderShared //Inspire` —— 1/24 个有
- `ShowText|pysssss` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
