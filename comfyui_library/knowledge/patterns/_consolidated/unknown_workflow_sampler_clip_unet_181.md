---
name: unknown_workflow_sampler_clip_unet_181
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.914
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1971371663310929922.json, 图片生成/文生图/Newbie Image 文生图_2025554845473705985.json, 图片生成/文生图/【琉梦】最强二次元_动漫 文生图 + 简易工作流 + Newbie Image模型 + 快速出图_2016462546584215553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_181

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1971371663310929922.json、图片生成/文生图/Newbie Image 文生图_2025554845473705985.json、图片生成/文生图/【琉梦】最强二次元_动漫 文生图 + 简易工作流 + Newbie Image模型 + 快速出图_2016462546584215553.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `RescaleCFG` —— 2/3 个有
- `EmptyHunyuanImageLatent` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 20 - 28 | 3 | 85% |
| Prompt 约束强度(CFG) | 4.5 | 3 - 4.5 | 3 | 82% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | linear_quadratic | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 20 - 28，3 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3 - 4.5，3 个样本，取值集中（一致性 82%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 linear_quadratic，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
