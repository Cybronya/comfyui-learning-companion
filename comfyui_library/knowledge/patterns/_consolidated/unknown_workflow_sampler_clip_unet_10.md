---
name: unknown_workflow_sampler_clip_unet_10
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.769533
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1954314194239811586.json, 图片生成/文生图/1954423623698280449.json, 图片生成/文生图/1954461836424953858.json, 图片生成/文生图/1954743795998965761.json, 图片生成/文生图/1954768333373620226.json, 图片生成/文生图/1954773431147479041.json, 图片生成/文生图/1954817663203721218.json, 图片生成/文生图/1955342392250417153.json, 图片生成/文生图/1955920019513376770.json, 图片生成/文生图/1959887822478061569.json, 图片生成/文生图/1961062588018835457.json, 图片生成/文生图/1961085397939982338.json, 图片生成/文生图/1964982995616677890.json, 图片生成/文生图/1966026218137096193.json, 图片生成/文生图/1970348297275777025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/1954314194239811586.json、图片生成/文生图/1954423623698280449.json、图片生成/文生图/1954461836424953858.json、图片生成/文生图/1954743795998965761.json、图片生成/文生图/1954768333373620226.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 9/15 个有
- `LoraLoaderModelOnly` —— 7/15 个有
- `LayerUtility: ImageReel` —— 6/15 个有
- `LayerUtility: ImageReelComposit` —— 6/15 个有
- `PrimitiveInt` —— 6/15 个有
- `PrimitiveStringMultiline` —— 6/15 个有
- `LoraLoader` —— 4/15 个有
- `AV_LoraLoader` —— 2/15 个有
- `ImpactInt` —— 1/15 个有
- `LayerUtility: PurgeVRAM V2` —— 1/15 个有
- `NunchakuQwenImageDiTLoader` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| 采样步数 | 10 | 4 - 30 | 15 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 15 | 29% |
| 采样算法 | euler | - | 15 | 47% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 4 - 30，15 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，15 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，15 个样本，一致性 47%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、LayerUtility: PurgeVRAM V2
