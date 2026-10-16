---
key: 视频生成/图生视频/LTX2.3-MSR全能参考V2角色多视图_多分镜多图参考支持参考自定义音色手动_全自动提示词Prompt Relay高动态场景无字幕-优化2_1897896006842044417.json
name: LTX2.3-MSR全能参考V2角色多视图_多分镜多图参考支持参考自定义音色手动_全自动提示词Prompt Relay高动态场景无字幕-优化2_1897896006842044417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1897896006842044417.json
hash: 1a9164d8271dfe5c
coverage: 0.409574
learned_at: 2026-10-15 22:29:19
nodes: [SetNode, PathchSageAttentionKJ, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, CheckpointLoaderSimple, SetNode, SetNode, SetNode, easy convertAnything, SetNode, SetNode, MathExpression|pysssss, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, SetNode, GetNode, GetNode, ComfySwitchNode, SetNode, SetNode, SetNode, SetNode, SetNode, KSamplerSelect, BasicScheduler, VisualizeSigmasKJ, GetNode, GetNode, SetNode, GetNode, ImageConcatMulti, SetNode, LayerUtility: PurgeVRAM V2, SetNode, SetNode, TextSplitByDelimiterEnhanced, SetNode, GetNode, GetNode, easy anythingIndexSwitch, SetNode, GetNode, DualCLIPLoader, GetNode, easy anythingIndexSwitch, LTXVAudioVAEEncode, SolidMask, GetNode, LoadImage, GetNode, GetNode, easy int, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, ComfySwitchNode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVCropGuides, GetNode, SamplerCustom, GetNode, LTXVConditioning, LTX2_NAG, LoadImage, GetNode, GetNode, MelBandRoFormerSampler, NormalizeAudioLoudness, MelBandRoFormerModelLoader, GetNode, LTXAddVideoICLoRAGuide, SetNode, GetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, VHS_VideoCombine, SetNode, ImageConcatMulti, GetNode, LayerUtility: ImageScaleByAspectRatio V2, Note, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, SetNode, easy int, TextSplitByDelimiterEnhanced, easy int, GetNode, GetNode, Qwen3_VQA_Plus, easy seed, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, PrimitiveStringMultiline, BatchImagesNode, PrimitiveStringMultiline, VHS_VideoCombine, easy showAnything, SetNode, EmptyLTXVLatentVideo, GetNode, Textbox, CLIPTextEncode, CLIPTextEncode, LoadAudio, GetNode, SetLatentNoiseMask, LoadAudio, easy imageSize, easy int, PreviewAudio, GetNode, GetNode, easy int, PrimitiveBoolean, LTXICLoRALoaderModelOnly, ModelPatchTorchSettings, SetNode, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, VHS_VideoCombine, MarkdownNote, GetNode, LTXVReferenceAudio, LiconMSR, PromptRelayEncode, SetNode, VAEDecodeTiled, GetNode, GetNode, ShowText|pysssss, ShowText|pysssss, SetNode, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ShowText|pysssss, LoraLoaderModelOnly, PrimitiveStringMultiline, SetNode, SetNode, GetNode, GetNode, MarkdownNote, MarkdownNote, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, Dapao_LlamaChat, easy int]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 241}
---

# 视频生成/图生视频/LTX2.3-MSR全能参考V2角色多视图_多分镜多图参考支持参考自定义音色手动_全自动提示词Prompt Relay高动态场景无字幕-优化2_1897896006842044417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1897896006842044417.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（188 个）：
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `TextSplitByDelimiterEnhanced`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy anythingIndexSwitch`
- `SetNode`
- `GetNode`
- `DualCLIPLoader`
- `GetNode`
- `easy anythingIndexSwitch`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `easy int`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `ComfySwitchNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `SamplerCustom` ★核心
- `GetNode`
- `LTXVConditioning`
- `LTX2_NAG`
- `LoadImage`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `NormalizeAudioLoudness`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `SetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `easy int`
- `TextSplitByDelimiterEnhanced`
- `easy int`
- `GetNode`
- `GetNode`
- `Qwen3_VQA_Plus`
- `easy seed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `BatchImagesNode`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `easy showAnything`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `Textbox`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `GetNode`
- `SetLatentNoiseMask`
- `LoadAudio`
- `easy imageSize`
- `easy int`
- `PreviewAudio`
- `GetNode`
- `GetNode`
- `easy int`
- `PrimitiveBoolean`
- `LTXICLoRALoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `SetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `MarkdownNote`
- `GetNode`
- `LTXVReferenceAudio`
- `LiconMSR`
- `PromptRelayEncode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SetNode`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `Dapao_LlamaChat`
- `easy int`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **41%**（77/188）

**有卡**：`PathchSageAttentionKJ`、`VAELoaderKJ`、`CheckpointLoaderSimple`、`easy convertAnything`、`MathExpression|pysssss`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`BasicScheduler`、`VisualizeSigmasKJ`、`ImageConcatMulti`、`LayerUtility: PurgeVRAM V2`、`TextSplitByDelimiterEnhanced`、`easy anythingIndexSwitch`、`DualCLIPLoader`、`LTXVAudioVAEEncode`、`SolidMask`、`LoadImage`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`SamplerCustom`、`LTXVConditioning`、`LTX2_NAG`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`MelBandRoFormerModelLoader`、`LTXAddVideoICLoRAGuide`、`VHS_VideoCombine`、`Qwen3_VQA_Plus`、`easy seed`、`BatchImagesNode`、`EmptyLTXVLatentVideo`、`Textbox`、`CLIPTextEncode`、`LoadAudio`、`SetLatentNoiseMask`、`easy imageSize`、`PreviewAudio`、`PrimitiveBoolean`、`LTXICLoRALoaderModelOnly`、`ModelPatchTorchSettings`、`LTXVReferenceAudio`、`LiconMSR`、`PromptRelayEncode`、`VAEDecodeTiled`、`RHHiddenNodes`、`LoraLoaderModelOnly`、`Dapao_LlamaChat`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、easy seed
