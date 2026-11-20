---
name: text_to_image_sampler_clip_unet_95
type: Text To Image
frequency: 7
level: moderate
coverage: 0.886429
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Dark daze art（Z-image-dazz）_1998590663778271234.json, 图片生成/图生图/Z-image高清细节DejpegV2_1998260405262778370.json, 图片生成/文生图/Qwen千问 _ 文生图_1953804613029908482.json, 图片生成/文生图/VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881.json, 图片生成/文生图/Z-image-turbo 极速文生图_1993943881752444930.json, 图片生成/文生图/Z-image文生图，二次元校园女生风格Lora_1998998879238508546.json, 图片生成/文生图/文生图（Z-image，带lora）_1998357719558029314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_95

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Dark daze art（Z-image-dazz）_1998590663778271234.json、图片生成/图生图/Z-image高清细节DejpegV2_1998260405262778370.json、图片生成/文生图/Qwen千问 _ 文生图_1953804613029908482.json、图片生成/文生图/VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881.json、图片生成/文生图/Z-image-turbo 极速文生图_1993943881752444930.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `Anything Everywhere3` —— 3/7 个有
- `LayerUtility: TextJoinV2` —— 3/7 个有
- `easy promptList` —— 3/7 个有
- `ModelSamplingAuraFlow` —— 2/7 个有
- `MuyeSizeSelector` —— 2/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 7 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 27% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1080 | 720 - 1536 | 7 | 75% |
| 高度 | 1920 | 1280 - 2048 | 7 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1536，7 个样本
- 高度 中位数 1920，观测区间 1280 - 2048，7 个样本，取值集中（一致性 82%）
