---
key: 视频生成/文生视频/LTX-2.3 MSR 多图参考视频生成｜三阶渲染增强版_2065743626793209857.json
name: LTX-2.3 MSR 多图参考视频生成｜三阶渲染增强版_2065743626793209857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3 MSR 多图参考视频生成｜三阶渲染增强版_2065743626793209857.json
hash: 94bff4ed95e1babb
coverage: 1
learned_at: 2026-10-15 22:44:37
nodes: [LTXICLoRALoaderModelOnly, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConcatAVLatent, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConcatAVLatent, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, LTXVAudioVAEDecode, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXAddVideoICLoRAGuide, CreateVideo, LTXAddVideoICLoRAGuide, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVEmptyLatentAudio, CLIPTextEncode, ImageResizeKJv2, GetImageSize, ImageResizeKJv2, LiconMSR, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LowVRAMCheckpointLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, INTConstant, SaveVideo, CLIPTextEncode, LoraLoaderModelOnly, image_scale_pixel_v2]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors", "height": 24, "width": 751}
---

# 视频生成/文生视频/LTX-2.3 MSR 多图参考视频生成｜三阶渲染增强版_2065743626793209857.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3 MSR 多图参考视频生成｜三阶渲染增强版_2065743626793209857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `LTXICLoRALoaderModelOnly` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXAddVideoICLoRAGuide`
- `CreateVideo`
- `LTXAddVideoICLoRAGuide`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `GetImageSize`
- `ImageResizeKJv2`
- `LiconMSR`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LowVRAMCheckpointLoader` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `INTConstant`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`

## 关键参数

- `width` = `751`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **100%**（66/66）

**有卡**：`LTXICLoRALoaderModelOnly`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`CreateVideo`、`SaveVideo`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`ImageResizeKJv2`、`GetImageSize`、`LiconMSR`、`LoadImage`、`LowVRAMCheckpointLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`INTConstant`、`LoraLoaderModelOnly`、`image_scale_pixel_v2`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
