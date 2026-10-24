---
name: unknown_workflow_sampler_clip_unet_391
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.866333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, PrimitiveInt, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/对比系列01-5大生图模型对比_2050390146960379906.json, 图片生成/文生图/对比系列03-Lens_Lens-Turbo_ZIT文生图_2066895289654530049.json, 图片生成/文生图/工作流基础系列30-Lens_Lens-T文生图工作流_2066888219807014913.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_391

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/对比系列01-5大生图模型对比_2050390146960379906.json、图片生成/文生图/对比系列03-Lens_Lens-Turbo_ZIT文生图_2066895289654530049.json、图片生成/文生图/工作流基础系列30-Lens_Lens-T文生图工作流_2066888219807014913.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LayerUtility: TextBox` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `CFGNorm` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RH_RhartImageG2TextToImage` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
