---
key: 视频生成/图生视频/【九镜联动】Z-image一致性+Gemini3反推九图故事分镜-Wan2.2 视频+FlashVSRt放大自用_1997586587758301186.json
name: 【九镜联动】Z-image一致性+Gemini3反推九图故事分镜-Wan2.2 视频+FlashVSRt放大自用_1997586587758301186.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1997586587758301186.json
hash: f6dcced7227db076
coverage: 0.792952
learned_at: 2026-10-15 22:33:30
nodes: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, SetNode, CLIPLoader, UNETLoader, UNETLoader, ModelSamplingSD3, PathchSageAttentionKJ, easy cleanGpuUsed, wanBlockSwap, VAELoader, GetImageRangeFromBatch, WanFirstMiddleLastFrameToVideo, GetNode, GetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, wanBlockSwap, VAEDecode, ColorMatch, ColorMatch, UNETLoader, LoraLoaderModelOnly, CLIPLoader, GetNode, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, VAELoader, Int, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, UNETLoader, PathchSageAttentionKJ, CLIPLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, ColorMatch, KSamplerAdvanced, VAEDecode, GetImageSize, VHS_VideoCombine, VAEDecode, easy batchAnything, Reroute, Reroute, SeedVR2ExtraArgs, Note, Note, ImageScaleToTotalPixels, easy showAnything, TextInput_, GetNode, TextInput_, JoinStrings, GetNode, easy showAnything, TextInput_, GetNode, WanFirstMiddleLastFrameToVideo, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, JoinStrings, GetNode, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, MuyeTextEditOutput, MuyeTextEditOutput, ShowText|pysssss, ShowText|pysssss, ImageConcatMulti, ImageConcatMulti, JWInteger, CR Prompt Text, MuyeTextEditOutput, ProcessString, ShowText|pysssss, ShellAgentPluginOutputText, Text Concatenate, RH_Captioner_Pro, RH_LLMAPI_NODE, Qwen3_VQA, easy showAnything, RH_Captioner_Pro, Qwen3_VQA, JoinStrings, ShowText|pysssss, RH_LLMAPI_NODE, RH_LLMAPI_NODE, RH_Captioner_Pro, ImageBatchSplitter //Inspire, Qwen3_VQA, MuyeTextEditOutput, MuyeTextEditOutput, LoraLoaderModelOnly, CR Text, Note, easy batchAnything, ImageUpscaleWithModel, VHS_VideoCombine, KSampler, LoadImage, CLIPLoader, VAELoader, UNETLoader, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, ConditioningZeroOut, CLIPTextEncode, JDCN_StringToList, LayerUtility: PurgeVRAM, ProcessString, easy showAnything, Seed (rgthree), easy showAnything, CR Text, Text Concatenate, easy showAnything, RH_Captioner_Pro, RH_LLMAPI_NODE, easy showAnything, PreviewImage, VHS_Unbatch, VAEEncode, PreviewImage, VAEDecode, VAEDecode, Int, LayerUtility: ImageScaleByAspectRatio V2, easy imageListToImageBatch, FlashVSRNode, Qwen3VL_Chat, MuyeTextEditOutput, MuyeTextEditOutput, ImageConcatMulti, Qwen3VL_Chat, MuyeTextEditOutput, MuyeTextEditOutput, ImageConcatMulti, Qwen3VL_Chat, ImageConcatMulti, Qwen3VL_Chat, easy showAnything, RH_LLMAPI_NODE, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy showAnything, Note, MuyeTextEditOutput, MuyeTextEditOutput, JjkText, easy promptLine, CR Text, RH_LLMAPI_NODE, easy showAnything, SeedVR2GGUF, PreviewImage, SaveImage, VHS_VideoCombine, ImageUpscaleWithModel, UpscaleModelLoader, ImageUpscaleWithModel, UpscaleModelLoader, VHS_VideoCombine, SeedVR2BlockSwap, SeedVR2, VHS_VideoCombine, VHS_VideoCombine, GetNode, WanFirstMiddleLastFrameToVideo, CR Text, KSamplerAdvanced, LayerUtility: PurgeVRAM, ImpactConditionalBranch, ImpactInt, CR Text Replace, CR Text, CR Prompt Text, CR Prompt Text, ImpactConditionalBranch, ImpactConditionalBranch, wanBlockSwap, wanBlockSwap, LoraLoaderModelOnly, CR Text, CR Text, VHS_VideoCombine, ImpactInt, ImpactConditionalBranch, ImpactConditionalBranch, CR Text, CR Text, ModelPatchTorchSettings, easy cleanGpuUsed, ModelPatchTorchSettings, ModelSamplingSD3, ImpactConditionalBranch, ImpactConditionalBranch, LoadImage, LoadImage, EmptyLatentImage, SDXLEmptyLatentSizePicker+, Note, UpscaleModelLoader, easy boolean, CR Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, Note, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 0, "cfg": 8, "denoise": "beta57", "height": 1, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed", "width": "768x1280 (0.6)"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/【九镜联动】Z-image一致性+Gemini3反推九图故事分镜-Wan2.2 视频+FlashVSRt放大自用_1997586587758301186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997586587758301186.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（227 个）：
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `wanBlockSwap`
- `VAELoader`
- `GetImageRangeFromBatch`
- `WanFirstMiddleLastFrameToVideo`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `VAEDecode` ★核心
- `ColorMatch`
- `ColorMatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `VAELoader`
- `Int`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `ColorMatch`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `easy batchAnything`
- `Reroute`
- `Reroute`
- `SeedVR2ExtraArgs`
- `Note`
- `Note`
- `ImageScaleToTotalPixels`
- `easy showAnything`
- `TextInput_`
- `GetNode`
- `TextInput_`
- `JoinStrings`
- `GetNode`
- `easy showAnything`
- `TextInput_`
- `GetNode`
- `WanFirstMiddleLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JoinStrings`
- `GetNode`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `JWInteger`
- `CR Prompt Text`
- `MuyeTextEditOutput`
- `ProcessString`
- `ShowText|pysssss`
- `ShellAgentPluginOutputText`
- `Text Concatenate`
- `RH_Captioner_Pro`
- `RH_LLMAPI_NODE`
- `Qwen3_VQA`
- `easy showAnything`
- `RH_Captioner_Pro`
- `Qwen3_VQA`
- `JoinStrings`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `RH_Captioner_Pro`
- `ImageBatchSplitter //Inspire`
- `Qwen3_VQA`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `Note`
- `easy batchAnything`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `JDCN_StringToList`
- `LayerUtility: PurgeVRAM`
- `ProcessString`
- `easy showAnything`
- `Seed (rgthree)`
- `easy showAnything`
- `CR Text`
- `Text Concatenate`
- `easy showAnything`
- `RH_Captioner_Pro`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `PreviewImage`
- `VHS_Unbatch`
- `VAEEncode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageListToImageBatch`
- `FlashVSRNode`
- `Qwen3VL_Chat`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `ImageConcatMulti`
- `Qwen3VL_Chat`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `ImageConcatMulti`
- `Qwen3VL_Chat`
- `ImageConcatMulti`
- `Qwen3VL_Chat`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `Note`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `JjkText`
- `easy promptLine`
- `CR Text`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `SeedVR2GGUF`
- `PreviewImage`
- `SaveImage`
- `VHS_VideoCombine`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `WanFirstMiddleLastFrameToVideo`
- `CR Text`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `ImpactConditionalBranch`
- `ImpactInt`
- `CR Text Replace`
- `CR Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `ImpactConditionalBranch`
- `ImpactConditionalBranch`
- `wanBlockSwap`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `CR Text`
- `VHS_VideoCombine`
- `ImpactInt`
- `ImpactConditionalBranch`
- `ImpactConditionalBranch`
- `CR Text`
- `CR Text`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ImpactConditionalBranch`
- `ImpactConditionalBranch`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `Note`
- `UpscaleModelLoader`
- `easy boolean`
- `CR Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `Note`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `beta57`
- `width` = `768x1280 (0.6)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **79%**（180/227）

