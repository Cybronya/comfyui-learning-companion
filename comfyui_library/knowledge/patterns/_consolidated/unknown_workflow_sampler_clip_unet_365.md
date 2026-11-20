---
name: unknown_workflow_sampler_clip_unet_365
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.91875
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen千问UI图标制作_1953131721208303618.json, 图片生成/文生图/Qwen千问文生图 测试_1952903251559649281.json, 图片生成/文生图/Qwen千问文生图+Z-image真实感洗图_1994294742995369986.json, 图片生成/文生图/千问文生图+Z-image增强真实感强强联合_1993897697482571778.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_365

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen千问UI图标制作_1953131721208303618.json、图片生成/文生图/Qwen千问文生图 测试_1952903251559649281.json、图片生成/文生图/Qwen千问文生图+Z-image真实感洗图_1994294742995369986.json、图片生成/文生图/千问文生图+Z-image增强真实感强强联合_1993897697482571778.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `LayerUtility: RoundedRectangle` —— 1/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 10 - 20 | 4 | 67% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 4 | 4 | 41% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.7 | 0.4 - 1 | 4 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 4，4 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.4 - 1，4 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
