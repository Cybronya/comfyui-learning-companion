---
key: 视频生成/文生视频/LTX-2.3配音术升级版：输入台词就能生成短剧！FishAudio S2 + LTX-2.3实战_2034068608220930049.json
name: LTX-2.3配音术升级版：输入台词就能生成短剧！FishAudio S2 + LTX-2.3实战_2034068608220930049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3配音术升级版：输入台词就能生成短剧！FishAudio S2 + LTX-2.3实战_2034068608220930049.json
hash: 74c6c505e77e94f2
coverage: 0.844828
learned_at: 2026-10-11 03:48:35
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, CLIPTextEncode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CFGGuider, LTXVImgToVideoInplace, PrimitiveInt, SolidMask, LTXVAudioVAELoader, PrimitiveBoolean, ResizeImagesByLongerEdge, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, PrimitiveInt, TrimAudioDuration, LTXVAudioVAEEncode, LTXVConcatAVLatent, SetLatentNoiseMask, LoraLoaderModelOnly, CheckpointLoaderSimple, ResizeImageMaskNode, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, PrimitiveInt, ComfyMathExpression, PrimitiveFloat, VAEDecodeTiled, LTXVAudioVAEDecode, SaveVideo, MarkdownNote, MarkdownNote, LoadAudio, LoadAudio, LoadImage, LoadAudio, PrimitiveStringMultiline, SaveAudio, FishS2MultiSpeakerTTS, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/文生视频/LTX-2.3配音术升级版：输入台词就能生成短剧！FishAudio S2 + LTX-2.3实战_2034068608220930049.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3配音术升级版：输入台词就能生成短剧！FishAudio S2 + LTX-2.3实战_2034068608220930049.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
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
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `SolidMask`
- `LTXVAudioVAELoader`
- `PrimitiveBoolean`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `ResizeImageMaskNode`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `FishS2MultiSpeakerTTS`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **84%**（49/58）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`LTXVAudioVAELoader`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ComfyMathExpression`、`CreateVideo`、`EmptyLTXVLatentVideo`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`ResizeImageMaskNode`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SaveVideo`、`LoadAudio`、`LoadImage`、`SaveAudio`、`FishS2MultiSpeakerTTS`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
