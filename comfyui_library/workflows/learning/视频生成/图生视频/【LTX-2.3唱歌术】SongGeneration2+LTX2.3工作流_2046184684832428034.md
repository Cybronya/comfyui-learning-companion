---
key: 视频生成/图生视频/【LTX-2.3唱歌术】SongGeneration2+LTX2.3工作流_2046184684832428034.json
name: 【LTX-2.3唱歌术】SongGeneration2+LTX2.3工作流_2046184684832428034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046184684832428034.json
hash: e816b788afa7a0a8
coverage: 0.859375
learned_at: 2026-10-15 22:36:56
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CFGGuider, VAEDecodeTiled, LTXVImgToVideoInplace, SolidMask, LTXVAudioVAELoader, ResizeImagesByLongerEdge, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, LTXVConcatAVLatent, SetLatentNoiseMask, LatentUpscaleModelLoader, LoraLoaderModelOnly, ResizeImageMaskNode, LTXAVTextEncoderLoader, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, Label (rgthree), CreateVideo, SaveVideo, Note, SongGeneration_Loader, SongGeneration_Sampler, Note, SaveAudio, SongGeneration_Stage2, PreviewAudio, SongGeneration_Stage1, Label (rgthree), Fast Groups Bypasser (rgthree), LoadAudio, TrimAudioDuration, PrimitiveFloat, PrimitiveInt, PrimitiveInt, CLIPTextEncode, CheckpointLoaderSimple, LoadImage, RH_LLMAPI_Pro_Node, TextInput_, PrimitiveStringMultiline, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/【LTX-2.3唱歌术】SongGeneration2+LTX2.3工作流_2046184684832428034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046184684832428034.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoInplace`
- `SolidMask`
- `LTXVAudioVAELoader`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `ResizeImageMaskNode`
- `LTXAVTextEncoderLoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `Label (rgthree)`
- `CreateVideo`
- `SaveVideo`
- `Note`
- `SongGeneration_Loader`
- `SongGeneration_Sampler` ★核心
- `Note`
- `SaveAudio`
- `SongGeneration_Stage2`
- `PreviewAudio`
- `SongGeneration_Stage1`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `TrimAudioDuration`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `TextInput_`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **86%**（55/64）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`VAEDecodeTiled`、`SolidMask`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`ResizeImageMaskNode`、`LTXAVTextEncoderLoader`、`Label (rgthree)`、`CreateVideo`、`SaveVideo`、`SongGeneration_Loader`、`SongGeneration_Sampler`、`SaveAudio`、`SongGeneration_Stage2`、`PreviewAudio`、`SongGeneration_Stage1`、`LoadAudio`、`TrimAudioDuration`、`CheckpointLoaderSimple`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`TextInput_`、`PrimitiveBoolean`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
