---
key: 视频生成/图生视频/LTX2.3-图生视频_2066084809260224514.json
name: LTX2.3-图生视频_2066084809260224514.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-图生视频_2066084809260224514.json
hash: defe59eb60c4d28b
coverage: 0.904762
learned_at: 2026-10-15 22:39:46
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVPreprocess, CFGGuider, LatentUpscaleModelLoader, EmptyImage, CLIPTextEncode, LTXVImgToVideoInplace, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAEDecode, ResizeImagesByLongerEdge, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVCropGuides, CreateVideo, LTXVConditioning, RandomNoise, DualCLIPLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, ImageScaleBy, GetImageSize, SaveVideo, KSampler, MarkdownNote, MarkdownNote, PrimitiveInt, GetImageSize, CLIPTextEncode, LoadImage, ResizeImageMaskNode, TextGenerateLTX2Prompt, PreviewAny]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 601132197884772, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3-图生视频_2066084809260224514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066084809260224514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `EmptyImage`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecode` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `CreateVideo`
- `LTXVConditioning`
- `RandomNoise`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `SaveVideo`
- `KSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveInt`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ResizeImageMaskNode`
- `TextGenerateLTX2Prompt`
- `PreviewAny`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `601132197884772`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`CFGGuider`、`LatentUpscaleModelLoader`、`EmptyImage`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAEDecode`、`ResizeImagesByLongerEdge`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`CreateVideo`、`LTXVConditioning`、`RandomNoise`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`ImageScaleBy`、`GetImageSize`、`SaveVideo`、`KSampler`、`LoadImage`、`ResizeImageMaskNode`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
