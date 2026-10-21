---
name: unknown_workflow_sampler_clip_unet_149
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.59725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ImpactSwitch, JjkText, KSampler, LimitNumber, LoadImage, PrimitiveInt, RH_LLMAPI_NODE, SaveImage, TextCombinerSix, TextCombinerTwo, UNETLoader, VAEDecode, VAELoader, easy seed, easy showAnything]
problems: []
missing: [easy seed, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1958709959401881601.json, 图片生成/文生图/1970924112187138049.json, 图片生成/文生图/1970937254313107458.json, 图片生成/文生图/1970950894877609986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_149

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1958709959401881601.json、图片生成/文生图/1970924112187138049.json、图片生成/文生图/1970937254313107458.json、图片生成/文生图/1970950894877609986.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `LimitNumber`
- `LoadImage`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `TextCombinerSix`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 40 | 4 | 70% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 4 | 61% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy seed、LayerUtility: PurgeVRAM V2
