---
name: text_to_image_lora_sampler_clip_236
type: Text To Image
frequency: 5
level: weak
coverage: 0.9236
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/xingtong_base_v2_2061416410592669697.json, 图片生成/文生图/剑来-大骊娘娘_2004711609975144450.json, 图片生成/文生图/燕如嫣-凡人_2004712644147904514.json, 图片生成/文生图/贞贞lora多重z-image版本对比_2018006131871846401.json, 图片生成/文生图/（贞贞-小情绪版）Z-Image 文生图V1_2001331257915080706.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_236

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/xingtong_base_v2_2061416410592669697.json、图片生成/文生图/剑来-大骊娘娘_2004711609975144450.json、图片生成/文生图/燕如嫣-凡人_2004712644147904514.json、图片生成/文生图/贞贞lora多重z-image版本对比_2018006131871846401.json、图片生成/文生图/（贞贞-小情绪版）Z-Image 文生图V1_2001331257915080706.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 928 - 1920 | 5 | 69% |
| 高度 | 1664 | 1080 - 1920 | 5 | 81% |
| 采样步数 | 10 | 8 - 50 | 5 | 12% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 928 - 1920，5 个样本
- 高度 中位数 1664，观测区间 1080 - 1920，5 个样本，取值集中（一致性 81%）
- 采样步数 中位数 10，观测区间 8 - 50，5 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