**有卡**：`LayerUtility: PurgeVRAM`、`CLIPLoader`、`UNETLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`wanBlockSwap`、`VAELoader`、`GetImageRangeFromBatch`、`WanFirstMiddleLastFrameToVideo`、`LoraLoaderModelOnly`、`VAEDecode`、`ColorMatch`、`Int`、`TextEncodeQwenImageEditPlus`、`KSamplerAdvanced`、`GetImageSize`、`VHS_VideoCombine`、`easy batchAnything`、`SeedVR2ExtraArgs`、`ImageScaleToTotalPixels`、`TextInput_`、`JoinStrings`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`MuyeTextEditOutput`、`ImageConcatMulti`、`JWInteger`、`CR Prompt Text`、`ProcessString`、`ShellAgentPluginOutputText`、`Text Concatenate`、`RH_Captioner_Pro`、`RH_LLMAPI_NODE`、`Qwen3_VQA`、`ImageBatchSplitter //Inspire`、`CR Text`、`ImageUpscaleWithModel`、`KSampler`、`LoadImage`、`ConditioningZeroOut`、`JDCN_StringToList`、`Seed (rgthree)`、`VHS_Unbatch`、`VAEEncode`、`easy imageListToImageBatch`、`FlashVSRNode`、`Qwen3VL_Chat`、`easy promptLine`、`SeedVR2GGUF`、`SaveImage`、`UpscaleModelLoader`、`SeedVR2BlockSwap`、`SeedVR2`、`ImpactConditionalBranch`、`ImpactInt`、`CR Text Replace`、`ModelPatchTorchSettings`、`EmptyLatentImage`、`SDXLEmptyLatentSizePicker+`、`easy boolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
