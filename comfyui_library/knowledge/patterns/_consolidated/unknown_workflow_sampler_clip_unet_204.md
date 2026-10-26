---
name: unknown_workflow_sampler_clip_unet_204
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.916
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json, 图片生成/文生图/Z-Image-Turbo 文生图 _ 9 节点极简模板_2086642662031060994.json, 图片生成/文生图/Z-Image-Turbo 文生图_2104866138722230274.json, 图片生成/文生图/Z-Image-Turbo-文生图_2013422713167155201.json, 图片生成/文生图/Zimage文生图基础_2044005460373676034.json, 图片生成/文生图/Zimage文生图基础_2060261069804892162.json, 图片生成/文生图/z-image-有无负面提示词对比_2016338426164944897.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_204

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json、图片生成/文生图/Z-Image-Turbo 文生图 _ 9 节点极简模板_2086642662031060994.json、图片生成/文生图/Z-Image-Turbo 文生图_2104866138722230274.json、图片生成/文生图/Z-Image-Turbo-文生图_2013422713167155201.json、图片生成/文生图/Zimage文生图基础_2044005460373676034.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ModelSamplingAuraFlow` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `LoadImage` —— 2/7 个有
- `LayerMask: BiRefNetUltra` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `Text` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `VAEDecodeTiled` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 7 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | res_multistep | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，7 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 res_multistep，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
