---
key: 视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json
name: CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json
hash: 866cfcce7dcdbaba
coverage: 0.821429
learned_at: 2026-10-15 22:44:05
nodes: [CLIPTextEncode, LTXVConditioning, GetImageSize, RandomNoise, LatentUpscaleModelLoader, LTX2_NAG, LTX2SamplingPreviewOverride, INTConstant, INTConstant, INTConstant, SetNode, LTXVScheduler, SetNode, ResizeImagesByLongerEdge, LoadImage, ResizeImageMaskNode, PreviewImage, SetNode, SetNode, PreviewImage, LTXVConcatAVLatent, LTXVPreprocess, EmptyImage, ImageScaleBy, EmptyLTXVLatentVideo, ManualSigmas, LTXVCropGuides, LTXVImgToVideoInplace, LTXVImgToVideoInplace, SamplerCustomAdvanced, KSamplerSelect, PrimitiveBoolean, Note, INTConstant, LTXVSeparateAVLatent, CreateVideo, LTXVAudioVAEDecode, VAEDecode, BasicScheduler, CFGGuider, KSampler, LTXVLatentUpsampler, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVSeparateAVLatent, CLIPTextEncode, VHS_VideoCombine, Note, SaveVideo, MarkdownNote, MarkdownNote, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 535846521724675, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetImageSize`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `LTXVScheduler`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `ResizeImageMaskNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `EmptyImage`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `ManualSigmas`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveBoolean`
- `Note`
- `INTConstant`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `CFGGuider`
- `KSampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Note`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `535846521724675`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **82%**（46/56）

**有卡**：`CLIPTextEncode`、`LTXVConditioning`、`GetImageSize`、`RandomNoise`、`LatentUpscaleModelLoader`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`INTConstant`、`LTXVScheduler`、`ResizeImagesByLongerEdge`、`LoadImage`、`ResizeImageMaskNode`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`EmptyImage`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`KSamplerSelect`、`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAEDecode`、`BasicScheduler`、`CFGGuider`、`KSampler`、`LTXVLatentUpsampler`、`LTXVEmptyLatentAudio`、`VHS_VideoCombine`、`SaveVideo`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
