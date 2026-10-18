---
key: 视频生成/图生视频/LTX2.3数字人说话唱歌高精准对口型_2101198595667095554.json
name: LTX2.3数字人说话唱歌高精准对口型_2101198595667095554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人说话唱歌高精准对口型_2101198595667095554.json
hash: cd745194bd0ef7a6
coverage: 0.822581
learned_at: 2026-10-17 02:14:10
nodes: [RandomNoise, LTXVConcatAVLatent, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, Reroute, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CLIPTextEncode, CFGGuider, CheckpointLoaderSimple, LTXVConditioning, KSamplerSelect, LTXVLatentUpsampler, LTXVImgToVideoInplace, SamplerCustomAdvanced, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVImgToVideoInplace, VAEDecodeTiled, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVAudioVAEEncode, Any Switch (rgthree), LTXVEmptyLatentAudio, SolidMask, SetLatentNoiseMask, CLIPTextEncode, ComfyMathExpression, easy cleanGpuUsed, Any Switch (rgthree), RandomNoise, TrimAudioDuration, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveInt, SimpleMath+, RHHiddenNodes, PrimitiveInt, PrimitiveInt, ResizeImageMaskNode, ResizeImagesByLongerEdge, ManualSigmas, PrimitiveInt, CM_IntToFloat, CM_IntToFloat, LTXVPreprocess, PreviewImage, CreateVideo, CM_IntToFloat, LoadAudio, PrimitiveInt, MarkdownNote, PrimitiveStringMultiline, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3数字人说话唱歌高精准对口型_2101198595667095554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人说话唱歌高精准对口型_2101198595667095554.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
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
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
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
- `SimpleMath+`
- `RHHiddenNodes`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `ManualSigmas`
- `PrimitiveInt`
- `CM_IntToFloat`
- `CM_IntToFloat`
- `LTXVPreprocess`
- `PreviewImage`
- `CreateVideo`
- `CM_IntToFloat`
- `LoadAudio`
- `PrimitiveInt`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（51/62）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`SolidMask`、`SetLatentNoiseMask`、`easy cleanGpuUsed`、`TrimAudioDuration`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`SimpleMath+`、`RHHiddenNodes`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`CM_IntToFloat`、`LTXVPreprocess`、`CreateVideo`、`LoadAudio`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
