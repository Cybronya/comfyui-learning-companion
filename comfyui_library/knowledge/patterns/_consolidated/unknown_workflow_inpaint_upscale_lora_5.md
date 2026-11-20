---
name: unknown_workflow_inpaint_upscale_lora_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.947
common_nodes: [CLIPTextEncode, CR Color Bars, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, ETN_CropImage, EmptySD3LatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, GlobalSeed //Inspire, Image To Mask, ImageBlur, ImageInvert, ImageUpscaleWithModel, InjectNoiseToLatent, InpaintModelConditioning, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, Paste By Mask, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/HDR360 全景环境生成_1942056269798916098.json, 平台全量/Seamless 360° Flux Image Generator_1891331746825379841.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/HDR360 全景环境生成_1942056269798916098.json、平台全量/Seamless 360° Flux Image Generator_1891331746825379841.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Color Bars`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `ETN_CropImage`
- `EmptySD3LatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GlobalSeed //Inspire`
- `Image To Mask`
- `ImageBlur`
- `ImageInvert`
- `ImageUpscaleWithModel`
- `InjectNoiseToLatent`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `Paste By Mask`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AlphaChanelRemove` —— 1/2 个有
- `Cut By Mask` —— 1/2 个有
- `ImageCompositeAbsolute` —— 1/2 个有
- `ImagePaste` —— 1/2 个有
- `ImageRemoveAlpha+` —— 1/2 个有
- `JjkShowText` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
