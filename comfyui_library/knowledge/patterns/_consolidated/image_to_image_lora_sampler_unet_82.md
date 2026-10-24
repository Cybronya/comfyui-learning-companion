---
name: image_to_image_lora_sampler_unet_82
type: Image To Image
frequency: 8
level: moderate
coverage: 0.8405
common_nodes: [Anything Everywhere, CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万物手办简单玩法_1971909657885339650.json, 图片生成/图生图/产品去标贴_1971522569771892738.json, 图片生成/图生图/修图师必备一键去瑕疵_2018971979549777922.json, 图片生成/图生图/修图师早点下班_2001217985199173634.json, 图片生成/图生图/修图师精修专用_2000844949270786050.json, 图片生成/图生图/千问超级版（去水印抹除物体、添加模特，一致性人物，更改服装，）_1959594362835513345.json, 图片生成/图生图/物品人物生成手办动漫摆放电脑前万物手办简单玩法_2068932630082576385.json, 图片生成/图生图/融图原版（产品标贴会变）_2034564115947069442.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_82

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/万物手办简单玩法_1971909657885339650.json、图片生成/图生图/产品去标贴_1971522569771892738.json、图片生成/图生图/修图师必备一键去瑕疵_2018971979549777922.json、图片生成/图生图/修图师早点下班_2001217985199173634.json、图片生成/图生图/修图师精修专用_2000844949270786050.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 5/8 个有
- `SeedVR2` —— 5/8 个有
- `SeedVR2BlockSwap` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `RH_Translator` —— 3/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | 8 - 25 | 8 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 8 | 33% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12.5，观测区间 8 - 25，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
