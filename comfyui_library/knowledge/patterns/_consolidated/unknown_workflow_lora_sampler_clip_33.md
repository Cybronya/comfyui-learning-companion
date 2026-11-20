---
name: unknown_workflow_lora_sampler_clip_33
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.76275
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageScaleDownToSize]
problems: []
missing: []
members: [图片生成/图生图/产品精修_2095771710493650945.json, 平台全量/F2-klein-9B产品人物换背景 万物溶图 光影融合 重新打光_2029429236431331329.json, 平台全量/Flux-2-klein-9B 万物迁移 优化版  人物模特_电商产品 一致性风格换迁移_2029031269878730753.json, 平台全量/Flux-2-klein-9B 换背景 人物模特_电商产品换场景  一致性风格换场景 高清放大_2029010409109331969.json, 平台全量/Flux-2-klein-9B 胸部放大 美女模特身材优化_2029068702238384130.json, 平台全量/Flux2+Klein 消除水印 移除文字+SeedVR2高清放大_2029763798713769985.json, 平台全量/一键提取人物衣服-One click extraction of character clothin_2031573125279780865.json, 平台全量/一键金属、电器、化妆品精修 产品精修SeedVR2+放大+FLUX2-Klein-9B产品精修极速版_2031179171875000322.json, 平台全量/万物提取服装展示 Seedream 5服饰提取 Flux-2-klein-9B  平铺展示服装_2032376983081984002.json, 平台全量/产品精修SeedVR2 放大一键金属 电器 化妆品精修 FLUX2-Klein-9B产品精修升级版_2030880230444896257.json, 平台全量/服饰提取 Flux-2-klein-9B 万物提取服装 平铺展示服装 精修产品_2029061796664971266.json, 平台全量/海报移除文字 去除产品 保留背景+万能移除 高清放大_2072886277074145282.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/产品精修_2095771710493650945.json、平台全量/F2-klein-9B产品人物换背景 万物溶图 光影融合 重新打光_2029429236431331329.json、平台全量/Flux-2-klein-9B 万物迁移 优化版  人物模特_电商产品 一致性风格换迁移_2029031269878730753.json、平台全量/Flux-2-klein-9B 换背景 人物模特_电商产品换场景  一致性风格换场景 高清放大_2029010409109331969.json、平台全量/Flux-2-klein-9B 胸部放大 美女模特身材优化_2029068702238384130.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 10/12 个有
- `SeedVR2LoadDiTModel` —— 9/12 个有
- `SeedVR2LoadVAEModel` —— 9/12 个有
- `SeedVR2VideoUpscaler` —— 9/12 个有
- `JWInteger` —— 7/12 个有
- `Fast Groups Bypasser (rgthree)` —— 6/12 个有
- `GrowMask` —— 1/12 个有
- `ImageUpscaleWithModel` —— 1/12 个有
- `InvertMask` —— 1/12 个有
- `JoinImageWithAlpha` —— 1/12 个有
- `LayerMask: BiRefNetUltraV2` —— 1/12 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `RH_Jimeng4_Image2Image` —— 1/12 个有
- `Upscale Model Loader` —— 1/12 个有
- `YUAN_TXTConvertAny` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
