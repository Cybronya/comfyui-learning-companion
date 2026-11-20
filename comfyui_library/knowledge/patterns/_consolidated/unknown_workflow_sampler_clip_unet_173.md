---
name: unknown_workflow_sampler_clip_unet_173
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.831875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/flux2_2018920250036719617.json, 图片生成/文生图/flux3-image-klein（文生图）_2111219542662930433.json, 图片生成/文生图/flux3_klein_文生图_2111049485966204929.json, 图片生成/文生图/flux3文生图_2110958826278187009.json, 图片生成/文生图/自动词优化版Moss-image Sft文生图_2112123208332824577.json, 数字人/数字人/MOSS sft Comfyui官方工作流文生图_2112066748353695746.json, 视频生成/文生视频/MOSS_sft_Comfyui官方_2113787365826326529.json, 视频生成/文生视频/MOSS_sft_Comfyui官方_2113788793810673665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_173

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/flux2_2018920250036719617.json、图片生成/文生图/flux3-image-klein（文生图）_2111219542662930433.json、图片生成/文生图/flux3_klein_文生图_2111049485966204929.json、图片生成/文生图/flux3文生图_2110958826278187009.json、图片生成/文生图/自动词优化版Moss-image Sft文生图_2112123208332824577.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 6/8 个有
- `ResolutionSelector` —— 6/8 个有
- `PreviewAny` —— 4/8 个有
- `TextGenerate` —— 4/8 个有
- `SkipLayerGuidanceDiTSimple` —— 3/8 个有
- `EmptyImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 37.5 | 4 - 50 | 8 | 44% |
| Prompt 约束强度(CFG) | 3 | 1 - 3.5 | 8 | 56% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 37.5，观测区间 4 - 50，8 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
