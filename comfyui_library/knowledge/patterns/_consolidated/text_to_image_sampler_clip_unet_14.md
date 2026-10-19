---
name: text_to_image_sampler_clip_unet_14
type: Text To Image
frequency: 5
level: moderate
coverage: 0.924
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/API-z-image_2100574150950739970.json, 图片生成/文生图/Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json, 图片生成/文生图/Qwen2.1文生图（写实风格）_2104831851583066113.json, 图片生成/文生图/Z_image文生图-宫崎骏风格｜吉卜力风格｜卡通动漫｜二次元｜_2088507302923034626.json, 图片生成/文生图/krea2-turbo-极简极速文生图小说用_2103827094890434561.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/API-z-image_2100574150950739970.json、图片生成/文生图/Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json、图片生成/文生图/Qwen2.1文生图（写实风格）_2104831851583066113.json、图片生成/文生图/Z_image文生图-宫崎骏风格｜吉卜力风格｜卡通动漫｜二次元｜_2088507302923034626.json、图片生成/文生图/krea2-turbo-极简极速文生图小说用_2103827094890434561.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `PreviewImage` —— 3/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `SaveImageAdvanced` —— 1/5 个有
- `Text _O` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 14 | 5 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1200 | 760 - 2416 | 5 | 58% |
| 高度 | 1280 | 1080 - 1920 | 5 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 14，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1200，观测区间 760 - 2416，5 个样本
- 高度 中位数 1280，观测区间 1080 - 1920，5 个样本
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
