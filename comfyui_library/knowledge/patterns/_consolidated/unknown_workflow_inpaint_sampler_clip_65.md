---
name: unknown_workflow_inpaint_sampler_clip_65
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.982
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/flux fill+redu万物迁移_1950148533690220546.json, 图片生成/图生图/redux风格迁移Reduced Adebance节点_1922216491712970754.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux fill+redu万物迁移_1950148533690220546.json、图片生成/图生图/redux风格迁移Reduced Adebance节点_1922216491712970754.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `FluxLoraLoader` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImpactGaussianBlurMask` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
