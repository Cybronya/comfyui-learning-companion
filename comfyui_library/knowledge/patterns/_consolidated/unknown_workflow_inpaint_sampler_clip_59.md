---
name: unknown_workflow_inpaint_sampler_clip_59
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.633
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FloatConstant, FluxGuidance, GetNode, GrowMaskWithBlur, ImageCompositeMasked, ImageCrop, ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, Mask Crop Region, MaskPreview+, MaskToImage, PreviewImage, SaveImage, SetNode, SimpleMathBoolean+, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FiLL修手修一切万物均可修（烂图修复神器）_1923560566143840258.json, 图片生成/图生图/万物修复 - 可处理各种AI生图的bug的方法 comfyui 工作流_1923006903839092737.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FiLL修手修一切万物均可修（烂图修复神器）_1923560566143840258.json、图片生成/图生图/万物修复 - 可处理各种AI生图的bug的方法 comfyui 工作流_1923006903839092737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FloatConstant`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageCrop`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `Mask Crop Region`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `SimpleMathBoolean+`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RH_Translator` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
