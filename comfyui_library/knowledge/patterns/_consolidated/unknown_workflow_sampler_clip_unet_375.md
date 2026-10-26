---
name: unknown_workflow_sampler_clip_unet_375
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.929667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, ResolutionSelector, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/🐘Flux3_klein-图像编辑_2110934568877518850.json, 图片生成/文生图/Flux3_klein-文生图_2110997853291245569.json, 图片生成/文生图/🐘Flux3_klein-文生图_2110969244363083778.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_375

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/🐘Flux3_klein-图像编辑_2110934568877518850.json、图片生成/文生图/Flux3_klein-文生图_2110997853291245569.json、图片生成/文生图/🐘Flux3_klein-文生图_2110969244363083778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ReferenceMultiLatent` —— 1/3 个有

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
