---
name: image_to_image_inpaint_upscale_lora_9
type: Image To Image
frequency: 2
level: weak
coverage: 0.792
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConstrainImage|pysssss, DifferentialDiffusion, DualCLIPLoader, EmptyImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetNode, GrowMaskWithBlur, ImageCompositeMasked, ImageConcatMulti, ImageScaleBy, ImageUpscaleWithModel, InpaintModelConditioning, InvertMask, KSampler, KSamplerSelect, LayerColor: AutoAdjustV2, LayerColor: AutoBrightness, LoadImage, LoraLoaderModelOnly, MaskPreview+, PreviewImage, RandomNoise, SamplerCustomAdvanced, SetNode, StyleModelApply, StyleModelLoader, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageScaleDownToSize, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flux+Redux换背景（自动蒙版+手动蒙版）_1937682268783558657.json, 平台全量/Flux+Redux换背景新思路_1864317414564626433.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux+Redux换背景（自动蒙版+手动蒙版）_1937682268783558657.json、平台全量/Flux+Redux换背景新思路_1864317414564626433.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConstrainImage|pysssss`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `KSamplerSelect`
- `LayerColor: AutoAdjustV2`
- `LayerColor: AutoBrightness`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageScaleDownToSize`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `AddMask` —— 1/2 个有
- `BiRefNet_Hugo` —— 1/2 个有
- `FeatheredMask` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `InspyrenetRembg` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
