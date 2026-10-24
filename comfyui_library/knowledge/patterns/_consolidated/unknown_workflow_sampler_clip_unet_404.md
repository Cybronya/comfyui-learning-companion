---
name: unknown_workflow_sampler_clip_unet_404
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.776
common_nodes: [AnySwitch, BasicGuider, CLIPLoader, CLIPTextEncode, ComfySwitchNode, CreateBoundingBoxes, EmptyFlux2LatentImage, Fast Bypasser (rgthree), Int, KSampler, KSamplerSelect, ManualSigmas, PreviewAny, PrimitiveBoolean, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX3.0 Klein多图编辑 满血+急速生成_2110934398165143554.json, 图片生成/文生图/FLUX3.0 Klein 文生图 满血+急速+提示词优化_2110777373066096641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_404

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX3.0 Klein多图编辑 满血+急速生成_2110934398165143554.json、图片生成/文生图/FLUX3.0 Klein 文生图 满血+急速+提示词优化_2110777373066096641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `AnySwitch`
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `CreateBoundingBoxes`
- `EmptyFlux2LatentImage`
- `Fast Bypasser (rgthree)`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `ManualSigmas`
- `PreviewAny`
- `PrimitiveBoolean`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ReferenceMultiLatent` —— 1/2 个有
- `TextGenerate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 75% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
