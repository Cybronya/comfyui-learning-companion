---
name: unknown_workflow_sampler_clip_unet_342
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.345
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, GetNode, Image Comparer (rgthree), ImageBatchOneOrMore, ImageScaleToTotalPixels, KSampler, LazySwitchKJ, LoadImage, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, ReferenceMultiLatent, ResizeAndPadImage, ResolutionSelector, SaveImage, SeedNode, SetNode, TextGenerate, UNETLoader, VAEDecode, VAELoader, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/图生图/FLUX 3 Klein 多功能整合工作流（16步蒸馏版 ·官方提示词增强）_2112320339689693186.json, 图片生成/图生图/FLUX+3 Klein  多功能整合 官方版_2111016753500352513.json, 图片生成/文生图/FLUX 3 Klein 多功能整合工作流（16步蒸馏版 ·官方提示词增强）_2110967971152752642.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_342

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX 3 Klein 多功能整合工作流（16步蒸馏版 ·官方提示词增强）_2112320339689693186.json、图片生成/图生图/FLUX+3 Klein  多功能整合 官方版_2111016753500352513.json、图片生成/文生图/FLUX 3 Klein 多功能整合工作流（16步蒸馏版 ·官方提示词增强）_2110967971152752642.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：34%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageBatchOneOrMore`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LazySwitchKJ`
- `LoadImage`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ReferenceMultiLatent`
- `ResizeAndPadImage`
- `ResolutionSelector`
- `SaveImage`
- `SeedNode`
- `SetNode`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 16 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 16，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
