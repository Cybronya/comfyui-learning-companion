---
name: text_to_image_lora_sampler_clip_493
type: Text To Image
frequency: 4
level: moderate
coverage: 0.85325
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, Label (rgthree), LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-二次元-4k艺术壁纸_2115997071386963969.json, 图片生成/文生图/Krea2-二次元-4k艺术壁纸_2116343120651706370.json, 图片生成/文生图/Krea2-二次元-4k艺术壁纸_2116695612308676610.json, 图片生成/文生图/Krea2-云上天宫_2095745487965081602.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_493

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2-二次元-4k艺术壁纸_2115997071386963969.json、图片生成/文生图/Krea2-二次元-4k艺术壁纸_2116343120651706370.json、图片生成/文生图/Krea2-二次元-4k艺术壁纸_2116695612308676610.json、图片生成/文生图/Krea2-云上天宫_2095745487965081602.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 3/4 个有
- `ImageScale` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `LatentUpscaleBy` —— 3/4 个有
- `StringConcatenate` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1536 - 2560 | 4 | 75% |
| 高度 | 864 | 864 - 1880 | 4 | 61% |
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 1 | 4 | 45% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1536，观测区间 1536 - 2560，4 个样本
- 高度 中位数 864，观测区间 864 - 1880，4 个样本
- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 1，4 个样本，取值分散，一致性仅 45%
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
