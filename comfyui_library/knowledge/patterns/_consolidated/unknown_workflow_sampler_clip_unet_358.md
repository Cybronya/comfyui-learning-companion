---
name: unknown_workflow_sampler_clip_unet_358
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.76925
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux3_Klein_t2i_2111797746670854146.json, 图片生成/文生图/Moss-image_Sft文生图_自动词优化版_2115267946862960641.json, 图片生成/文生图/Moss-image_Sft文生图_自动词优化版_2115279858786988034.json, 图片生成/文生图/flux3-image-klein（文生图）_2110956174114910210.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_358

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux3_Klein_t2i_2111797746670854146.json、图片生成/文生图/Moss-image_Sft文生图_自动词优化版_2115267946862960641.json、图片生成/文生图/Moss-image_Sft文生图_自动词优化版_2115279858786988034.json、图片生成/文生图/flux3-image-klein（文生图）_2110956174114910210.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ModelSamplingFlux` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 15 - 50 | 4 | 55% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 4 | 60% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 15 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
