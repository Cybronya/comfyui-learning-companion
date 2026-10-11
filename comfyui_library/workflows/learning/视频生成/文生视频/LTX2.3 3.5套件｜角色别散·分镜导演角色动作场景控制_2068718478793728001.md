---
key: 视频生成/文生视频/LTX2.3 3.5套件｜角色别散·分镜导演角色动作场景控制_2068718478793728001.json
name: LTX2.3 3.5套件｜角色别散·分镜导演角色动作场景控制_2068718478793728001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 3.5套件｜角色别散·分镜导演角色动作场景控制_2068718478793728001.json
hash: da2306cac2e40999
coverage: 0.98
learned_at: 2026-10-11 20:21:25
nodes: [ManualSigmas, KSamplerSelect, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVConditioning, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGGuider, LTXDirectorGuide, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVLatentUpsampler, FluxResolutionNode, LTXDirectorGuide, SamplerCustomAdvanced, SamplerCustomAdvanced, VAEDecodeTiled, LatentUpscaleModelLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, LTX2_NAG, LoraLoaderModelOnly, LTX2_NAG, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Sigmas Easing, STGGuiderAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, SaveVideo, CreateVideo, SaveVideo, LTXVSeparateAVLatent, CreateVideo, VAEDecodeTiled, SetLatentNoiseMask, LTXVSeparateAVLatent, SolidMask, ManualSigmas, KSamplerSelect, LTXVLatentUpsampler, LTXVCropGuides, LTXVCropGuides, RandomNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, image_scale_pixel_v2, EmptyImage, LTXVAudioVAEDecode, SamplerCustomAdvanced, LTXDirectorGuide, LTXVConcatAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVCropGuides, LTXVAudioVAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, PrimitiveInt, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, ImageFromBatch, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXDirector]
patterns: []
missing: [Sigmas Easing]
parameters: {"checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors"}
discoveries: [次要节点 `Sigmas Easing` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 3.5套件｜角色别散·分镜导演角色动作场景控制_2068718478793728001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 3.5套件｜角色别散·分镜导演角色动作场景控制_2068718478793728001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
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
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `FluxResolutionNode`
- `LTXDirectorGuide`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `LTXVAudioVAEDecode` ★核心
- `SaveVideo`
- `CreateVideo`
- `SaveVideo`
- `LTXVSeparateAVLatent`
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `EmptyImage`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `ImageFromBatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXDirector`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **98%**（98/100）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`CFGGuider`、`LTXDirectorGuide`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LTXVLatentUpsampler`、`FluxResolutionNode`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LTX2_NAG`、`STGGuiderAdvanced`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAEDecode`、`SaveVideo`、`CreateVideo`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`SolidMask`、`LTXVCropGuides`、`RandomNoise`、`image_scale_pixel_v2`、`EmptyImage`、`VHS_VideoCombine`、`ImageFromBatch`、`LTXDirector`

**缺卡**（1）：`Sigmas Easing`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Sigmas Easing` 知识库中没有该节点类型的任何知识
