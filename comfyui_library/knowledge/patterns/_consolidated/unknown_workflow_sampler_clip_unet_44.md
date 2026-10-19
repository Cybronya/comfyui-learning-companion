---
name: unknown_workflow_sampler_clip_unet_44
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.871
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1947211070849110017.json, 图片生成/文生图/1950928691515817986.json, 图片生成/文生图/1952795772553203714.json, 图片生成/文生图/1952820714467487746.json, 图片生成/文生图/1952877428207194113.json, 图片生成/文生图/1953630061981257729.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_44

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1947211070849110017.json、图片生成/文生图/1950928691515817986.json、图片生成/文生图/1952795772553203714.json、图片生成/文生图/1952820714467487746.json、图片生成/文生图/1952877428207194113.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `RH_Captioner` —— 3/6 个有
- `DualCLIPLoader` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 6 | 54% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
