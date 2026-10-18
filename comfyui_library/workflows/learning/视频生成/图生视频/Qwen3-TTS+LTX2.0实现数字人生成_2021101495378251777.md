---
key: 视频生成/图生视频/Qwen3-TTS+LTX2.0实现数字人生成_2021101495378251777.json
name: Qwen3-TTS+LTX2.0实现数字人生成_2021101495378251777.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen3-TTS+LTX2.0实现数字人生成_2021101495378251777.json
hash: 46c1a92f9a2a6894
coverage: 0.533333
learned_at: 2026-10-15 22:35:07
nodes: [GetNode, LoraLoaderModelOnly, Qwen3TTSVoiceClone, VAELoader, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, SetNode, PrimitiveFloat, SetNode, INTConstant, ImageResizeKJv2, GetNode, GetNode, SetNode, CLIPTextEncode, GetNode, LTXVPreprocess, SetNode, LTXVEmptyLatentAudio, GetNode, SimpleMath+, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, GetNode, LTX2AudioLatentNormalizingSampling, CFGGuider, GetNode, GetNode, LTXVScheduler, KSamplerSelect, LTXVSeparateAVLatent, GetNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, GetNode, SolidMask, SimpleCalculatorKJ, VRAM_Debug, Audio Duration (mtb), LTXVAudioVAEEncode, SetLatentNoiseMask, SetNode, SetNode, DualCLIPLoaderGGUF, LTXVConcatAVLatent, SetNode, SamplerCustomAdvanced, GetNode, easy showAnything, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, ManualSigmas, RandomNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, GetNode, Qwen3TTSModelLoader, LoadAudio, LoadImage, SetNode, SetNode, SetNode, INTConstant, CLIPTextEncode, LTXVConditioning, SetNode, SetNode, CheckpointLoaderSimple, LoraLoaderModelOnly, SetNode, GetNode, ResizeImagesByLongerEdge, ImageScaleBy, GetImageSize, GetNode, GetNode, GetNode, CFGGuider, SaveAudio, GetNode, GetNode, RandomNoise, LTXVSeparateAVLatent, LTXVLatentUpsampler, GetNode, CR Text, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 121}
---

# 视频生成/图生视频/Qwen3-TTS+LTX2.0实现数字人生成_2021101495378251777.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021101495378251777.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `Qwen3TTSVoiceClone`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `SimpleMath+`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTX2AudioLatentNormalizingSampling`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SolidMask`
- `SimpleCalculatorKJ`
- `VRAM_Debug`
- `Audio Duration (mtb)`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SetNode`
- `SetNode`
- `DualCLIPLoaderGGUF`
- `LTXVConcatAVLatent`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ManualSigmas`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Qwen3TTSModelLoader`
- `LoadAudio`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `ImageScaleBy`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `SaveAudio`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `CR Text`
- `CR Text`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **53%**（56/105）

**有卡**：`LoraLoaderModelOnly`、`Qwen3TTSVoiceClone`、`VAELoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`INTConstant`、`ImageResizeKJv2`、`CLIPTextEncode`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTX2AudioLatentNormalizingSampling`、`CFGGuider`、`LTXVScheduler`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SolidMask`、`SimpleCalculatorKJ`、`VRAM_Debug`、`Audio Duration (mtb)`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`DualCLIPLoaderGGUF`、`VHS_VideoCombine`、`ManualSigmas`、`RandomNoise`、`Qwen3TTSModelLoader`、`LoadAudio`、`LoadImage`、`LTXVConditioning`、`CheckpointLoaderSimple`、`ResizeImagesByLongerEdge`、`ImageScaleBy`、`GetImageSize`、`SaveAudio`、`LTXVLatentUpsampler`、`CR Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
