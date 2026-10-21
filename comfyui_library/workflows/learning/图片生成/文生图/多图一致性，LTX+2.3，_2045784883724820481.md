---
key: 图片生成/文生图/多图一致性，LTX+2.3，_2045784883724820481.json
name: 多图一致性，LTX+2.3，_2045784883724820481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/多图一致性，LTX+2.3，_2045784883724820481.json
hash: 6b3d6f335d8e0fb6
coverage: 0.948718
learned_at: 2026-10-21 02:59:45
nodes: [ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImageMaskNode, LoadImage, ResizeImagesByLongerEdge, LoadImage, LTXAVTextEncoderLoader, LTXVAudioVAELoader, ResizeImageMaskNode, ResizeImageMaskNode, LTX2_NAG, LTXVSeparateAVLatent, LTXVConcatAVLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, CreateVideo, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVPreprocess, SimpleMath+, ImageFromBatch+, llama_cpp_model_loader, llama_cpp_parameters, LTXVCropGuides, LTXVLatentUpsampler, CheckpointLoaderSimple, llama_cpp_instruct_adv, LTXVPreprocess, PrimitiveInt, PrimitiveInt, LTXVAddGuideMulti, LTXVPreprocess, LTXVPreprocess, ShowText|pysssss, ImageBatchMulti, SaveVideo, ResizeImagesByLongerEdge, LTXVPreprocess, CR Text, ResizeImageMaskNode, ResizeImageMaskNode, CLIPTextEncode, ComfyMathExpression, CLIPTextEncode, LTXVConditioning, LoadImage, LoadImage, ResizeImagesByLongerEdge, LoadImage, CR Text, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, CFGGuider, SamplerCustom, CFGGuider, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustom, CR Text Concatenate, CR Text, CR Text, LTXVEmptyLatentAudio, ManualSigmas, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplaceKJ, Bjornulf_ShowInt, EmptyLTXVLatentVideo, INTConstant, PrimitiveInt, SimpleMath+, SimpleCalculatorKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 25, "width": 97}
---

# 图片生成/文生图/多图一致性，LTX+2.3，_2045784883724820481.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/多图一致性，LTX+2.3，_2045784883724820481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTX2_NAG`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `SimpleMath+`
- `ImageFromBatch+`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `llama_cpp_instruct_adv`
- `LTXVPreprocess`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVAddGuideMulti`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ShowText|pysssss`
- `ImageBatchMulti`
- `SaveVideo`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `CR Text`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LoadImage`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `CR Text`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `SamplerCustom` ★核心
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustom` ★核心
- `CR Text Concatenate`
- `CR Text`
- `CR Text`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplaceKJ`
- `Bjornulf_ShowInt`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `PrimitiveInt`
- `SimpleMath+`
- `SimpleCalculatorKJ`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（74/78）

**有卡**：`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`LoadImage`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LTX2_NAG`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVPreprocess`、`SimpleMath+`、`ImageFromBatch+`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`CheckpointLoaderSimple`、`llama_cpp_instruct_adv`、`LTXVAddGuideMulti`、`ImageBatchMulti`、`SaveVideo`、`CR Text`、`CLIPTextEncode`、`ComfyMathExpression`、`LTXVConditioning`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CFGGuider`、`SamplerCustom`、`ManualSigmas`、`CR Text Concatenate`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplaceKJ`、`Bjornulf_ShowInt`、`EmptyLTXVLatentVideo`、`INTConstant`、`SimpleCalculatorKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、SamplerCustom
