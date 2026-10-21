---
name: text_to_image_sampler_clip_unet_97
type: Text To Image
frequency: 4
level: moderate
coverage: 0.8355
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM, easy imageConcat]
members: [图片生成/文生图/1955802388865191937.json, 图片生成/文生图/1975922379924877314.json, 图片生成/文生图/失败作图工作流_2077959412047765506.json, 图片生成/文生图/海报添加logo（qwen-image）_1998716673144279042.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_97

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1955802388865191937.json、图片生成/文生图/1975922379924877314.json、图片生成/文生图/失败作图工作流_2077959412047765506.json、图片生成/文生图/海报添加logo（qwen-image）_1998716673144279042.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `JanusImageUnderstanding` —— 2/4 个有
- `JanusModelLoader` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Image Overlay` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `OffsetMask` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 768 - 1920 | 4 | 58% |
| 高度 | 1052 | 1024 - 1536 | 4 | 82% |
| 采样步数 | 30 | 9 - 35 | 4 | 59% |
| Prompt 约束强度(CFG) | 3.25 | 1 - 4 | 4 | 57% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 768 - 1920，4 个样本
- 高度 中位数 1052，观测区间 1024 - 1536，4 个样本，取值集中（一致性 82%）
- 采样步数 中位数 30，观测区间 9 - 35，4 个样本
- Prompt 约束强度(CFG) 中位数 3.25，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、easy imageConcat
