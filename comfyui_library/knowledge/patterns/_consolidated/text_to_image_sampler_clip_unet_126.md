---
name: text_to_image_sampler_clip_unet_126
type: Text To Image
frequency: 6
level: moderate
coverage: 0.9605
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima_api_2075524651396198402.json, 图片生成/文生图/anima_preview2 二次元动漫角色自由~ & RTX Video 超分放大~_2036407166378184705.json, 图片生成/文生图/krea2 文生图 无LORA_2111016861499486209.json, 图片生成/文生图/krea2的极致美学_2069777686637142018.json, 图片生成/文生图/miaomiao RealSkin Anima 1.0 文生图_2114597001806569473.json, 图片生成/文生图/z-image文生图+FlashVSR超清放大-简单直观方便新手研究学习_1996121050985512961.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_126

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/anima_api_2075524651396198402.json、图片生成/文生图/anima_preview2 二次元动漫角色自由~ & RTX Video 超分放大~_2036407166378184705.json、图片生成/文生图/krea2 文生图 无LORA_2111016861499486209.json、图片生成/文生图/krea2的极致美学_2069777686637142018.json、图片生成/文生图/miaomiao RealSkin Anima 1.0 文生图_2114597001806569473.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `FlashVSRNode` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `SeedNode` —— 1/6 个有
- `TT_img_enc` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 6 | 46% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 6 | 36% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1052 | 720 - 1920 | 6 | 68% |
| 高度 | 1280 | 1024 - 1920 | 6 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，6 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 720 - 1920，6 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，6 个样本
