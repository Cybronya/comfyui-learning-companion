---
key: 视频生成/图生视频/多图一致性，LTX+2.3+首中尾三图+多图参考，顺滑转场，符合物理逻辑，强引导参考，_2044285849671569409.json
name: 多图一致性，LTX+2.3+首中尾三图+多图参考，顺滑转场，符合物理逻辑，强引导参考，_2044285849671569409.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多图一致性，LTX+2.3+首中尾三图+多图参考，顺滑转场，符合物理逻辑，强引导参考，_2044285849671569409.json
hash: 5db5267ac24fc4dc
coverage: 0.943662
learned_at: 2026-10-15 22:36:36
nodes: [ManualSigmas, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, CLIPTextEncode, LoadImage, ResizeImagesByLongerEdge, LoadImage, LTXVPreprocess, CLIPTextEncode, ComfyMathExpression, LTXAVTextEncoderLoader, LTXVAudioVAELoader, CFGGuider, ResizeImageMaskNode, ResizeImageMaskNode, ImageBatchMulti, LTXVConditioning, LTX2_NAG, RandomNoise, CFGGuider, CR Text, CR Text Concatenate, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVConcatAVLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, ShowText|pysssss, ManualSigmas, KSamplerSelect, KSamplerSelect, ComfyMathExpression, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, CreateVideo, PrimitiveInt, ComfyMathExpression, VAEDecodeTiled, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, SimpleCalculatorKJ, LTXVPreprocess, SimpleMath+, SaveVideo, ImageFromBatch+, PrimitiveInt, PrimitiveInt, LoadImage, llama_cpp_model_loader, llama_cpp_parameters, EmptyLTXVLatentVideo, LTXVImgToVideoInplaceKJ, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, LTXVAddGuideMulti, CheckpointLoaderSimple, llama_cpp_instruct_adv, INTConstant, ResizeImagesByLongerEdge, LoadImage, ResizeImageMaskNode, LoadImage, ResizeImageMaskNode, ResizeImageMaskNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/多图一致性，LTX+2.3+首中尾三图+多图参考，顺滑转场，符合物理逻辑，强引导参考，_2044285849671569409.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044285849671569409.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `ManualSigmas`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `CFGGuider`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ImageBatchMulti`
- `LTXVConditioning`
- `LTX2_NAG`
- `RandomNoise`
- `CFGGuider`
- `CR Text`
- `CR Text Concatenate`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `PrimitiveInt`
- `ComfyMathExpression`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SimpleCalculatorKJ`
- `LTXVPreprocess`
- `SimpleMath+`
- `SaveVideo`
- `ImageFromBatch+`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplaceKJ`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`
- `CheckpointLoaderSimple` ★核心
- `llama_cpp_instruct_adv`
- `INTConstant`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `ResizeImageMaskNode`
- `LoadImage`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **94%**（67/71）

**有卡**：`ManualSigmas`、`ResizeImagesByLongerEdge`、`CLIPTextEncode`、`LoadImage`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CFGGuider`、`ResizeImageMaskNode`、`ImageBatchMulti`、`LTXVConditioning`、`LTX2_NAG`、`RandomNoise`、`CR Text`、`CR Text Concatenate`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SimpleCalculatorKJ`、`SimpleMath+`、`SaveVideo`、`ImageFromBatch+`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAddGuideMulti`、`CheckpointLoaderSimple`、`llama_cpp_instruct_adv`、`INTConstant`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
