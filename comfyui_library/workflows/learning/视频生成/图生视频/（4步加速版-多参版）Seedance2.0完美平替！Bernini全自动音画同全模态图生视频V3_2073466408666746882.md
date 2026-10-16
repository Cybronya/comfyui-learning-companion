---
key: 视频生成/图生视频/（4步加速版-多参版）Seedance2.0完美平替！Bernini全自动音画同全模态图生视频V3_2073466408666746882.json
name: （4步加速版-多参版）Seedance2.0完美平替！Bernini全自动音画同全模态图生视频V3_2073466408666746882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073466408666746882.json
hash: 9859f1f992d6d572
coverage: 0.870968
learned_at: 2026-10-15 22:41:07
nodes: [VAEDecode, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, CreateVideo, EmptyAudio, AudioAdjustVolume, AdjustAudio, CLIPLoader, ConditioningZeroOut, AudioEncoderLoader, ModelPatchLoader, easy cleanGpuUsed, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, easy showAnything, easy showAnything, PainterAudioCut, VAELoader, VAELoader, KSamplerAdvanced, PainterAV2V, AudioEncoderEncode, easy showAnything, Qwen3_VQA, VHS_SelectFilename, Any To Any, HunyuanVideoFoley, easy cleanGpuUsed, easy cleanGpuUsed, Reroute, DF_Get_image_size, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed, VHS_VideoCombine, SaveAudio, SaveAudio, GetVideoComponents, VHS_VideoCombine, CR Prompt Text, RunningHub_VoxCPM_LoadModel, CR Prompt Text, LoadAudio, AudioCombine, Audio Add Silence, ACE_AudioCrop, SaveAudio, easy showAnything, easy showAnything, easy showAnything, easy showAnything, MathExpression|pysssss, Float, CLIPTextEncode, LoadImage, LoadImage, JWInteger, Note, Note, RHLLMChatNode, LoadImage, Text, StringReplace, StringReplace, easy showAnything, VHS_VideoCombine, CR Prompt Text, CR Prompt Text, easy cleanGpuUsed, CR Prompt Text, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, BerniniPromptEnhancer, BatchImagesNode, ImageResizeKJv2, SaveVideo, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, RunningHub_VoxCPM_Generate, KSamplerAdvanced, KSamplerAdvanced, BerniniConditioning]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/（4步加速版-多参版）Seedance2.0完美平替！Bernini全自动音画同全模态图生视频V3_2073466408666746882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073466408666746882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `EmptyAudio`
- `AudioAdjustVolume`
- `AdjustAudio`
- `CLIPLoader`
- `ConditioningZeroOut`
- `AudioEncoderLoader`
- `ModelPatchLoader`
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `easy showAnything`
- `PainterAudioCut`
- `VAELoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `PainterAV2V`
- `AudioEncoderEncode`
- `easy showAnything`
- `Qwen3_VQA`
- `VHS_SelectFilename`
- `Any To Any`
- `HunyuanVideoFoley`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Reroute`
- `DF_Get_image_size`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `SaveAudio`
- `SaveAudio`
- `GetVideoComponents`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `RunningHub_VoxCPM_LoadModel`
- `CR Prompt Text`
- `LoadAudio`
- `AudioCombine`
- `Audio Add Silence`
- `ACE_AudioCrop`
- `SaveAudio`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `Float`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `Note`
- `Note`
- `RHLLMChatNode`
- `LoadImage`
- `Text`
- `StringReplace`
- `StringReplace`
- `easy showAnything`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `CR Prompt Text`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `BerniniPromptEnhancer`
- `BatchImagesNode`
- `ImageResizeKJv2`
- `SaveVideo`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RunningHub_VoxCPM_Generate`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `BerniniConditioning`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（81/93）

**有卡**：`VAEDecode`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`CreateVideo`、`EmptyAudio`、`AudioAdjustVolume`、`AdjustAudio`、`ConditioningZeroOut`、`AudioEncoderLoader`、`ModelPatchLoader`、`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`PainterAudioCut`、`VAELoader`、`KSamplerAdvanced`、`PainterAV2V`、`AudioEncoderEncode`、`Qwen3_VQA`、`VHS_SelectFilename`、`Any To Any`、`HunyuanVideoFoley`、`DF_Get_image_size`、`VHS_VideoCombine`、`SaveAudio`、`GetVideoComponents`、`CR Prompt Text`、`RunningHub_VoxCPM_LoadModel`、`LoadAudio`、`AudioCombine`、`Audio Add Silence`、`ACE_AudioCrop`、`MathExpression|pysssss`、`Float`、`LoadImage`、`JWInteger`、`RHLLMChatNode`、`Text`、`StringReplace`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`BerniniPromptEnhancer`、`BatchImagesNode`、`SaveVideo`、`RunningHub_VoxCPM_Generate`、`BerniniConditioning`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
