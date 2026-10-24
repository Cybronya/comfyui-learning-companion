---
name: unknown_workflow_sampler_clip_unet_438
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.935
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSamplerAdvanced, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/ErineTurbo+Z-Image-双采_2053344254163992577.json, 图片生成/文生图/Flux_Klein_文生图_图像编辑_多图编辑_2013254277736697857.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_438

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/ErineTurbo+Z-Image-双采_2053344254163992577.json、图片生成/文生图/Flux_Klein_文生图_图像编辑_多图编辑_2013254277736697857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSamplerAdvanced`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 57% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | ddim_uniform | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 ddim_uniform，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
