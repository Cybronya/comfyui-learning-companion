---
name: unknown_workflow_sampler_clip_unet_18
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.945893
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2Klein-4B 一致性人物替换加速版_2015600860935491586.json, 图片生成/图生图/Flux2Klein-4B 人物一致性换装_2043595835887329282.json, 图片生成/图生图/Flux2Klein-换内衣-9B版_2013862581559107585.json, 图片生成/图生图/Flux2Klein-换内衣_2084936137038188546.json, 图片生成/图生图/Flux2Klein-换装_2015725097327267841.json, 图片生成/图生图/Flux2Klein-换装工作流-高级版_1938439504737034241.json, 图片生成/图生图/Flux2Klein9B动漫转写实真人_2061651201707569153.json, 图片生成/图生图/Flux2Klein9b万物迁移_2065953597262749698.json, 图片生成/图生图/Flux2Klein人物换脸+多图编辑_2018928471556235265.json, 图片生成/图生图/Flux2Klein人物换脸高清快速版_2047599085003218946.json, 图片生成/图生图/Flux2Klein动漫转写实真人+细节增强_2063438140592975874.json, 图片生成/图生图/Flux2Klein动漫转真实+细节增强_2060937329581318146.json, 图片生成/图生图/Flux2Klein图像编辑9B版官方版（加速版）_2012060623399559170.json, 图片生成/图生图/Flux2Klein图像编辑终极版角色一致性_2060283231865495553.json, 图片生成/图生图/Flux2Klein图像编辑终极版角色一致性_2062072605993168898.json, 图片生成/图生图/Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2012067711764926466.json, 图片生成/图生图/Flux2Klein多图编辑4B加速版本_2012148311343501314.json, 图片生成/图生图/Flux2Klein细节增强真实皮肤质感_2064503315794321409.json, 图片生成/图生图/Flux2_Klein_9B印花提取_2104442102175322114.json, 图片生成/图生图/Flux2_Klein_9B高清放大Lora方法_2027577843588276226.json, 图片生成/图生图/Klein-一致性_2028302502973677570.json, 图片生成/图生图/Klein9b产品渲染精修_2048198461790621698.json, 图片生成/图生图/Klein一致性加强_2030832629217497090.json, 图片生成/图生图/Klein人物一致性发型衣服换脸一致性增强换衣服换发色换脸_2029595679181508609.json, 图片生成/图生图/SQ-效果图优化工作流_2112780528683409410.json, 图片生成/图生图/klein-9b面部一致性增强与东方审美lora_2035090544275234817.json, 图片生成/图生图/klein克莱因转赛璐珞_2018983559482052610.json, 图片生成/文生图/Klein-一致性_2096434383749210114.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Flux2Klein-4B 一致性人物替换加速版_2015600860935491586.json、图片生成/图生图/Flux2Klein-4B 人物一致性换装_2043595835887329282.json、图片生成/图生图/Flux2Klein-换内衣-9B版_2013862581559107585.json、图片生成/图生图/Flux2Klein-换内衣_2084936137038188546.json、图片生成/图生图/Flux2Klein-换装_2015725097327267841.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 28 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 27/28 个有
- `ImageScaleToTotalPixels` —— 24/28 个有
- `CR Text` —— 23/28 个有
- `EmptyFlux2LatentImage` —— 23/28 个有
- `GetImageSize` —— 18/28 个有
- `LoraLoaderModelOnly` —— 15/28 个有
- `PreviewImage` —— 13/28 个有
- `Image Comparer (rgthree)` —— 12/28 个有
- `JWFloat` —— 11/28 个有
- `ImageConcanate` —— 9/28 个有
- `LayerUtility: ImageReel` —— 8/28 个有
- `LayerUtility: ImageReelComposit` —— 8/28 个有
- `easy imageSize` —— 6/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/28 个有
- `IdentityFeatureTransferV3` —— 2/28 个有
- `Int` —— 2/28 个有
- `BetterFilmGrain` —— 1/28 个有
- `HAIGC_SavePSD` —— 1/28 个有
- `ImageApplyLUT+` —— 1/28 个有
- `ImageSharpen` —— 1/28 个有
- `PathchSageAttentionKJ` —— 1/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
