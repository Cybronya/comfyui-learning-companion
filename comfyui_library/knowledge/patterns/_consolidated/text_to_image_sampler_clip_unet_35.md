---
name: text_to_image_sampler_clip_unet_35
type: Text To Image
frequency: 14
level: weak
coverage: 0.955357
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI牛马文生图写实风_2038437485671358466.json, 图片生成/文生图/AI牛马文生图（全）_2038456795647188993.json, 图片生成/文生图/AI牛马文生图（全）_2038813773825314818.json, 图片生成/文生图/API-z-image-my_2046050393880272898.json, 图片生成/文生图/API-z-image_2066009097937448961.json, 图片生成/文生图/API-z-image_2066893780837560322.json, 图片生成/文生图/API-z-image_2085310412328886273.json, 图片生成/文生图/API-z-image_2100574150950739970.json, 图片生成/文生图/Anima DMDX 四步极速版_2060754845304446978.json, 图片生成/文生图/Anima HiresFix 1.5倍精修_2060759010810355714.json, 图片生成/文生图/Anima base v1 动漫生图_2059172782583410690.json, 图片生成/文生图/Anima base v1 动漫生图_2093989338236407810.json, 图片生成/文生图/Qwen_Image基础加速工作流_1973965175168569346.json, 图片生成/文生图/Qwen_image_文生图_1977747366285561858.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_35

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/AI牛马文生图写实风_2038437485671358466.json、图片生成/文生图/AI牛马文生图（全）_2038456795647188993.json、图片生成/文生图/AI牛马文生图（全）_2038813773825314818.json、图片生成/文生图/API-z-image-my_2046050393880272898.json、图片生成/文生图/API-z-image_2066009097937448961.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 9/14 个有
- `ConditioningZeroOut` —— 7/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `Int` —— 6/14 个有
- `Text _O` —— 5/14 个有
- `AddLabel` —— 2/14 个有
- `PrimitiveInt` —— 2/14 个有
- `Anything Everywhere3` —— 1/14 个有
- `CR Latent Batch Size` —— 1/14 个有
- `LatentUpscale` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `QwenEditResolution` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 896 - 2416 | 14 | 62% |
| 高度 | 1080 | 1024 - 1720 | 14 | 85% |
| 采样步数 | 14 | 4 - 30 | 14 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 14 | 25% |
| 采样算法 | euler | - | 14 | 64% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 0.35 - 1 | 14 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 896 - 2416，14 个样本
- 高度 中位数 1080，观测区间 1024 - 1720，14 个样本，取值集中（一致性 85%）
- 采样步数 中位数 14，观测区间 4 - 30，14 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，14 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，14 个样本，一致性 64%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，14 个样本，取值集中（一致性 82%）
