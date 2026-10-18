---
key: 视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json
name: LTX-2.5-I2V+双采样加速视频生成_2096206827863232514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json
hash: 163aaba18ba58d93
coverage: 0.87234
learned_at: 2026-10-17 01:09:24
nodes: [KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, RandomNoise, ImageScaleBy, LoadImage, ManualSigmas, easy showAnything, easy showAnything, ImageResizeKJv2, LTXVPreprocess, ResolutionSelector, MarkdownNote, LatentUpscaleModelLoader, CLIPLoader, VAELoader, VAELoader, UNETLoader, ModelAttentionBackend, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, EmptyImage, PrimitiveFloat, PrimitiveInt, LTXVEmptyLatentAudio, GetImageSize, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, ComfyMathExpression, CR Prompt Text, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `ImageScaleBy`
- `LoadImage`
- `ManualSigmas`
- `easy showAnything`
- `easy showAnything`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ResolutionSelector`
- `MarkdownNote`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `EmptyImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`KSamplerSelect`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`ImageScaleBy`、`LoadImage`、`ManualSigmas`、`ImageResizeKJv2`、`LTXVPreprocess`、`ResolutionSelector`、`LatentUpscaleModelLoader`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelAttentionBackend`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyImage`、`LTXVEmptyLatentAudio`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ComfyMathExpression`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
