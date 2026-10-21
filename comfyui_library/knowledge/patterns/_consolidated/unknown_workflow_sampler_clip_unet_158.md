---
name: unknown_workflow_sampler_clip_unet_158
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.93225
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, PreviewAny, SaveImage, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Rebalance超强写实质感出图_1990940694510514177.json, 图片生成/文生图/一次生成三种模型的海报_1998634326935920641.json, 图片生成/文生图/万能懒人海报设计_2077383233066590209.json, 图片生成/文生图/初芒-_2013994857626345474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_158

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Rebalance超强写实质感出图_1990940694510514177.json、图片生成/文生图/一次生成三种模型的海报_1998634326935920641.json、图片生成/文生图/万能懒人海报设计_2077383233066590209.json、图片生成/文生图/初芒-_2013994857626345474.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `PreviewAny`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Image Batch` —— 1/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
