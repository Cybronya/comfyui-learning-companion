---
name: unknown_workflow_inpaint_sampler_clip_77
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.615333
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FloatConstant, FluxGuidance, GetNode, GrowMaskWithBlur, ImageCompositeMasked, ImageCrop, ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, Mask Crop Region, MaskPreview+, MaskToImage, PreviewImage, SaveImage, SetNode, SimpleMathBoolean+, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FiLL修手修一切万物均可修（烂图修复神器）_1923560566143840258.json, 图片生成/图生图/万物修复 - 可处理各种AI生图的bug的方法 comfyui 工作流_1923006903839092737.json, 平台全量/[高清版] 万物修复_1922527162283474946.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FiLL修手修一切万物均可修（烂图修复神器）_1923560566143840258.json、图片生成/图生图/万物修复 - 可处理各种AI生图的bug的方法 comfyui 工作流_1923006903839092737.json、平台全量/[高清版] 万物修复_1922527162283474946.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `JJC_JoyCaption` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
