---
name: unknown_workflow_sampler_clip_vae_2
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1954314194239811586.json, 图片生成/文生图/1954461836424953858.json, 图片生成/文生图/1954565922696654850.json, 图片生成/文生图/1954567812612288513.json, 图片生成/文生图/1954743795998965761.json, 图片生成/文生图/1954768333373620226.json, 图片生成/文生图/1954773431147479041.json, 图片生成/文生图/1955214645163278337.json, 图片生成/文生图/1955920019513376770.json, 图片生成/文生图/1959414093880963073.json, 图片生成/文生图/1964993982478602241.json, 图片生成/文生图/1981766660744986626.json, 图片生成/文生图/Qwen-Image文生图（亚洲复古胶片摄影）_2063953908111859714.json, 图片生成/文生图/Qwen-image Lora_2007472820174987265.json, 图片生成/文生图/千问QWEN IMAGE极速文生图_2006405852235833345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_2

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/1954314194239811586.json、图片生成/文生图/1954461836424953858.json、图片生成/文生图/1954565922696654850.json、图片生成/文生图/1954567812612288513.json、图片生成/文生图/1954743795998965761.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 14/15 个有
- `UNETLoader` —— 14/15 个有
- `PrimitiveStringMultiline` —— 11/15 个有
- `PrimitiveInt` —— 6/15 个有
- `easy cleanGpuUsed` —— 5/15 个有
- `ConditioningZeroOut` —— 4/15 个有
- `LoraLoader` —— 4/15 个有
- `LoraLoaderModelOnly` —— 4/15 个有
- `FluxResolutionNode` —— 3/15 个有
- `AV_LoraLoader` —— 2/15 个有
- `NunchakuQwenImageDiTLoader` —— 2/15 个有
- `CFGNorm` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| 采样步数 | 10 | 8 - 25 | 15 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 15 | 24% |
| 采样算法 | euler | - | 15 | 67% |
| 调度器 | simple | - | 15 | 87% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 8 - 25，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，15 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，15 个样本，一致性 67%
- 调度器 最常用 simple，15 个样本，一致性 87%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
