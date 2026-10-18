---
key: 视频生成/图生视频/(4步加速版)Seedance2.0完美平替！Bernini全自动音画同全模态图生视频V3_2073466718235746306.json
name: (4步加速版)Seedance2.0完美平替！Bernini全自动音画同全模态图生视频V3_2073466718235746306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(4步加速版)Seedance2.0完美平替！Bernini全自动音画同全模态图生视频V3_2073466718235746306.json
hash: b239af60b9146ae9
coverage: 0.853933
learned_at: 2026-10-15 22:41:07
nodes: [VAEDecode, StringReplace, LoraLoaderModelOnly, easy showAnything, CLIPLoader, CLIPTextEncode, Note, Note, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, CR Prompt Text, CR Prompt Text, CreateVideo, EmptyAudio, AudioAdjustVolume, AdjustAudio, CLIPLoader, ConditioningZeroOut, AudioEncoderLoader, ModelPatchLoader, easy cleanGpuUsed, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, easy showAnything, easy showAnything, PainterAudioCut, VHS_VideoCombine, VAELoader, VAELoader, KSamplerAdvanced, PainterAV2V, AudioEncoderEncode, MarkdownNote, easy showAnything, Qwen3_VQA, VHS_SelectFilename, Any To Any, HunyuanVideoFoley, easy cleanGpuUsed, easy cleanGpuUsed, Reroute, DF_Get_image_size, VAEDecode, VHS_VideoCombine, StringReplace, easy cleanGpuUsed, VHS_VideoCombine, SaveAudio, SaveAudio, LayerUtility: ImageScaleByAspectRatio V2, RHLLMChatNode, RHLLMChatNode, BerniniPromptEnhancer, LoadImage, GetVideoComponents, VHS_VideoCombine, CR Prompt Text, RunningHub_VoxCPM_LoadModel, RunningHub_VoxCPM_Generate, CR Prompt Text, LoadAudio, CR Prompt Text, AudioCombine, Audio Add Silence, ACE_AudioCrop, SaveAudio, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, easy showAnything, easy showAnything, easy showAnything, MathExpression|pysssss, Float, CLIPTextEncode, PrimitiveInt, JWInteger, BerniniConditioning, SaveVideo, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": "normal", "sampler_name": 1, "scheduler": "dpmpp_sde", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/(4步加速版)Seedance2.0完美平替！Bernini全自动音画同全模态图生视频V3_2073466718235746306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073466718235746306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
- `VAEDecode` ★核心
- `StringReplace`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
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
- `VHS_VideoCombine`
- `VAELoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `PainterAV2V`
- `AudioEncoderEncode`
- `MarkdownNote`
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
- `StringReplace`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `SaveAudio`
- `SaveAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RHLLMChatNode`
- `RHLLMChatNode`
- `BerniniPromptEnhancer`
- `LoadImage`
- `GetVideoComponents`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `RunningHub_VoxCPM_LoadModel`
- `RunningHub_VoxCPM_Generate`
- `CR Prompt Text`
- `LoadAudio`
- `CR Prompt Text`
- `AudioCombine`
- `Audio Add Silence`
- `ACE_AudioCrop`
- `SaveAudio`
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `Float`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `JWInteger`
- `BerniniConditioning`
- `SaveVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_sde`
- `denoise` = `normal`

## 知识

覆盖率 **85%**（76/89）

**有卡**：`VAEDecode`、`StringReplace`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`CR Prompt Text`、`CreateVideo`、`EmptyAudio`、`AudioAdjustVolume`、`AdjustAudio`、`ConditioningZeroOut`、`AudioEncoderLoader`、`ModelPatchLoader`、`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`UNETLoader`、`PainterAudioCut`、`VHS_VideoCombine`、`VAELoader`、`PainterAV2V`、`AudioEncoderEncode`、`Qwen3_VQA`、`VHS_SelectFilename`、`Any To Any`、`HunyuanVideoFoley`、`DF_Get_image_size`、`SaveAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`RHLLMChatNode`、`BerniniPromptEnhancer`、`LoadImage`、`GetVideoComponents`、`RunningHub_VoxCPM_LoadModel`、`RunningHub_VoxCPM_Generate`、`LoadAudio`、`AudioCombine`、`Audio Add Silence`、`ACE_AudioCrop`、`MathExpression|pysssss`、`Float`、`JWInteger`、`BerniniConditioning`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
