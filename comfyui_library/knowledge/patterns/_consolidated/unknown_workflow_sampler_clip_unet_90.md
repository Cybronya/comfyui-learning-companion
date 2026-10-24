---
name: unknown_workflow_sampler_clip_unet_90
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.923727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json, 图片生成/文生图/Z-Image-Turbo 文生图 _ 9 节点极简模板_2086642662031060994.json, 图片生成/文生图/Z-Image-Turbo 文生图_2104866138722230274.json, 图片生成/文生图/Z-Image-Turbo-文生图_2013422713167155201.json, 图片生成/文生图/Z-Image_turbo造像模型文生图极速版_2049364318055043073.json, 图片生成/文生图/Z-Image（base）文生图_2016049580982407169.json, 图片生成/文生图/ZIT基础文生图_2088289408716992513.json, 图片生成/文生图/Z_image_turbo文生图原版工作流-B站UP主@好奇漫步_1995897359357919233.json, 图片生成/文生图/Zimage文生图基础_2044005460373676034.json, 图片生成/文生图/Zimage文生图基础_2060261069804892162.json, 图片生成/文生图/z-image-有无负面提示词对比_2016338426164944897.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json、图片生成/文生图/Z-Image-Turbo 文生图 _ 9 节点极简模板_2086642662031060994.json、图片生成/文生图/Z-Image-Turbo 文生图_2104866138722230274.json、图片生成/文生图/Z-Image-Turbo-文生图_2013422713167155201.json、图片生成/文生图/Z-Image_turbo造像模型文生图极速版_2049364318055043073.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/11 个有
- `ModelSamplingAuraFlow` —— 9/11 个有
- `LoadImage` —— 5/11 个有
- `PreviewImage` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `LayerMask: BiRefNetUltra` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `Text` —— 1/11 个有
- `UnetLoaderGGUF` —— 1/11 个有
- `VAEDecodeTiled` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 11 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 34% |
| 采样算法 | res_multistep | - | 11 | 82% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，11 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 res_multistep，11 个样本，一致性 82%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（7/11 个样本）：Steps较低可能导致细节不足
