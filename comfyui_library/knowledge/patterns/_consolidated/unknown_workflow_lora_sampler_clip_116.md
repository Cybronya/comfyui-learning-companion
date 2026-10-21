---
name: unknown_workflow_lora_sampler_clip_116
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.282333
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, CR Text, ConditioningZeroOut, GetNode, KSampler, Lora Loader Stack (rgthree), ModelSamplingAuraFlow, SaveImage, Seed (rgthree), SetNode, UNETLoader, VAEDecode, VAELoader, easy promptConcat]
problems: []
missing: [CR Text, CR SDXL Aspect Ratio, Lora Loader Stack (rgthree), Seed (rgthree), easy promptConcat, LayerUtility: PurgeVRAM]
members: [图片生成/文生图/1972192446874578945.json, 图片生成/文生图/1984095755768102914.json, 图片生成/文生图/1988231309522812930.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_116

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1972192446874578945.json、图片生成/文生图/1984095755768102914.json、图片生成/文生图/1988231309522812930.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：28%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CR Text`
- `ConditioningZeroOut`
- `GetNode`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UltimateSDUpscaleNoUpscale` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 3 | 65% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR SDXL Aspect Ratio、Lora Loader Stack (rgthree)、Seed (rgthree)、easy promptConcat
