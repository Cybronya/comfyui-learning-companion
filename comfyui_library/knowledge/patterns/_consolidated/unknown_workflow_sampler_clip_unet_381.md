---
name: unknown_workflow_sampler_clip_unet_381
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.94675
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: []
missing: []
members: [平台全量/klein人像去塑料感高清修复_2060886702041944065.json, 平台全量/图像清晰修复_1953827606942633986.json, 平台全量/模糊图片变清晰  图像清晰修复 高清放大_2061247267818004482.json, 平台全量/模糊图片变清晰+高清放大 图像清晰修复_2064525320392372225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_381

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/klein人像去塑料感高清修复_2060886702041944065.json、平台全量/图像清晰修复_1953827606942633986.json、平台全量/模糊图片变清晰  图像清晰修复 高清放大_2061247267818004482.json、平台全量/模糊图片变清晰+高清放大 图像清晰修复_2064525320392372225.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | sa_solver | - | 4 | 100% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，4 个样本，一致性 100%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 100%
