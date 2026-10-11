---
key: 视频生成/文生视频/【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697.json
name: 【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697.json
hash: b78c414c0a1e0393
coverage: 0.822581
learned_at: 2026-10-11 03:48:39
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CFGGuider, VAEDecodeTiled, LTXVImgToVideoInplace, SolidMask, LTXVAudioVAELoader, ResizeImagesByLongerEdge, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, TrimAudioDuration, LTXVAudioVAEEncode, LTXVConcatAVLatent, SetLatentNoiseMask, LatentUpscaleModelLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, ResizeImageMaskNode, LoadImage, LTXAVTextEncoderLoader, ComfyMathExpression, ComfyMathExpression, LoadAudio, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveBoolean, PrimitiveStringMultiline, Label (rgthree), CreateVideo, SaveVideo, Note, SongGeneration_Loader, SongGeneration_Sampler, Note, SaveAudio, SongGeneration_Stage2, PreviewAudio, SongGeneration_Stage1, Label (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: [Label (rgthree), Label (rgthree)]
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
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
- `CLIPTextEncode` ★核心
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
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `ResizeImageMaskNode`
- `LoadImage`
- `LTXAVTextEncoderLoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LoadAudio`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
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

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **82%**（51/62）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SolidMask`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`ResizeImageMaskNode`、`LoadImage`、`LTXAVTextEncoderLoader`、`LoadAudio`、`PrimitiveBoolean`、`CreateVideo`、`SaveVideo`、`SongGeneration_Loader`、`SongGeneration_Sampler`、`SaveAudio`、`SongGeneration_Stage2`、`PreviewAudio`、`SongGeneration_Stage1`

**缺卡**（2）：`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
