---
name: image_to_image_upscale_sampler_vae
type: Image To Image
frequency: 12
level: strong
coverage: 0.882333
common_nodes: [Any Switch (rgthree), CFGNorm, CR Prompt List, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, JWInteger, KSampler, LoadImage, ModelSamplingAuraFlow, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, WujiCleaner, WujiSampler, WujiUpscaler]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SeeDance Qwen-image2511_2027190717482803202.json, 图片生成/图生图/剧漫剧专用资产生成 自用_2038987198648815617.json, 图片生成/文生图/2029394586908499969.json, 图片生成/文生图/SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028398044986744834.json, 图片生成/文生图/SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028468060918652929.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库-邻家AI大女孩_2042477388948312065.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026667723161346050.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026684338699509762.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2036617927289479170.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产道具库_2045773382909693954.json, 图片生成/文生图/专为SeeDance 2.0AI短剧漫剧专用超真实感资产道具库Qwen-image2511_2026943803659132929.json, 图片生成/文生图/资产道具场景库_2042384861738049537.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_vae

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/SeeDance Qwen-image2511_2027190717482803202.json、图片生成/图生图/剧漫剧专用资产生成 自用_2038987198648815617.json、图片生成/文生图/2029394586908499969.json、图片生成/文生图/SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028398044986744834.json、图片生成/文生图/SeeDance 2.0 AI 短剧 漫剧 专用 超真实感 资产道具库Qwen-image2511_2028468060918652929.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
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
- `WujiEditor` —— 10/12 个有
- `CheckpointLoaderSimple` —— 7/12 个有
- `CLIPLoader` —— 5/12 个有
- `CR LoRA Stack` —— 5/12 个有
- `LoraLoaderModelOnly` —— 5/12 个有
- `UNETLoader` —— 5/12 个有
- `VAELoader` —— 5/12 个有
- `WujiQwenEditor` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
