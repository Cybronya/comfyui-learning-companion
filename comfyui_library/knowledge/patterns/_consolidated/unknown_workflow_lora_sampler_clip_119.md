---
name: unknown_workflow_lora_sampler_clip_119
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.820667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, easy cleanGpuUsed, Seed (rgthree), LayerUtility: ImageScaleByAspectRatio V2, RunningHub Deepcleaner, SimpleMath+]
members: [图片生成/文生图/1983771974319153153.json, 图片生成/文生图/1984294296314658817.json, 图片生成/文生图/Qwen_千问-时尚穿搭_1995326727742218242.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_119

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1983771974319153153.json、图片生成/文生图/1984294296314658817.json、图片生成/文生图/Qwen_千问-时尚穿搭_1995326727742218242.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `ImageUpscaleWithModelCUDAspeedFixed` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy cleanGpuUsed、Seed (rgthree)、LayerUtility: ImageScaleByAspectRatio V2、RunningHub Deepcleaner
