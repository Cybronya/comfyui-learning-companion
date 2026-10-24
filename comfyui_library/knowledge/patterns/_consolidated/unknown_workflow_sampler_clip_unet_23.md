---
name: unknown_workflow_sampler_clip_unet_23
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.90076
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/家纺四件套扒花型_2031572811197714434.json, 图片生成/图生图/庭院效果图洗图-高清放大_2055964480579874817.json, 图片生成/图生图/熊熊-Flux2 Klein局部重绘+图片去水印+物品迁移_2044458513019179010.json, "图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2034815871520083969.json", "图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2037006862268239874.json", 图片生成/图生图/脸部迁移+换头_2015404568665919489.json, 图片生成/文生图/Z-image-base-邪修双采+高清放大_2016379330103873538.json, 图片生成/文生图/Z-image-base-邪修双采+高清放大_2018103457047126018.json, 图片生成/文生图/z-iamge多功能生图工作流_2050156379784138753.json, 图片生成/文生图/z-images 文生图 高质量版_2028826690939527170.json, 图片生成/文生图/万能图像生成器 - 直出4K.6K.8K图_2029090503827922945.json, 图片生成/文生图/万能图像生成器 Z-image 三阶采样 多样性超写实 文生图 万能图像生成器一键直出4K大图_2051105971912622082.json, 图片生成/文生图/万能图像生成器 一键直出4K_2040718467866828802.json, 图片生成/文生图/万能图像生成器-直出4K_2055990233665155073.json, 图片生成/文生图/万能图像生成器-邻家AI大女孩_2042230797427544066.json, 图片生成/文生图/万能图像生成器_2028113030734680066.json, 图片生成/文生图/万能图像生成器_2041868257631670273.json, 图片生成/文生图/万能图像生成器_2053646155682201602.json, 图片生成/文生图/万能图像生成器（z-image+Flux2-klein+自动化提示词）_2034136038548967425.json, 图片生成/文生图/万能文生图—阿浩_2039866907611893761.json, 图片生成/文生图/人物生成_2033068431771176961.json, 图片生成/文生图/什么都能生的万能图像生成器_2044715424964677634.json, 图片生成/文生图/动漫+短剧人物主角设计工作流_2039520925674119169.json, 图片生成/文生图/真人短剧人物主角设计工作流_2039916090708467713.json, 图片生成/文生图/🏄【Sitoyn】真人角色设计【直出单人全景+多视图】_2044291590763585537.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_23

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/家纺四件套扒花型_2031572811197714434.json、图片生成/图生图/庭院效果图洗图-高清放大_2055964480579874817.json、图片生成/图生图/熊熊-Flux2 Klein局部重绘+图片去水印+物品迁移_2044458513019179010.json、图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2034815871520083969.json、图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2037006862268239874.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 25 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 24/25 个有
- `SaveImage` —— 24/25 个有
- `SeedVR2LoadDiTModel` —— 23/25 个有
- `SeedVR2LoadVAEModel` —— 23/25 个有
- `SeedVR2VideoUpscaler` —— 23/25 个有
- `EmptyFlux2LatentImage` —— 22/25 个有
- `GetImageSize` —— 22/25 个有
- `ImageScaleToTotalPixels` —— 22/25 个有
- `LoraLoaderModelOnly` —— 22/25 个有
- `ColorMatch` —— 21/25 个有
- `ImageSharpen` —— 21/25 个有
- `EmptyLatentImage` —— 20/25 个有
- `KSamplerAdvanced` —— 19/25 个有
- `ModelSamplingAuraFlow` —— 19/25 个有
- `PreviewImage` —— 19/25 个有
- `Int` —— 18/25 个有
- `LayerUtility: PurgeVRAM V2` —— 18/25 个有
- `CR Text` —— 17/25 个有
- `INTConstant` —— 17/25 个有
- `Fast Groups Bypasser (rgthree)` —— 10/25 个有
- `Label (rgthree)` —— 10/25 个有
- `LoadImage` —— 8/25 个有
- `CLIPLoaderGGUF` —— 6/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/25 个有
- `GetNode` —— 4/25 个有
- `SetNode` —— 4/25 个有
- `ShowText|pysssss` —— 4/25 个有
- `PlaySound|pysssss` —— 3/25 个有
- `RH_LLMAPI_Pro_Node` —— 3/25 个有
- `Mute / Bypass Relay (rgthree)` —— 2/25 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/25 个有
- `MuyeLoadImage` —— 2/25 个有
- `Text` —— 2/25 个有
- `Fast Groups Muter (rgthree)` —— 1/25 个有
- `ImageResize+` —— 1/25 个有
- `ImageScaleBy` —— 1/25 个有
- `ImpactConditionalBranch` —— 1/25 个有
- `MemoryCleaner` —— 1/25 个有
- `PrimitiveBoolean` —— 1/25 个有
- `RH_LLMAPI_NODE` —— 1/25 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/25 个有
- `SaveImageJPG_GH` —— 1/25 个有
- `SmartImageConcat` —— 1/25 个有
- `TTResolutionSelector` —— 1/25 个有
- `TextInput_` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1536 | 20 | 89% |
| 高度 | 1536 | 1536 - 1536 | 20 | 100% |
| 采样步数 | randomize | - | 19 | 100% |
| Prompt 约束强度(CFG) | 3 | 1.15 - 3 | 19 | 86% |
| 采样算法 | 1 | 1 - 2 | 19 | 65% |
| 调度器 | euler | - | 19 | 95% |
| 重绘幅度 | simple | - | 19 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1536，20 个样本，取值集中（一致性 89%）
- 高度 中位数 1536，观测区间 1536 - 1536，20 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，19 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1.15 - 3，19 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 2，19 个样本
- 调度器 最常用 euler，19 个样本，一致性 95%
- 重绘幅度 最常用 simple，19 个样本，一致性 95%
