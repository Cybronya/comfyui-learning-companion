---
key: 视频生成/文生视频/LTX2.3数字人说话唱歌-无字幕、提示词优化版_2034907055777124353.json
name: LTX2.3数字人说话唱歌-无字幕、提示词优化版_2034907055777124353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人说话唱歌-无字幕、提示词优化版_2034907055777124353.json
hash: 97a655b3be92fcd9
coverage: 0.724638
learned_at: 2026-10-11 03:48:36
nodes: [RandomNoise, LTXVConcatAVLatent, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ResizeImagesByLongerEdge, KSamplerSelect, Reroute, ManualSigmas, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CLIPTextEncode, CFGGuider, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVConditioning, KSamplerSelect, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, SamplerCustomAdvanced, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVImgToVideoInplace, VAEDecodeTiled, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVAudioVAEEncode, Any Switch (rgthree), LTXVEmptyLatentAudio, SolidMask, CM_IntToFloat, SetLatentNoiseMask, ResizeImageMaskNode, RH_LLMAPI_Pro_Node, LoadImage, MarkdownNote, PrimitiveInt, CM_IntToFloat, Fast Groups Bypasser (rgthree), SimpleMath+, Label (rgthree), MarkdownNote, MarkdownNote, PrimitiveInt, PrimitiveInt, PreviewAny, PrimitiveBoolean, PrimitiveInt, CLIPTextEncode, Any Switch (rgthree), Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, LoadAudio, ComfyMathExpression, easy cleanGpuUsed, Any Switch (rgthree), TrimAudioDuration, VHS_VideoCombine, RHHiddenNodes, RHHiddenNodes, Fast Groups Bypasser (rgthree), RandomNoise]
patterns: []
missing: [Label (rgthree), SimpleMath+, easy cleanGpuUsed]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3数字人说话唱歌-无字幕、提示词优化版_2034907055777124353.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人说话唱歌-无字幕、提示词优化版_2034907055777124353.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（69 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ResizeImagesByLongerEdge`
- `KSamplerSelect` ★核心
- `Reroute`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `CM_IntToFloat`
- `SetLatentNoiseMask`
- `ResizeImageMaskNode`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveInt`
- `CM_IntToFloat`
- `Fast Groups Bypasser (rgthree)`
- `SimpleMath+`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `ComfyMathExpression`
- `easy cleanGpuUsed`
- `Any Switch (rgthree)`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Fast Groups Bypasser (rgthree)`
- `RandomNoise`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（50/69）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ResizeImagesByLongerEdge`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`CreateVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`SolidMask`、`CM_IntToFloat`、`SetLatentNoiseMask`、`ResizeImageMaskNode`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`PrimitiveBoolean`、`LoadAudio`、`TrimAudioDuration`、`VHS_VideoCombine`、`RHHiddenNodes`

**缺卡**（3）：`Label (rgthree)`、`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
