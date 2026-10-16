---
key: 视频生成/图生视频/LTX2.3-i2v-kijai-三段式采样-细节更丰富-自动提示词_2040449259794866177.json
name: LTX2.3-i2v-kijai-三段式采样-细节更丰富-自动提示词_2040449259794866177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2040449259794866177.json
hash: 1f9ded158137baa9
coverage: 0.558559
learned_at: 2026-10-15 22:36:15
nodes: [RandomNoise, KSamplerSelect, ManualSigmas, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, LTXVPreprocess, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, SetNode, MarkdownNote, MarkdownNote, SetNode, GetNode, GetNode, LTXVConditioning, GetNode, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ResizeImagesByLongerEdge, GetNode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, GetNode, LoraLoader, SetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, UNETLoader, ImageResizeKJv2, LTXVImgToVideoInplace, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVLatentUpsampler, llama_cpp_parameters, SimpleMath+, SetNode, SimpleMath+, SimpleMath+, Int, TTResolutionSelector, PreviewImage, llama_cpp_model_loader, SetNode, Int, GetNode, easy showAnything, llama_cpp_instruct_adv, PrimitiveStringMultiline, CLIPTextEncode, VHS_VideoCombine, ComfyMathExpression, GetNode, CustomAddLabel, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, LoadImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 25, "lora_name": "gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/图生视频/LTX2.3-i2v-kijai-三段式采样-细节更丰富-自动提示词_2040449259794866177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040449259794866177.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `LoraLoader` ★核心
- `SetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `llama_cpp_parameters`
- `SimpleMath+`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `Int`
- `TTResolutionSelector`
- `PreviewImage`
- `llama_cpp_model_loader`
- `SetNode`
- `Int`
- `GetNode`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `GetNode`
- `CustomAddLabel`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **56%**（62/111）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`CFGGuider`、`CLIPTextEncode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`ResizeImagesByLongerEdge`、`LTXVEmptyLatentAudio`、`LoraLoader`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`llama_cpp_parameters`、`SimpleMath+`、`Int`、`TTResolutionSelector`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`VHS_VideoCombine`、`CustomAddLabel`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
