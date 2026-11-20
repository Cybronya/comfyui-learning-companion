---
name: text_to_image_video_upscale_latent_upscale_16
type: Text To Image
frequency: 4
level: strong
coverage: 0.91725
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR String To Number, ComfyMathExpression, EmptyLatentImage, GuHaiAutoImageSplit, ImageBatchMulti, ImageFromBatch+, ImageResizeKJv2, Int, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ExtendCanvasV2, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SimpleMath+, SplitSigmas, StringConcatenate, StringSubstring, Text Load Line From File, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy mathInt, easy showAnything, easy sleep, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ComfyUI图生图通用工作流 图片处理灵活方案_2110247428615139329.json, 图片生成/图生图/ComfyUI图生图通用工作流 图片处理灵活方案_2110362524469252098.json, 图片生成/图生图/comfyui工作流新版 图像编辑方案高质量稳定_2109351622294982658.json, 图片生成/图生图/comfyui通用图生图工作流｜新手拿来就能跑的万金油_2103723313355902978.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/ComfyUI图生图通用工作流 图片处理灵活方案_2110247428615139329.json、图片生成/图生图/ComfyUI图生图通用工作流 图片处理灵活方案_2110362524469252098.json、图片生成/图生图/comfyui工作流新版 图像编辑方案高质量稳定_2109351622294982658.json、图片生成/图生图/comfyui通用图生图工作流｜新手拿来就能跑的万金油_2103723313355902978.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR String To Number`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GuHaiAutoImageSplit`
- `ImageBatchMulti`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ExtendCanvasV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `SplitSigmas`
- `StringConcatenate`
- `StringSubstring`
- `Text Load Line From File`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy mathInt`
- `easy showAnything`
- `easy sleep`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
