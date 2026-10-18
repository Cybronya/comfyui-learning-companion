---
key: 视频生成/图生视频/LTX2.3-电商带货-上传图片自动生成-音画同步-Distilled-1.1-蒸馏稳定版_2052289650873651201.json
name: LTX2.3-电商带货-上传图片自动生成-音画同步-Distilled-1.1-蒸馏稳定版_2052289650873651201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-电商带货-上传图片自动生成-音画同步-Distilled-1.1-蒸馏稳定版_2052289650873651201.json
hash: 99c81d401e0dc4c8
coverage: 0.830189
learned_at: 2026-10-15 22:37:28
nodes: [LTX2SamplingPreviewOverride, GetNode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, SetNode, SetNode, CLIPTextEncode, llama_cpp_parameters, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, easy cleanGpuUsed, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, UNETLoader, LTX2_NAG, PathchSageAttentionKJ, ConditioningZeroOut, CLIPTextEncode, GetNode, TTResolutionSelector, Int, CustomAddLabel, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, EmptyLTXVLatentVideo, ModelSamplingSD3, SimpleMath+, BasicScheduler, LTXVPreprocess, DF_Int_to_Float, GetNode, LTXVConcatAVLatent, LTXVAudioVAEDecode, KSamplerSelect, VAEDecode, SamplerCustom, Int, llama_cpp_model_loader, easy positive, SetNode, ShowText|pysssss, LTXVSeparateAVLatent, LTXVImgToVideoInplaceKJ, GetNode, easy showAnything, llama_cpp_instruct_adv, Text, SeedGeneratorMira]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3-电商带货-上传图片自动生成-音画同步-Distilled-1.1-蒸馏稳定版_2052289650873651201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052289650873651201.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `VAELoader`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `llama_cpp_parameters`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LTX2_NAG`
- `PathchSageAttentionKJ`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `GetNode`
- `TTResolutionSelector`
- `Int`
- `CustomAddLabel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `ModelSamplingSD3`
- `SimpleMath+`
- `BasicScheduler`
- `LTXVPreprocess`
- `DF_Int_to_Float`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `Int`
- `llama_cpp_model_loader`
- `easy positive`
- `SetNode`
- `ShowText|pysssss`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `Text`
- `SeedGeneratorMira`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（44/53）

**有卡**：`LTX2SamplingPreviewOverride`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`llama_cpp_parameters`、`LoadImage`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`LTX2_NAG`、`PathchSageAttentionKJ`、`ConditioningZeroOut`、`TTResolutionSelector`、`Int`、`CustomAddLabel`、`VHS_VideoCombine`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`ModelSamplingSD3`、`SimpleMath+`、`BasicScheduler`、`LTXVPreprocess`、`DF_Int_to_Float`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`VAEDecode`、`SamplerCustom`、`llama_cpp_model_loader`、`easy positive`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplaceKJ`、`llama_cpp_instruct_adv`、`Text`、`SeedGeneratorMira`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect
