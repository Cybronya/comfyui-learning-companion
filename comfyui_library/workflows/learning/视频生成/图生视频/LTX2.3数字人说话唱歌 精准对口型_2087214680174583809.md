---
key: 视频生成/图生视频/LTX2.3数字人说话唱歌 精准对口型_2087214680174583809.json
name: LTX2.3数字人说话唱歌 精准对口型_2087214680174583809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人说话唱歌 精准对口型_2087214680174583809.json
hash: f5e04b61921fb7e4
coverage: 0.822581
learned_at: 2026-10-16 21:27:35
nodes: [RandomNoise, LTXVConcatAVLatent, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, Reroute, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CLIPTextEncode, CFGGuider, CheckpointLoaderSimple, LTXVConditioning, KSamplerSelect, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, SamplerCustomAdvanced, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVImgToVideoInplace, VAEDecodeTiled, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVAudioVAEEncode, Any Switch (rgthree), LTXVEmptyLatentAudio, SolidMask, SetLatentNoiseMask, CLIPTextEncode, ComfyMathExpression, easy cleanGpuUsed, Any Switch (rgthree), RandomNoise, TrimAudioDuration, LoraLoaderModelOnly, MarkdownNote, PrimitiveBoolean, PrimitiveInt, SimpleMath+, RHHiddenNodes, PrimitiveInt, LoadImage, PrimitiveStringMultiline, CM_IntToFloat, LoadAudio, PrimitiveInt, CM_IntToFloat, CM_IntToFloat, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, ResizeImageMaskNode, ResizeImagesByLongerEdge, PreviewImage, ManualSigmas]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3数字人说话唱歌 精准对口型_2087214680174583809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人说话唱歌 精准对口型_2087214680174583809.json`

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
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `SimpleMath+`
- `RHHiddenNodes`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveStringMultiline`
- `CM_IntToFloat`
- `LoadAudio`
- `PrimitiveInt`
- `CM_IntToFloat`
- `CM_IntToFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `PreviewImage`
- `ManualSigmas`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（51/62）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`CreateVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`SolidMask`、`SetLatentNoiseMask`、`easy cleanGpuUsed`、`TrimAudioDuration`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`SimpleMath+`、`RHHiddenNodes`、`LoadImage`、`CM_IntToFloat`、`LoadAudio`、`VHS_VideoCombine`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
