---
name: unknown_workflow_sampler_clip_unet_131
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.952333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS文生图2K极速版!_2112525560906870786.json, 图片生成/文生图/MOSS文生图2K极速版_2112541313756389378.json, 图片生成/文生图/Moss Image 4步快速文生图_2112395762205290497.json, 图片生成/文生图/Moss-Image图像生成（官方示例版）_2111823655494840322.json, 图片生成/文生图/flux.2-klein文生图_2077238073297031169.json, 图片生成/文生图/flux2_2018920250036719617.json, 图片生成/文生图/flux3_klein_文生图_2111049485966204929.json, 图片生成/文生图/flux3文生图_2110958826278187009.json, 图片生成/文生图/【遇见AI】Moss image 文生图8步加速基础流_2112071294949879810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_131

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/MOSS文生图2K极速版!_2112525560906870786.json、图片生成/文生图/MOSS文生图2K极速版_2112541313756389378.json、图片生成/文生图/Moss Image 4步快速文生图_2112395762205290497.json、图片生成/文生图/Moss-Image图像生成（官方示例版）_2111823655494840322.json、图片生成/文生图/flux.2-klein文生图_2077238073297031169.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 6/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `SkipLayerGuidanceDiTSimple` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 9 | 21% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，9 个样本，取值分散，一致性仅 21%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
