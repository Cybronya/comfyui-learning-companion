---
key: 视频生成/图生视频/LTX2.3数字人精准对口型，类型：说话、唱歌_2062387729098428417.json
name: LTX2.3数字人精准对口型，类型：说话、唱歌_2062387729098428417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062387729098428417.json
hash: c723a569ab0bd0d9
coverage: 0.836066
learned_at: 2026-10-15 22:39:03
nodes: [RandomNoise, LTXVConcatAVLatent, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ResizeImagesByLongerEdge, KSamplerSelect, Reroute, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CLIPTextEncode, CFGGuider, CheckpointLoaderSimple, LTXVConditioning, KSamplerSelect, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, SamplerCustomAdvanced, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVImgToVideoInplace, VAEDecodeTiled, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVAudioVAEEncode, Any Switch (rgthree), LTXVEmptyLatentAudio, SolidMask, SetLatentNoiseMask, CLIPTextEncode, ComfyMathExpression, easy cleanGpuUsed, Any Switch (rgthree), RandomNoise, TrimAudioDuration, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, SimpleMath+, RHHiddenNodes, ManualSigmas, PrimitiveInt, CM_IntToFloat, CM_IntToFloat, CM_IntToFloat, VHS_VideoCombine, ResizeImageMaskNode, LoadImage, PrimitiveStringMultiline, MarkdownNote, PrimitiveInt, LoadAudio, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3数字人精准对口型，类型：说话、唱歌_2062387729098428417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062387729098428417.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（61 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ResizeImagesByLongerEdge`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `CheckpointLoaderSimple` ★核心
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `Any Switch (rgthree)`
- `LTXVEmptyLatentAudio` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `easy cleanGpuUsed`
- `Any Switch (rgthree)`
- `RandomNoise`
- `TrimAudioDuration`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `SimpleMath+`
- `RHHiddenNodes`
- `ManualSigmas`
- `PrimitiveInt`
- `CM_IntToFloat`
- `CM_IntToFloat`
- `CM_IntToFloat`
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `PrimitiveInt`
- `LoadAudio`
- `PrimitiveInt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（51/61）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ResizeImagesByLongerEdge`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`CreateVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`SolidMask`、`SetLatentNoiseMask`、`easy cleanGpuUsed`、`TrimAudioDuration`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`SimpleMath+`、`RHHiddenNodes`、`CM_IntToFloat`、`VHS_VideoCombine`、`ResizeImageMaskNode`、`LoadImage`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
