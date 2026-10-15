---
key: 视频生成/图生视频/最新LTX2.3+Gemma4本地自动化运行_2052786138674409473.json
name: 最新LTX2.3+Gemma4本地自动化运行_2052786138674409473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新LTX2.3+Gemma4本地自动化运行_2052786138674409473.json
hash: e8d1e18fec988bea
coverage: 0.777778
learned_at: 2026-10-15 22:43:03
nodes: [SetNode, VisualizeSigmasKJ, VAELoaderKJ, SetNode, RegexExtract, RegexExtract, LTXVConcatAVLatent, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, DualCLIPLoader, LTXVImgToVideoInplaceKJ, LTXVPreprocess, GetNode, BasicScheduler, LTXVEmptyLatentAudio, VAELoaderKJ, KSamplerSelect, LTXVConditioning, LTX2SamplingPreviewOverride, SamplerCustom, PreviewImage, ConditioningZeroOut, LTXVAudioVAEDecode, LayerUtility: PurgeVRAM V2, PreviewAny, PreviewAny, JWInteger, Reroute, FlashVSR_SM_KSampler, GetImageRangeFromBatch, LayerUtility: PurgeVRAM V2, StringReplace, GetImageSize, EmptyLTXVLatentVideo, FlashVSR_SM_Model, JWInteger, VAEDecode, easy mathInt, LayerUtility: ImageScaleByAspectRatio V2, PromptRelayEncode, UNETLoader, LoraLoaderModelOnly, VHS_VideoCombine, Text, PreviewAny, PathchSageAttentionKJ, LoadImage, PreviewImage, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": "randomize", "denoise": 11, "height": 25, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 2056010111, "width": 489}
---

# 视频生成/图生视频/最新LTX2.3+Gemma4本地自动化运行_2052786138674409473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/最新LTX2.3+Gemma4本地自动化运行_2052786138674409473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
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

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `1280`
- `steps` = `2056010111`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **78%**（42/54）

**有卡**：`VisualizeSigmasKJ`、`VAELoaderKJ`、`RegexExtract`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`DualCLIPLoader`、`LTXVImgToVideoInplaceKJ`、`LTXVPreprocess`、`BasicScheduler`、`LTXVEmptyLatentAudio`、`KSamplerSelect`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`SamplerCustom`、`ConditioningZeroOut`、`LTXVAudioVAEDecode`、`LayerUtility: PurgeVRAM V2`、`JWInteger`、`FlashVSR_SM_KSampler`、`GetImageRangeFromBatch`、`StringReplace`、`GetImageSize`、`EmptyLTXVLatentVideo`、`FlashVSR_SM_Model`、`VAEDecode`、`easy mathInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`PromptRelayEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`Text`、`PathchSageAttentionKJ`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、FlashVSR_SM_KSampler、SamplerCustom
