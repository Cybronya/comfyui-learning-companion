---
key: 视频生成/图生视频/Seedance2平替！LTX2.3图生有声视频_2028654571588952066.json
name: Seedance2平替！LTX2.3图生有声视频_2028654571588952066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2028654571588952066.json
hash: 703804f70073bad9
coverage: 0.875
learned_at: 2026-10-15 22:35:19
nodes: [MarkdownNote, KSamplerSelect, KSamplerSelect, LTXVCropGuides, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, ImageScaleBy, GetImageSize, GetImageSize, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, CFGGuider, EmptyImage, ResizeImagesByLongerEdge, CheckpointLoaderSimple, LTXVConditioning, VAEDecode, CreateVideo, PreviewAny, LTXAVTextEncoderLoader, CLIPTextEncode, CLIPTextEncode, TextGenerateLTX2Prompt, RandomNoise, CFGGuider, ManualSigmas, LTXVLatentUpsampler, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVScheduler, RandomNoise, SamplerCustomAdvanced, LoraLoaderModelOnly, ResizeImageMaskNode, MarkdownNote, LoadImage, CR SDXL Aspect Ratio, SaveVideo, PrimitiveInt, PrimitiveStringMultiline, LTXVEmptyLatentAudio, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/Seedance2平替！LTX2.3图生有声视频_2028654571588952066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2028654571588952066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `ImageScaleBy`
- `GetImageSize`
- `GetImageSize`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `EmptyImage`
- `ResizeImagesByLongerEdge`
- `CheckpointLoaderSimple` ★核心
- `LTXVConditioning`
- `VAEDecode` ★核心
- `CreateVideo`
- `PreviewAny`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `ResizeImageMaskNode`
- `MarkdownNote`
- `LoadImage`
- `CR SDXL Aspect Ratio`
- `SaveVideo`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（42/48）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`LTXVConcatAVLatent`、`ImageScaleBy`、`GetImageSize`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`CFGGuider`、`EmptyImage`、`ResizeImagesByLongerEdge`、`CheckpointLoaderSimple`、`LTXVConditioning`、`VAEDecode`、`CreateVideo`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`TextGenerateLTX2Prompt`、`RandomNoise`、`ManualSigmas`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVScheduler`、`LoraLoaderModelOnly`、`ResizeImageMaskNode`、`LoadImage`、`CR SDXL Aspect Ratio`、`SaveVideo`、`LTXVEmptyLatentAudio`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
