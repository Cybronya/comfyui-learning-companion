---
name: text_to_image_video_upscale_latent_upscale_21
type: Text To Image
frequency: 3
level: strong
coverage: 0.88
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX-2.5-I2V图生视频｜双采样加速视频生成工作流_2096312957528530946.json, 视频生成/图生视频/三图首中尾帧视频图生视频｜老孙AI多图参考视频生成工作流_2087224294895087618.json, 视频生成/图生视频/出片提速神器｜LTX-2.5-I2V双采样图生视频加速_2096525982470590465.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5-I2V图生视频｜双采样加速视频生成工作流_2096312957528530946.json、视频生成/图生视频/三图首中尾帧视频图生视频｜老孙AI多图参考视频生成工作流_2087224294895087618.json、视频生成/图生视频/出片提速神器｜LTX-2.5-I2V双采样图生视频加速_2096525982470590465.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `EmptyImage` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `LTXAVTextEncoderLoader` —— 1/3 个有
- `LTXVAudioVAELoader` —— 1/3 个有
- `LTXVChunkFeedForward` —— 1/3 个有
- `LTXVImgToVideoInplaceKJ` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `ResizeImagesByLongerEdge` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `TextCombinerTwo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
