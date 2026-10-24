---
name: unknown_workflow_inpaint_sampler_clip_63
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6885
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), InpaintModelConditioning, InvertMask, KSampler, LoadImage, MaskPreview+, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux一键换背景_1903764418365132802.json, 图片生成/图生图/换背景工作流 (FLUX+Redux模型组合)_2045069052585971714.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux一键换背景_1903764418365132802.json、图片生成/图生图/换背景工作流 (FLUX+Redux模型组合)_2045069052585971714.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModel` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26 | - | 2 | 85% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26，样本不足，未给区间，2 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
