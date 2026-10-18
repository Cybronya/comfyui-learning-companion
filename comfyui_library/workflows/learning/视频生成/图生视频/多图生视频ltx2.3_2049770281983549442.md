---
key: 视频生成/图生视频/多图生视频ltx2.3_2049770281983549442.json
name: 多图生视频ltx2.3_2049770281983549442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多图生视频ltx2.3_2049770281983549442.json
hash: 18413c15c45e351a
coverage: 0.949367
learned_at: 2026-10-15 22:37:16
nodes: [ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImageMaskNode, LoadImage, ResizeImagesByLongerEdge, LoadImage, LTXAVTextEncoderLoader, LTXVAudioVAELoader, ResizeImageMaskNode, ResizeImageMaskNode, LTXVSeparateAVLatent, LTXVConcatAVLatent, LatentUpscaleModelLoader, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVPreprocess, SimpleMath+, llama_cpp_model_loader, LTXVCropGuides, LTXVLatentUpsampler, llama_cpp_instruct_adv, LTXVPreprocess, PrimitiveInt, PrimitiveInt, LTXVAddGuideMulti, LTXVPreprocess, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImageMaskNode, ResizeImageMaskNode, ComfyMathExpression, CLIPTextEncode, LTXVConditioning, LoadImage, ResizeImagesByLongerEdge, RandomNoise, SamplerCustomAdvanced, CFGGuider, SamplerCustom, CFGGuider, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustom, CR Text Concatenate, CR Text, LTXVEmptyLatentAudio, ManualSigmas, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplaceKJ, Bjornulf_ShowInt, EmptyLTXVLatentVideo, INTConstant, SimpleMath+, SimpleCalculatorKJ, PrimitiveInt, LoadImage, llama_cpp_parameters, LTX2_NAG, CheckpointLoaderSimple, LoraLoaderModelOnly, ImageBatchMulti, CLIPTextEncode, CR Text, CR Text, ImageFromBatch+, LTXVAudioVAEDecode, CreateVideo, SaveImage, TT_img_enc_v2, KSamplerSelect, LoraLoaderModelOnly, LoadImage, ShowText|pysssss, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/多图生视频ltx2.3_2049770281983549442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049770281983549442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
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
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `SimpleMath+`
- `llama_cpp_model_loader`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `llama_cpp_instruct_adv`
- `LTXVPreprocess`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVAddGuideMulti`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `RandomNoise`
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
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplaceKJ`
- `Bjornulf_ShowInt`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `SimpleMath+`
- `SimpleCalculatorKJ`
- `PrimitiveInt`
- `LoadImage`
- `llama_cpp_parameters`
- `LTX2_NAG`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageBatchMulti`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CR Text`
- `ImageFromBatch+`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveImage`
- `TT_img_enc_v2`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ShowText|pysssss`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **95%**（75/79）

**有卡**：`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`LoadImage`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`LTXVPreprocess`、`SimpleMath+`、`llama_cpp_model_loader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`llama_cpp_instruct_adv`、`LTXVAddGuideMulti`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`SamplerCustomAdvanced`、`CFGGuider`、`SamplerCustom`、`KSamplerSelect`、`ManualSigmas`、`CR Text Concatenate`、`CR Text`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplaceKJ`、`Bjornulf_ShowInt`、`EmptyLTXVLatentVideo`、`INTConstant`、`SimpleCalculatorKJ`、`llama_cpp_parameters`、`LTX2_NAG`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`ImageBatchMulti`、`ImageFromBatch+`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveImage`、`TT_img_enc_v2`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、SamplerCustom
