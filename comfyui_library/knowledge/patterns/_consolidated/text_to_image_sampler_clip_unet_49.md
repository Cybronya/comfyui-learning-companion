---
name: text_to_image_sampler_clip_unet_49
type: Text To Image
frequency: 12
level: moderate
coverage: 0.8915
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰008.文生图-语义理解升级_2033732546902630402.json, 图片生成/文生图/001.Z-image生图巅峰009.Z-回车批量文生图+flux-vae_2033738805638860802.json, 图片生成/文生图/2030634268841480193.json, 图片生成/文生图/AA--Zimage文生图-基础+SeedVR2放大_1998702080091152386.json, 图片生成/文生图/Z-IMAGE：小而美图像模型：文生图_2035264157662060546.json, 图片生成/文生图/Z-image-中老年内衣女模特_1999303495641690114.json, 图片生成/文生图/Z-image-女内裤模特图_1998988604456194049.json, 图片生成/文生图/Z-image-电商保暖模特_1996104929171423233.json, 图片生成/文生图/Z-image-电商内衣模特图_2002330895598120962.json, 图片生成/文生图/Z-image-电商女内裤模特图_1999755593114152961.json, 图片生成/文生图/Z-image-男内裤模特_1998588053952299010.json, 图片生成/文生图/Z-image电商文胸模特_1995676126175485954.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰008.文生图-语义理解升级_2033732546902630402.json、图片生成/文生图/001.Z-image生图巅峰009.Z-回车批量文生图+flux-vae_2033738805638860802.json、图片生成/文生图/2030634268841480193.json、图片生成/文生图/AA--Zimage文生图-基础+SeedVR2放大_1998702080091152386.json、图片生成/文生图/Z-IMAGE：小而美图像模型：文生图_2035264157662060546.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 10/12 个有
- `LoraLoaderModelOnly` —— 10/12 个有
- `SeedVR2LoadDiTModel` —— 10/12 个有
- `SeedVR2LoadVAEModel` —— 10/12 个有
- `SeedVR2VideoUpscaler` —— 10/12 个有
- `Image Comparer (rgthree)` —— 9/12 个有
- `String Literal` —— 9/12 个有
- `easy cleanGpuUsed` —— 8/12 个有
- `Fast Groups Bypasser (rgthree)` —— 7/12 个有
- `CR Prompt List` —— 3/12 个有
- `SeedVR2TorchCompileSettings` —— 3/12 个有
- `easy showAnything` —— 2/12 个有
- `INTConstant` —— 1/12 个有
- `ImageScaleBy` —— 1/12 个有
- `InversionDemoLazySwitch` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `PreviewImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1920 | 12 | 59% |
| 高度 | 1280 | 1080 - 1920 | 12 | 86% |
| 采样步数 | 10 | 8 - 12 | 12 | 91% |
| Prompt 约束强度(CFG) | 1.25 | 1 - 3 | 12 | 63% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | beta57 | - | 12 | 58% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1920，12 个样本
- 高度 中位数 1280，观测区间 1080 - 1920，12 个样本，取值集中（一致性 86%）
- 采样步数 中位数 10，观测区间 8 - 12，12 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1.25，观测区间 1 - 3，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 beta57，12 个样本，一致性 58%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
