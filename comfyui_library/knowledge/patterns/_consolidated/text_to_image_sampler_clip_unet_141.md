---
name: text_to_image_sampler_clip_unet_141
type: Text To Image
frequency: 4
level: strong
coverage: 0.87225
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImpactSwitch, Int, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN3反推提示词+Z-image生图_仿图_洗图_2002384500183166978.json, 图片生成/文生图/AI知识分享宝库丨Z-image文生图（优化出图比例）_1993874811084619777.json, 图片生成/文生图/Z-IMAGE 文生图_2020752365468520449.json, 图片生成/文生图/Z-image 基础文生图 V1（优化出图比例）_2003120005589999618.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_141

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QWEN3反推提示词+Z-image生图_仿图_洗图_2002384500183166978.json、图片生成/文生图/AI知识分享宝库丨Z-image文生图（优化出图比例）_1993874811084619777.json、图片生成/文生图/Z-IMAGE 文生图_2020752365468520449.json、图片生成/文生图/Z-image 基础文生图 V1（优化出图比例）_2003120005589999618.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `easy positive` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `Display Any (rgthree)` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1920 | 1152 - 1920 | 4 | 81% |
| 高度 | 1080 | 1080 - 1536 | 4 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1152 - 1920，4 个样本，取值集中（一致性 81%）
- 高度 中位数 1080，观测区间 1080 - 1536，4 个样本，取值集中（一致性 83%）
