---
name: image_to_image_upscale_sampler_vae
type: Image To Image
frequency: 3
level: strong
coverage: 0.875667
common_nodes: [Any Switch (rgthree), CFGNorm, CR Prompt List, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, JWInteger, KSampler, LoadImage, ModelSamplingAuraFlow, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, WujiCleaner, WujiSampler, WujiUpscaler]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026667723161346050.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026684338699509762.json, 图片生成/文生图/专为SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026943803659132929.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_vae

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026667723161346050.json、图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026684338699509762.json、图片生成/文生图/专为SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026943803659132929.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CR Prompt List`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `JWInteger`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `WujiCleaner`
- `WujiSampler`
- `WujiUpscaler`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `WujiEditor` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `CR LoRA Stack` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `VAELoader` —— 1/3 个有
- `WujiQwenEditor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
