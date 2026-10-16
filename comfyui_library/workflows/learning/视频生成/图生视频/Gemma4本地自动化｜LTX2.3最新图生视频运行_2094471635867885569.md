---
key: 视频生成/图生视频/Gemma4本地自动化｜LTX2.3最新图生视频运行_2094471635867885569.json
name: Gemma4本地自动化｜LTX2.3最新图生视频运行_2094471635867885569
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Gemma4本地自动化｜LTX2.3最新图生视频运行_2094471635867885569.json
hash: fdd7c31a15fbc6ff
coverage: 0.802469
learned_at: 2026-10-17 00:02:07
nodes: [SetNode, VisualizeSigmasKJ, VAELoaderKJ, SetNode, RegexExtract, RegexExtract, LTXVConcatAVLatent, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, DualCLIPLoader, LTXVImgToVideoInplaceKJ, LTXVPreprocess, GetNode, BasicScheduler, LTXVEmptyLatentAudio, VAELoaderKJ, KSamplerSelect, LTXVConditioning, LTX2SamplingPreviewOverride, SamplerCustom, PreviewImage, ConditioningZeroOut, LTXVAudioVAEDecode, LayerUtility: PurgeVRAM V2, PreviewAny, PreviewAny, JWInteger, Reroute, FlashVSR_SM_KSampler, GetImageRangeFromBatch, LayerUtility: PurgeVRAM V2, StringReplace, GetImageSize, EmptyLTXVLatentVideo, FlashVSR_SM_Model, JWInteger, VAEDecode, easy mathInt, LayerUtility: ImageScaleByAspectRatio V2, PromptRelayEncode, UNETLoader, LoraLoaderModelOnly, VHS_VideoCombine, Text, PreviewAny, PathchSageAttentionKJ, LoadImage, PreviewImage, Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Gemma4本地自动化｜LTX2.3最新图生视频运行_2094471635867885569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Gemma4本地自动化｜LTX2.3最新图生视频运行_2094471635867885569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `SetNode`
- `VisualizeSigmasKJ`
- `VAELoaderKJ`
- `SetNode`
- `RegexExtract`
- `RegexExtract`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `DualCLIPLoader`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `GetNode`
- `BasicScheduler`
- `LTXVEmptyLatentAudio` ★核心
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `SamplerCustom` ★核心
- `PreviewImage`
- `ConditioningZeroOut`
- `LTXVAudioVAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewAny`
- `PreviewAny`
- `JWInteger`
- `Reroute`
- `FlashVSR_SM_KSampler` ★核心
- `GetImageRangeFromBatch`
- `LayerUtility: PurgeVRAM V2`
- `StringReplace`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `FlashVSR_SM_Model`
- `JWInteger`
- `VAEDecode` ★核心
- `easy mathInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PromptRelayEncode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `Text`
- `PreviewAny`
- `PathchSageAttentionKJ`
- `LoadImage`
- `PreviewImage`
- `Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **80%**（65/81）

**有卡**：`VisualizeSigmasKJ`、`VAELoaderKJ`、`RegexExtract`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`DualCLIPLoader`、`LTXVImgToVideoInplaceKJ`、`LTXVPreprocess`、`BasicScheduler`、`LTXVEmptyLatentAudio`、`KSamplerSelect`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`SamplerCustom`、`ConditioningZeroOut`、`LTXVAudioVAEDecode`、`LayerUtility: PurgeVRAM V2`、`JWInteger`、`FlashVSR_SM_KSampler`、`GetImageRangeFromBatch`、`StringReplace`、`GetImageSize`、`EmptyLTXVLatentVideo`、`FlashVSR_SM_Model`、`VAEDecode`、`easy mathInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`PromptRelayEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`Text`、`PathchSageAttentionKJ`、`LoadImage`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
