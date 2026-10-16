---
key: 视频生成/图生视频/LTX 2.3 电商模特产品展示  分辨率和你传图一致_2084197196118974466.json
name: LTX 2.3 电商模特产品展示  分辨率和你传图一致_2084197196118974466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3 电商模特产品展示  分辨率和你传图一致_2084197196118974466.json
hash: 84d903a7d28c86e0
coverage: 0.928571
learned_at: 2026-10-16 19:52:08
nodes: [LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXAVTextEncoderLoader, ImageScaleBy, EmptyImage, GetImageSize, PrimitiveInt, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVImgToVideoInplace, LoraLoaderModelOnly, PreviewAny, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LatentUpscaleModelLoader, RandomNoise, CFGGuider, KSamplerSelect, LTXVScheduler, LTXVLatentUpsampler, LTXVConcatAVLatent, VAEDecode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, KSampler, ResizeImageMaskNode, DualCLIPLoader, CheckpointLoaderSimple, GetImageSize, LTXVAudioVAELoader, ResizeImagesByLongerEdge, CreateVideo, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, TextGenerateLTX2Prompt, LoadImage, MuyeTextEditOutput, 孤海注释, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 227659934210360, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX 2.3 电商模特产品展示  分辨率和你传图一致_2084197196118974466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX 2.3 电商模特产品展示  分辨率和你传图一致_2084197196118974466.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXAVTextEncoderLoader`
- `ImageScaleBy`
- `EmptyImage`
- `GetImageSize`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `KSampler` ★核心
- `ResizeImageMaskNode`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `GetImageSize`
- `LTXVAudioVAELoader`
- `ResizeImagesByLongerEdge`
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `MuyeTextEditOutput`
- `孤海注释`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `227659934210360`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **93%**（39/42）

**有卡**：`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXAVTextEncoderLoader`、`ImageScaleBy`、`EmptyImage`、`GetImageSize`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LTXVScheduler`、`LTXVLatentUpsampler`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`KSampler`、`ResizeImageMaskNode`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`CreateVideo`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`TextGenerateLTX2Prompt`、`LoadImage`、`MuyeTextEditOutput`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
