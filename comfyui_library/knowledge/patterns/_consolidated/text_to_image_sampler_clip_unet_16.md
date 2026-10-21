---
name: text_to_image_sampler_clip_unet_16
type: Text To Image
frequency: 18
level: strong
coverage: 0.869889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo基础文生图+高清放大_2063174571645296642.json, 图片生成/文生图/Z-image-turbo文生图_2063952781551169537.json, 图片生成/文生图/Z-image-中老年内衣女模特_1999303495641690114.json, 图片生成/文生图/Z-image-女内裤模特图_1998988604456194049.json, 图片生成/文生图/Z-image-电商保暖模特_1996104929171423233.json, 图片生成/文生图/Z-image-电商内衣模特图_2002330895598120962.json, 图片生成/文生图/Z-image-电商女内裤模特图_1999755593114152961.json, 图片生成/文生图/Z-image-男内裤模特_1998588053952299010.json, 图片生成/文生图/Z-image文生图批量工作流直出4K（动漫短剧资产生图抽卡专用）_2102674578551164929.json, 图片生成/文生图/Z-image电商文胸模特_1995676126175485954.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070356235764977666.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070398228675252226.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070414848839737345.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070428303873368066.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2078331213101752321.json, 图片生成/文生图/zimage（梦幻）_2053013074277355522.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2052651394800336898.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色_2057377135022661634.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo基础文生图+高清放大_2063174571645296642.json、图片生成/文生图/Z-image-turbo文生图_2063952781551169537.json、图片生成/文生图/Z-image-中老年内衣女模特_1999303495641690114.json、图片生成/文生图/Z-image-女内裤模特图_1998988604456194049.json、图片生成/文生图/Z-image-电商保暖模特_1996104929171423233.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 17/18 个有
- `SeedVR2LoadVAEModel` —— 17/18 个有
- `SeedVR2VideoUpscaler` —— 17/18 个有
- `Image Comparer (rgthree)` —— 16/18 个有
- `ConditioningZeroOut` —— 14/18 个有
- `CR Text` —— 11/18 个有
- `LoraLoaderModelOnly` —— 11/18 个有
- `PreviewImage` —— 10/18 个有
- `ImpactInt` —— 8/18 个有
- `Fast Groups Bypasser (rgthree)` —— 7/18 个有
- `String Literal` —— 7/18 个有
- `easy cleanGpuUsed` —— 7/18 个有
- `PrimitiveInt` —— 5/18 个有
- `INTConstant` —— 4/18 个有
- `ImageScaleToTotalPixels` —— 4/18 个有
- `SeedVR2TorchCompileSettings` —— 3/18 个有
- `ImpactConditionalBranch` —— 1/18 个有
- `PDRatioSelector` —— 1/18 个有
- `PreviewAny` —— 1/18 个有
- `PrimitiveBoolean` —— 1/18 个有
- `RHHiddenNodes` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 872 | 720 - 1080 | 18 | 81% |
| 高度 | 1408 | 1280 - 1920 | 18 | 83% |
| 采样步数 | 8 | 8 - 10 | 18 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 18 | 82% |
| 采样算法 | euler | - | 18 | 78% |
| 调度器 | simple | - | 18 | 39% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 872，观测区间 720 - 1080，18 个样本，取值集中（一致性 81%）
- 高度 中位数 1408，观测区间 1280 - 1920，18 个样本，取值集中（一致性 83%）
- 采样步数 中位数 8，观测区间 8 - 10，18 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，18 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，18 个样本，一致性 78%
- 调度器 最常用 simple，18 个样本，一致性 39%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（10/18 个样本）：Steps较低可能导致细节不足
