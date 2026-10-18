---
key: 视频生成/图生视频/LTX2.3全新参考表生视频_2067478623367553025.json
name: LTX2.3全新参考表生视频_2067478623367553025.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3全新参考表生视频_2067478623367553025.json
hash: 23870efcd21201af
coverage: 0.825
learned_at: 2026-10-15 22:40:02
nodes: [SetNode, SetNode, CLIPTextEncode, PrimitiveInt, VAELoaderKJ, VAELoader, VisualizeSigmasKJ, ConditioningZeroOut, KSamplerSelect, BasicScheduler, GetNode, GetNode, GetNode, SimpleMath+, DualCLIPLoader, LTXVPreprocess, ModelSamplingSD3, SamplerCustom, LTXVCropGuides, LTXVSeparateAVLatent, VAELoaderKJ, LTXVConditioning, GetNode, LTXAddVideoICLoRAGuide, PathchSageAttentionKJ, LTX2_NAG, LTXVConcatAVLatent, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, PrimitiveNode, easy cleanGpuUsed, TextEncodeQwenImageEditPlus, EmptyLatentImage, easy indexAnything, easy indexAnything, easy indexAnything, ImpactImageBatchToImageList, ImageStitch, easy indexAnything, ImageStitch, VAEDecode, CLIPLoader, llama_cpp_parameters, ImpactImageBatchToImageList, CLIPTextEncode, SetNode, GetNode, ImageBatchMulti, CR Text Concatenate, llama_cpp_model_loader, ImageStitch, GetNode, ImageStitch, KSampler, VAEDecode, LTXVAudioVAEDecode, DF_Int_to_Float, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, ImageBatchMulti, CR Text List To String, TTResolutionSelector, LTX2SamplingPreviewOverride, Int, ImageResizeKJv2, EmptyLTXVLatentVideo, VHS_VideoCombine, LTXVEmptyLatentAudio, PreviewImage, SetNode, llama_cpp_instruct_adv, easy positive]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 24, "sampler_name": "euler", "scheduler": "simple", "seed": 819296905694526, "steps": 4, "width": 305}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3全新参考表生视频_2067478623367553025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067478623367553025.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `VAELoaderKJ`
- `VAELoader`
- `VisualizeSigmasKJ`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `DualCLIPLoader`
- `LTXVPreprocess`
- `ModelSamplingSD3`
- `SamplerCustom` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `LTXVConditioning`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `PathchSageAttentionKJ`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveNode`
- `easy cleanGpuUsed`
- `TextEncodeQwenImageEditPlus`
- `EmptyLatentImage` ★核心
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `ImpactImageBatchToImageList`
- `ImageStitch`
- `easy indexAnything`
- `ImageStitch`
- `VAEDecode` ★核心
- `CLIPLoader`
- `llama_cpp_parameters`
- `ImpactImageBatchToImageList`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `ImageBatchMulti`
- `CR Text Concatenate`
- `llama_cpp_model_loader`
- `ImageStitch`
- `GetNode`
- `ImageStitch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `DF_Int_to_Float`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `ImageBatchMulti`
- `CR Text List To String`
- `TTResolutionSelector`
- `LTX2SamplingPreviewOverride`
- `Int`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `LTXVEmptyLatentAudio` ★核心
- `PreviewImage`
- `SetNode`
- `llama_cpp_instruct_adv`
- `easy positive`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`
- `seed` = `819296905694526`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（66/80）

**有卡**：`CLIPTextEncode`、`VAELoaderKJ`、`VAELoader`、`VisualizeSigmasKJ`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`SimpleMath+`、`DualCLIPLoader`、`LTXVPreprocess`、`ModelSamplingSD3`、`SamplerCustom`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`PathchSageAttentionKJ`、`LTX2_NAG`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`TextEncodeQwenImageEditPlus`、`EmptyLatentImage`、`easy indexAnything`、`ImpactImageBatchToImageList`、`ImageStitch`、`VAEDecode`、`CLIPLoader`、`llama_cpp_parameters`、`ImageBatchMulti`、`CR Text Concatenate`、`llama_cpp_model_loader`、`KSampler`、`LTXVAudioVAEDecode`、`DF_Int_to_Float`、`UNETLoader`、`LoadImage`、`CR Text List To String`、`TTResolutionSelector`、`LTX2SamplingPreviewOverride`、`Int`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`LTXVEmptyLatentAudio`、`llama_cpp_instruct_adv`、`easy positive`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
