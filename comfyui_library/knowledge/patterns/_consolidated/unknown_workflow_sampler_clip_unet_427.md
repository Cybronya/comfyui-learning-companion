---
name: unknown_workflow_sampler_clip_unet_427
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6225
common_nodes: [ApplyRegionalConds, BasicGuider, BasicScheduler, CLIPTextEncode, ConfigureModifiedFlux, CreateRegionalCond, CreateShapeMask, DualCLIPLoader, EmptyLatentImage, FluxAttnOverride, FluxDeGuidance, GetNode, INTConstant, KSamplerSelect, MaskToImage, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/抖音涨粉爆款一键生成多个美女_1894911849743908865.json, 图片生成/文生图/区域提示+深度提示=布局引导的场景生成_1898351164520353793.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_427

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/抖音涨粉爆款一键生成多个美女_1894911849743908865.json、图片生成/文生图/区域提示+深度提示=布局引导的场景生成_1898351164520353793.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyRegionalConds`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConfigureModifiedFlux`
- `CreateRegionalCond`
- `CreateShapeMask`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxAttnOverride`
- `FluxDeGuidance`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `MaskToImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Apply LoRA Stack` —— 1/2 个有
- `CR LoRA Stack` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `InstructPixToPixConditioning` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Mask Invert` —— 1/2 个有
- `MaskFromColor+` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1344 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1344，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
