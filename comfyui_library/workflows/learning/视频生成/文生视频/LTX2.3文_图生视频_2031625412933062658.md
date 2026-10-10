---
key: 视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json
name: LTX2.3文_图生视频_2031625412933062658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json
hash: 4be1b1837c9ab479
coverage: 0.880952
learned_at: 2026-10-11 03:16:47
nodes: [VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, PreviewAny, LTXVImgToVideoInplace, LTXVConcatAVLatent, CreateVideo, ImageScaleBy, KSampler, SaveVideo, MarkdownNote, MarkdownNote, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, RH_LLMAPI_NODE, LTX2_NAG, EmptyLTXVLatentVideo, LoadImage, GetImageSize, EmptyImage, PrimitiveInt, CheckpointLoaderSimple, LTXAVTextEncoderLoader, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, LTXVScheduler, LoraLoaderModelOnly, LTXVSeparateAVLatent, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVCropGuides, GetImageSize, LTXVAudioVAELoader, LTXVConditioning, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, LTXVPreprocess]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 766044084899970, "steps": 4, "width": 97}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `CreateVideo`
- `ImageScaleBy`
- `KSampler` ★核心
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_LLMAPI_NODE`
- `LTX2_NAG`
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `GetImageSize`
- `EmptyImage`
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `GetImageSize`
- `LTXVAudioVAELoader`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`

## 关键参数

- `seed` = `766044084899970`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（37/42）

**有卡**：`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`CreateVideo`、`ImageScaleBy`、`KSampler`、`SaveVideo`、`RH_LLMAPI_NODE`、`LTX2_NAG`、`EmptyLTXVLatentVideo`、`LoadImage`、`GetImageSize`、`EmptyImage`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LTXVScheduler`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVAudioVAELoader`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
