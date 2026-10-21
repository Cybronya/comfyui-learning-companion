---
name: unknown_workflow_lora_sampler_clip_82
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.74825
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, LayerUtility: PurgeVRAM V2, Text Concatenate]
members: [图片生成/文生图/1983414394384228354.json, 图片生成/文生图/1983878313116631041.json, 图片生成/文生图/1984151149953646593.json, 图片生成/文生图/1984179316147847170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1983414394384228354.json、图片生成/文生图/1983878313116631041.json、图片生成/文生图/1984151149953646593.json、图片生成/文生图/1984179316147847170.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Any Switch (rgthree)` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `Seed` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 10 - 30 | 4 | 65% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 4 | 60% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 10 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、LayerUtility: ImageScaleByAspectRatio V2、Text Multiline、LayerUtility: PurgeVRAM V2
