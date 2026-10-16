---
key: 视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json
name: ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json
hash: c375b66c5e19822b
coverage: 0.87931
learned_at: 2026-10-16 22:01:52
nodes: [RandomNoise, LTXVConcatAVLatent, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ResizeImagesByLongerEdge, KSamplerSelect, Reroute, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CFGGuider, KSamplerSelect, LTXVLatentUpsampler, LTXVImgToVideoInplace, SamplerCustomAdvanced, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVImgToVideoInplace, VAEDecodeTiled, CreateVideo, LTXVAudioVAEDecode, LTXVAudioVAEEncode, Any Switch (rgthree), LTXVEmptyLatentAudio, SolidMask, SetLatentNoiseMask, ComfyMathExpression, easy cleanGpuUsed, Any Switch (rgthree), RandomNoise, TrimAudioDuration, LoraLoaderModelOnly, PrimitiveBoolean, SimpleMath+, RHHiddenNodes, ManualSigmas, CM_IntToFloat, CM_IntToFloat, CM_IntToFloat, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, ConditioningConcat, EmptyLTXVLatentVideo, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadAudio, LTXVPreprocess, CheckpointLoaderSimple, MarkdownNote, LoadImage, VHS_VideoCombine, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（58 个）：
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
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `Any Switch (rgthree)`
- `LTXVEmptyLatentAudio` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `ComfyMathExpression`
- `easy cleanGpuUsed`
- `Any Switch (rgthree)`
- `RandomNoise`
- `TrimAudioDuration`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `SimpleMath+`
- `RHHiddenNodes`
- `ManualSigmas`
- `CM_IntToFloat`
- `CM_IntToFloat`
- `CM_IntToFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ConditioningConcat`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadAudio`
- `LTXVPreprocess`
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`
- `LoadImage`
- `VHS_VideoCombine`
- `RH_LLMAPI_Pro_Node`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（51/58）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ResizeImagesByLongerEdge`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`CreateVideo`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`SolidMask`、`SetLatentNoiseMask`、`ComfyMathExpression`、`easy cleanGpuUsed`、`TrimAudioDuration`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`SimpleMath+`、`RHHiddenNodes`、`CM_IntToFloat`、`CLIPTextEncode`、`LTXVConditioning`、`ConditioningConcat`、`EmptyLTXVLatentVideo`、`LoadAudio`、`LTXVPreprocess`、`CheckpointLoaderSimple`、`LoadImage`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
