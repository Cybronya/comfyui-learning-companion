---
key: 视频生成/文生视频/LTX2.3 - 多功能可独立音频数字人_2047017723305140225.json
name: LTX2.3 - 多功能可独立音频数字人_2047017723305140225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 - 多功能可独立音频数字人_2047017723305140225.json
hash: 8270734fdb08e32e
coverage: 0.803279
learned_at: 2026-10-11 19:49:36
nodes: [Reroute, Note, Note, CFGGuider, LTXVConditioning, CLIPTextEncode, LTXVCropGuides, LTXVSeparateAVLatent, PreviewAudio, SolidMask, CR Text, LTXVAudioVAEEncode, SetLatentNoiseMask, CLIPTextEncode, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, TrimAudioDuration, PrimitiveInt, CM_IntToFloat, LTXVImgToVideoInplace, CFGGuider, LTXVConcatAVLatent, ManualSigmas, easy cleanGpuUsed, ManualSigmas, RandomNoise, KSamplerSelect, LatentUpscaleModelLoader, LTXVAudioVAELoader, Any Switch (rgthree), LTXVImgToVideoInplace, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, SimpleMath+, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, VAEDecodeTiled, Any Switch (rgthree), RandomNoise, KSamplerSelect, CM_IntToFloat, SamplerCustomAdvanced, PrimitiveInt, PrimitiveInt, LoadImage, PrimitiveBoolean, SamplerCustomAdvanced, PrimitiveInt, AudioCrop, LoadAudio, LTXVConcatAVLatent, LTXVPreprocess, ResizeImagesByLongerEdge, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, VHS_VideoCombine, ImageResizeKJv2]
patterns: []
missing: [CR Text, SimpleMath+, easy cleanGpuUsed]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 - 多功能可独立音频数字人_2047017723305140225.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 - 多功能可独立音频数字人_2047017723305140225.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（61 个）：
- `Reroute`
- `Note`
- `Note`
- `CFGGuider`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `PreviewAudio`
- `SolidMask`
- `CR Text`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `TrimAudioDuration`
- `PrimitiveInt`
- `CM_IntToFloat`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `easy cleanGpuUsed`
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `Any Switch (rgthree)`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `Any Switch (rgthree)`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CM_IntToFloat`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveBoolean`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `AudioCrop`
- `LoadAudio`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `ImageResizeKJv2`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **80%**（49/61）

**有卡**：`CFGGuider`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`PreviewAudio`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`CreateVideo`、`TrimAudioDuration`、`CM_IntToFloat`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`ManualSigmas`、`RandomNoise`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`LoadImage`、`PrimitiveBoolean`、`AudioCrop`、`LoadAudio`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`ComfyMathExpression`、`VHS_VideoCombine`、`ImageResizeKJv2`

**缺卡**（3）：`CR Text`、`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
