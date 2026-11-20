---
name: unknown_workflow_sampler_clip_unet_357
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.71675
common_nodes: [CLIPLoader, CLIPTextEncode, CreateBoundingBoxes, EmptyFlux2LatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux.3-Klein-文生图-bbox提示词增强扩写(UpSampler）_2115021845564051458.json, 图片生成/文生图/Flux3 Klein 文生图标准版_2113456940520132610.json, 图片生成/文生图/Flux3 Klein官方文生图_2112067434525061121.json, 图片生成/文生图/flux3_klein 文生图 base版本_2110956211372904449.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_357

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux.3-Klein-文生图-bbox提示词增强扩写(UpSampler）_2115021845564051458.json、图片生成/文生图/Flux3 Klein 文生图标准版_2113456940520132610.json、图片生成/文生图/Flux3 Klein官方文生图_2112067434525061121.json、图片生成/文生图/flux3_klein 文生图 base版本_2110956211372904449.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateBoundingBoxes`
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
- `ComfySwitchNode` —— 3/4 个有
- `Flux3LayoutPrompt` —— 3/4 个有
- `ComfyNotNode` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `ShowAnything|Mie` —— 1/4 个有
- `Switch string [Crystools]` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 33 | 15 - 50 | 4 | 47% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 3.5 | 4 | 44% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 33，观测区间 15 - 50，4 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
