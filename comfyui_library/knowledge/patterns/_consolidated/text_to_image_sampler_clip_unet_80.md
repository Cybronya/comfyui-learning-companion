---
name: text_to_image_sampler_clip_unet_80
type: Text To Image
frequency: 8
level: moderate
coverage: 0.858625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image文生图+FlashVSR超清放大-简单直观方便新手研究学习_1996121050985512961.json, 图片生成/文生图/z-image文生图_2094325413752426498.json, 图片生成/文生图/【老金驿站】Anima二次元专属出图工作流_2019258717857914882.json, 图片生成/文生图/东方阳台美女Qwen2512文生图真实人像质感御姐美女_2041499716185231362.json, 图片生成/文生图/俯视户外Qwen2512文生图真实人像质感御姐美女_2041474355028303873.json, 图片生成/文生图/千问大模型文生图工作流_1959919853350105089.json, 图片生成/文生图/原神风格文生图场景设计_2100396348150472705.json, 图片生成/文生图/绝区零风格文生图场景设计_2100441031195062274.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/z-image文生图+FlashVSR超清放大-简单直观方便新手研究学习_1996121050985512961.json、图片生成/文生图/z-image文生图_2094325413752426498.json、图片生成/文生图/【老金驿站】Anima二次元专属出图工作流_2019258717857914882.json、图片生成/文生图/东方阳台美女Qwen2512文生图真实人像质感御姐美女_2041499716185231362.json、图片生成/文生图/俯视户外Qwen2512文生图真实人像质感御姐美女_2041474355028303873.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `CR Text` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `UpscaleModelLoader` —— 2/8 个有
- `FlashVSRNode` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 768 - 1920 | 8 | 67% |
| 高度 | 1116 | 768 - 1960 | 8 | 67% |
| 采样步数 | 17 | 8 - 35 | 8 | 43% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 8 | 40% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 768 - 1920，8 个样本
- 高度 中位数 1116，观测区间 768 - 1960，8 个样本
- 采样步数 中位数 17，观测区间 8 - 35，8 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，8 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
