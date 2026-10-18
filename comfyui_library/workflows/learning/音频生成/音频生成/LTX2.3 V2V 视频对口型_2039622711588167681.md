---
key: 音频生成/音频生成/LTX2.3 V2V 视频对口型_2039622711588167681.json
name: LTX2.3 V2V 视频对口型_2039622711588167681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX2.3 V2V 视频对口型_2039622711588167681.json
hash: 9ec97cc19ed71303
coverage: 0.833333
learned_at: 2026-10-18 02:28:41
nodes: [MarkdownNote, LTXVConcatAVLatent, KSamplerSelect, SamplerCustomAdvanced, KSamplerSelect, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, RandomNoise, RandomNoise, ManualSigmas, ManualSigmas, SaveVideo, TrimAudioDuration, LTXVConditioning, CFGGuider, CLIPTextEncode, CLIPTextEncode, LTXVCropGuides, LTXVCropGuides, LTXVSeparateAVLatent, LTXVAudioVAEEncode, SetLatentNoiseMask, VAEEncode, LTXVSetVideoLatentNoiseMasks, PrimitiveStringMultiline, ImageResizeKJv2, MarkdownNote, MarkdownNote, PrimitiveInt, MarkdownNote, LoadAudio, GetImageRangeFromBatch, BlockifyMask, GetImageRangeFromBatch, ResizeMask, LTXVPreprocessMasks, LTXVImgToVideoInplace, Reroute, LTXVLatentUpsampler, VAEEncode, LTXVConcatAVLatent, LTXVAudioVideoMask, LTXVAddLatentGuide, Reroute, CreateVideo, VAEDecodeTiled, PrimitiveInt, VHS_LoadVideoFFmpeg, VHS_VideoInfo, GetImageSize, SolidMask, ComfyMathExpression, LatentUpscaleModelLoader, FaceSegment, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, DualCLIPLoaderGGUF, MarkdownNote]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 音频生成/音频生成/LTX2.3 V2V 视频对口型_2039622711588167681.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX2.3 V2V 视频对口型_2039622711588167681.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `RandomNoise`
- `ManualSigmas`
- `ManualSigmas`
- `SaveVideo`
- `TrimAudioDuration`
- `LTXVConditioning`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `LTXVSetVideoLatentNoiseMasks`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveInt`
- `MarkdownNote`
- `LoadAudio`
- `GetImageRangeFromBatch`
- `BlockifyMask`
- `GetImageRangeFromBatch`
- `ResizeMask`
- `LTXVPreprocessMasks`
- `LTXVImgToVideoInplace`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `VAEEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVideoMask`
- `LTXVAddLatentGuide`
- `Reroute`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoInfo`
- `GetImageSize`
- `SolidMask`
- `ComfyMathExpression`
- `LatentUpscaleModelLoader`
- `FaceSegment`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `DualCLIPLoaderGGUF`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（50/60）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CFGGuider`、`RandomNoise`、`ManualSigmas`、`SaveVideo`、`TrimAudioDuration`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`VAEEncode`、`LTXVSetVideoLatentNoiseMasks`、`ImageResizeKJv2`、`LoadAudio`、`GetImageRangeFromBatch`、`BlockifyMask`、`ResizeMask`、`LTXVPreprocessMasks`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LTXVAudioVideoMask`、`LTXVAddLatentGuide`、`CreateVideo`、`VAEDecodeTiled`、`VHS_LoadVideoFFmpeg`、`VHS_VideoInfo`、`GetImageSize`、`SolidMask`、`ComfyMathExpression`、`LatentUpscaleModelLoader`、`FaceSegment`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`DualCLIPLoaderGGUF`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
