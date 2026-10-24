---
name: text_to_image_sampler_clip_unet_162
type: Text To Image
frequency: 4
level: moderate
coverage: 0.76925
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/boogu_base_文生图-支持复杂提示词(可自动扩写)_2069358557987954689.json, 图片生成/文生图/boogu_turbo_快速出图，支持复杂提示词（可自动扩写）​_2069356414316924929.json, 图片生成/文生图/文生图_2028064937913880578.json, 图片生成/文生图/文生图。Zimage（支持真人的国产加速模型）_2028059294964387841.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_162

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/boogu_base_文生图-支持复杂提示词(可自动扩写)_2069358557987954689.json、图片生成/文生图/boogu_turbo_快速出图，支持复杂提示词（可自动扩写）​_2069356414316924929.json、图片生成/文生图/文生图_2028064937913880578.json、图片生成/文生图/文生图。Zimage（支持真人的国产加速模型）_2028059294964387841.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactConditionalBranch` —— 2/4 个有
- `PDRatioSelector` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `easy showAnything` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | 936 - 1920 | 4 | 70% |
| 高度 | 1024 | 720 - 1280 | 4 | 80% |
| 采样步数 | 35 | 4 - 40 | 4 | 50% |
| Prompt 约束强度(CFG) | 4.75 | 1 - 5.5 | 4 | 54% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1152，观测区间 936 - 1920，4 个样本
- 高度 中位数 1024，观测区间 720 - 1280，4 个样本，取值集中（一致性 80%）
- 采样步数 中位数 35，观测区间 4 - 40，4 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 4.75，观测区间 1 - 5.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
