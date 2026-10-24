---
name: unknown_workflow_sampler_clip_unet_221
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9525
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLSampler (BSS) 画质提升-ZImage_2062006258563108866.json, 图片生成/文生图/Flux2.0-Dev _ 文生图_1993501652189642754.json, 图片生成/文生图/Flux2文生图_1993378851996844034.json, 图片生成/文生图/Flux2文生图官方版_1993503885006405633.json, 图片生成/文生图/Qwen千问文生图+Z-image真实感洗图_1994294742995369986.json, 图片生成/文生图/千问文生图+Z-image增强真实感强强联合_1993897697482571778.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_221

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/FLSampler (BSS) 画质提升-ZImage_2062006258563108866.json、图片生成/文生图/Flux2.0-Dev _ 文生图_1993501652189642754.json、图片生成/文生图/Flux2文生图_1993378851996844034.json、图片生成/文生图/Flux2文生图官方版_1993503885006405633.json、图片生成/文生图/Qwen千问文生图+Z-image真实感洗图_1994294742995369986.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `LayerUtility: PurgeVRAM V2` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `FLS_SamplerV4` —— 1/6 个有
- `LoadImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 20 | 6 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.4 - 1 | 6 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，6 个样本
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
