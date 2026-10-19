---
name: text_to_image_controlnet_upscale_lora_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.7895
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageResize+, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: [ImageResize+, LayerUtility: ImageBlendAdvance V3, Preview from image [Crystools]]
members: [图片生成/文生图/1919597654442184705.json, 图片生成/文生图/1938147090012749826.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1919597654442184705.json、图片生成/文生图/1938147090012749826.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `InspyrenetRembg` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance V3` —— 1/2 个有
- `Preview from image [Crystools]` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：ImageResize+、LayerUtility: ImageBlendAdvance V3、Preview from image [Crystools]
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
