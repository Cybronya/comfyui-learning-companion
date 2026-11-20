---
name: text_to_image_upscale_latent_upscale_lora_12
type: Text To Image
frequency: 3
level: weak
coverage: 0.845
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScale, ImageUpscaleWithModel, KSampler, LatentUpscaleBy, LoadImage, Power Lora Loader (rgthree), PreviewImage, PrimitiveStringMultiline, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/游戏场景01_2100549378082697217.json, 图片生成/文生图/游戏场景01_2100180693333659649.json, 图片生成/文生图/游戏场景01文生图打底｜场景概念图批量生成，游戏美术素材库起步首选_2100481657882107905.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/游戏场景01_2100549378082697217.json、图片生成/文生图/游戏场景01_2100180693333659649.json、图片生成/文生图/游戏场景01文生图打底｜场景概念图批量生成，游戏美术素材库起步首选_2100481657882107905.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentUpscaleBy`
- `LoadImage`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 3 | 38% |
| 宽度 | 1536 | 80 - 1536 | 3 | 35% |
| 高度 | 768 | 80 - 768 | 3 | 40% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，3 个样本，取值分散，一致性仅 38%
- 宽度 中位数 1536，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 35%
- 高度 中位数 768，观测区间 80 - 768，3 个样本，取值分散，一致性仅 40%
- 高发问题（10/3 个样本）：Steps较低可能导致细节不足
