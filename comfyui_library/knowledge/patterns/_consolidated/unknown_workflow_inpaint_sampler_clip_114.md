---
name: unknown_workflow_inpaint_sampler_clip_114
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.972
common_nodes: [CLIPTextEncode, CLIPVisionEncode, ConditioningZeroOut, ConstrainImage|pysssss, DifferentialDiffusion, FluxGuidance, GetImageSize+, Image Blend by Mask, Image to Noise, ImageConcanate, ImageCrop, ImageResizeKJ, ImageToMask, InpaintModelConditioning, InvertMask, KSampler, LayerUtility: ColorImage, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskToImage, SaveImage, SimpleMath+, SplitImageWithAlpha, StyleModelApply, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/阿里ACE++最新无瑕疵换装_1892034733931663362.json, 平台全量/Redux+AEC万物迁移电商产品换装工作流-StarAI_1912571926873866241.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/阿里ACE++最新无瑕疵换装_1892034733931663362.json、平台全量/Redux+AEC万物迁移电商产品换装工作流-StarAI_1912571926873866241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DifferentialDiffusion`
- `FluxGuidance`
- `GetImageSize+`
- `Image Blend by Mask`
- `Image to Noise`
- `ImageConcanate`
- `ImageCrop`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `LayerUtility: ColorImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskToImage`
- `SaveImage`
- `SimpleMath+`
- `SplitImageWithAlpha`
- `StyleModelApply`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `workflow/模型组` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
