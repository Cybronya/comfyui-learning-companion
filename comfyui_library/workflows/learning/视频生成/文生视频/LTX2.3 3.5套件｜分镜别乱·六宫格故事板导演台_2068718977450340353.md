---
key: 视频生成/文生视频/LTX2.3 3.5套件｜分镜别乱·六宫格故事板导演台_2068718977450340353.json
name: LTX2.3 3.5套件｜分镜别乱·六宫格故事板导演台_2068718977450340353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 3.5套件｜分镜别乱·六宫格故事板导演台_2068718977450340353.json
hash: 3b5b16a60e4128f5
coverage: 0.970297
learned_at: 2026-10-11 20:21:25
nodes: [ManualSigmas, KSamplerSelect, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVConditioning, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGGuider, LTXDirectorGuide, LTXDirectorGuide, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVLatentUpsampler, FluxResolutionNode, LTXDirectorGuide, SamplerCustomAdvanced, LTXVConcatAVLatent, SamplerCustomAdvanced, VAEDecodeTiled, LTXVAudioVAEDecode, LatentUpscaleModelLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, LTX2_NAG, LoraLoaderModelOnly, LTX2_NAG, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Sigmas Easing, STGGuiderAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, VAEDecodeTiled, CreateVideo, SaveVideo, VAEDecodeTiled, LTXVAudioVAEDecode, SaveVideo, CreateVideo, SaveVideo, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVCropGuides, CreateVideo, VAEDecodeTiled, SetLatentNoiseMask, LTXVSeparateAVLatent, SolidMask, ManualSigmas, KSamplerSelect, LTXVLatentUpsampler, LTXVCropGuides, LTXVCropGuides, RandomNoise, VAEDecodeTiled, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, image_scale_pixel_v2, EmptyImage, LTXDirector, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEDecode, LoadImage, PrimitiveInt, ImageFromBatch, ImageFromBatch, ImageFromBatch, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, CS-LTXGridDirector]
patterns: []
missing: [CS-LTXGridDirector, Sigmas Easing]
parameters: {"checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors"}
discoveries: [次要节点 `CS-LTXGridDirector` 知识库中没有该节点类型的任何知识, 次要节点 `Sigmas Easing` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 3.5套件｜分镜别乱·六宫格故事板导演台_2068718977450340353.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 3.5套件｜分镜别乱·六宫格故事板导演台_2068718977450340353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `FluxResolutionNode`
- `LTXDirectorGuide`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Sigmas Easing`
- `STGGuiderAdvanced`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SaveVideo`
- `CreateVideo`
- `SaveVideo`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `SetLatentNoiseMask`
- `LTXVSeparateAVLatent`
- `SolidMask`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVCropGuides`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `EmptyImage`
- `LTXDirector`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LoadImage`
- `PrimitiveInt`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `CS-LTXGridDirector`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **97%**（98/101）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`CFGGuider`、`LTXDirectorGuide`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LTXVLatentUpsampler`、`FluxResolutionNode`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LTX2_NAG`、`STGGuiderAdvanced`、`LTXICLoRALoaderModelOnly`、`CreateVideo`、`SaveVideo`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`SetLatentNoiseMask`、`SolidMask`、`RandomNoise`、`image_scale_pixel_v2`、`EmptyImage`、`LTXDirector`、`LoadImage`、`ImageFromBatch`

**缺卡**（2）：`CS-LTXGridDirector`、`Sigmas Easing`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CS-LTXGridDirector` 知识库中没有该节点类型的任何知识
- 次要节点 `Sigmas Easing` 知识库中没有该节点类型的任何知识
