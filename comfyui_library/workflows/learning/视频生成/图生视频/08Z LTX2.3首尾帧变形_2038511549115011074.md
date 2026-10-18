---
key: 视频生成/图生视频/08Z LTX2.3首尾帧变形_2038511549115011074.json
name: 08Z LTX2.3首尾帧变形_2038511549115011074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/08Z LTX2.3首尾帧变形_2038511549115011074.json
hash: 253ffcf9811fde42
coverage: 0.703448
learned_at: 2026-10-15 22:36:03
nodes: [LTXVConcatAVLatent, CFGGuider, LTXVConditioning, LTXVLatentUpsampler, LatentUpscaleModelLoader, VAELoaderKJ, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, KSamplerSelect, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, SetNode, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, ImageResizeKJv2, PrimitiveBoolean, SetNode, SetNode, ComfyMathExpression, LTXVConcatAVLatent, SimpleMath+, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetNode, ShowText|pysssss, VAEDecodeTiled, SetNode, SetNode, LTXVAudioVAEDecode, PrimitiveInt, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ResizeImageMaskNode, LTXVCropGuides, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, LTXVPreprocess, SamplerCustomAdvanced, LTX2_NAG, LTXVAddGuideMulti, SimpleMath+, GetNode, GetNode, UNETLoader, Any To Any, Any To Any, Any To Any, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, Any To Any, PrimitiveBoolean, ZML_SwitchOutput, Any To Any, PrimitiveInt, TT_img_enc_v2, ZML_SwitchOutput, DuckHideNode, Any To Any, GetNode, GetNode, VHS_VideoCombine, PrimitiveInt, ComfyMathExpression, GetNode, GetNode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, VHS_VideoCombine, SimpleMath+, llama_cpp_parameters, llama_cpp_model_loader, Note, Switch string [Crystools], llama_cpp_instruct_adv, easy saveText, easy showAnything, Switch string [Crystools], Text Concatenate, Note, CR Prompt Text, PrimitiveBoolean, CR Text, CR Text, Text Concatenate, CR Prompt Text, ImpactSwitch, ZML_SwitchOutput, CR Text Replace, IntToString, easy showAnything, CR Text, ImpactSwitch, ImageResizeKJv2, ImageResizeKJv2, Text Multiline, CR Text, ImpactSwitch, SetNode, Any To Any, LayerUtility: PurgeVRAM, easy positive, AILab_QwenVL_Advanced, Image Stitch, ImageScaleDownToSize, DualCLIPLoader, VAELoaderKJ, ImageBatch, PreviewImage, ManualSigmas, PrimitiveInt, PrimitiveInt, LayerUtility: BooleanOperator, LayerUtility: If , PreviewTextNode, PrimitiveBoolean, PreviewAny, CR Prompt Text, Fast Groups Bypasser (rgthree), CR Text, CR Text, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/08Z LTX2.3首尾帧变形_2038511549115011074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038511549115011074.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（145 个）：
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVConditioning`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `PrimitiveBoolean`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `ShowText|pysssss`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImageMaskNode`
- `LTXVCropGuides`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `LTX2_NAG`
- `LTXVAddGuideMulti`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `Any To Any`
- `Any To Any`
- `Any To Any`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Any To Any`
- `PrimitiveBoolean`
- `ZML_SwitchOutput`
- `Any To Any`
- `PrimitiveInt`
- `TT_img_enc_v2`
- `ZML_SwitchOutput`
- `DuckHideNode`
- `Any To Any`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `VHS_VideoCombine`
- `SimpleMath+`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Note`
- `Switch string [Crystools]`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `easy showAnything`
- `Switch string [Crystools]`
- `Text Concatenate`
- `Note`
- `CR Prompt Text`
- `PrimitiveBoolean`
- `CR Text`
- `CR Text`
- `Text Concatenate`
- `CR Prompt Text`
- `ImpactSwitch`
- `ZML_SwitchOutput`
- `CR Text Replace`
- `IntToString`
- `easy showAnything`
- `CR Text`
- `ImpactSwitch`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Text Multiline`
- `CR Text`
- `ImpactSwitch`
- `SetNode`
- `Any To Any`
- `LayerUtility: PurgeVRAM`
- `easy positive`
- `AILab_QwenVL_Advanced`
- `Image Stitch`
- `ImageScaleDownToSize`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `ImageBatch`
- `PreviewImage`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveInt`
- `LayerUtility: BooleanOperator`
- `LayerUtility: If `
- `PreviewTextNode`
- `PrimitiveBoolean`
- `PreviewAny`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `CR Text`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（102/145）

**有卡**：`LTXVConcatAVLatent`、`CFGGuider`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`ComfyMathExpression`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`PrimitiveBoolean`、`SimpleMath+`、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ResizeImageMaskNode`、`LTXVCropGuides`、`CLIPTextEncode`、`LTXVPreprocess`、`LTX2_NAG`、`LTXVAddGuideMulti`、`UNETLoader`、`Any To Any`、`SaveImage`、`ZML_SwitchOutput`、`TT_img_enc_v2`、`DuckHideNode`、`VHS_VideoCombine`、`ResizeImagesByLongerEdge`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`Switch string [Crystools]`、`llama_cpp_instruct_adv`、`easy saveText`、`Text Concatenate`、`CR Prompt Text`、`CR Text`、`CR Text Replace`、`IntToString`、`Text Multiline`、`LayerUtility: PurgeVRAM`、`easy positive`、`AILab_QwenVL_Advanced`、`Image Stitch`、`ImageScaleDownToSize`、`DualCLIPLoader`、`ImageBatch`、`LayerUtility: BooleanOperator`、`LayerUtility: If `、`PreviewTextNode`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、SaveImage、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
