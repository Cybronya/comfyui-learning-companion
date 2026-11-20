---
name: image_to_image_upscale_sampler_clip_9
type: Image To Image
frequency: 12
level: strong
coverage: 0.68825
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleBy, ImpactInt, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/【加密版】图片去除Ai感工作流： Z_image反推洗图重绘+SeedVR放大工作流-B站UP主@好奇漫步_2065781622254956545.json, 图片生成/图生图/【自优】图片去除Ai感工作流_2114227657826197505.json, 图片生成/图生图/去AI感加细节_2044079478636290050.json, 图片生成/图生图/去ai感反推洗图重绘+SeedVR放大对比工作流_2032824879841550337.json, 图片生成/图生图/去除AI感洗图工作流（ZImage+高清放大)_2050404907630514177.json, 图片生成/图生图/去除Ai感还原真实照片图像人像_2064711799517306881.json, 图片生成/图生图/去除Ai感高清流_2059640138900271105.json, 图片生成/图生图/图像去除Ai感肤色真实感极佳_2063521747957272578.json, 图片生成/图生图/图像去除Ai感，肤色真实感极佳_2058561035572961282.json, 图片生成/图生图/图像去除Ai感，肤色真实感极佳_2059092954777735170.json, 图片生成/图生图/图片image去除Ai感肤色真实感极佳_2064506351417651202.json, 图片生成/图生图/图片去除Ai感工作流： Z_image反推洗图重绘+SeedVR放大对比工作流-B站UP主@好奇漫步_1995894229622800386.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/【加密版】图片去除Ai感工作流： Z_image反推洗图重绘+SeedVR放大工作流-B站UP主@好奇漫步_2065781622254956545.json、图片生成/图生图/【自优】图片去除Ai感工作流_2114227657826197505.json、图片生成/图生图/去AI感加细节_2044079478636290050.json、图片生成/图生图/去ai感反推洗图重绘+SeedVR放大对比工作流_2032824879841550337.json、图片生成/图生图/去除AI感洗图工作流（ZImage+高清放大)_2050404907630514177.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleBy`
- `ImpactInt`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 11/12 个有
- `LayerUtility: ImageReelComposit` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `ShowText|pysssss` —— 11/12 个有
- `Fast Groups Bypasser (rgthree)` —— 7/12 个有
- `Image Comparer (rgthree)` —— 7/12 个有
- `easy imageConcat` —— 6/12 个有
- `GetNode` —— 5/12 个有
- `SetNode` —— 5/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `SomethingToString` —— 2/12 个有
- `TT_img_enc` —— 2/12 个有
- `easy convertAnything` —— 2/12 个有
- `easy indexAnything` —— 2/12 个有
- `FancyTimerNode` —— 1/12 个有
- `HAIGC_SaveImagesToZip` —— 1/12 个有
- `JWFloat` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 0.7 | 0.3 - 0.95 | 12 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.3 - 0.95，12 个样本
