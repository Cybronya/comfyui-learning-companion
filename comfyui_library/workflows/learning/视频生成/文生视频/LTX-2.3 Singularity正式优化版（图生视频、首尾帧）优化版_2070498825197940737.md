---
key: 视频生成/文生视频/LTX-2.3 Singularity正式优化版（图生视频、首尾帧）优化版_2070498825197940737.json
name: LTX-2.3 Singularity正式优化版（图生视频、首尾帧）优化版_2070498825197940737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3 Singularity正式优化版（图生视频、首尾帧）优化版_2070498825197940737.json
hash: d07b8e503f27374f
coverage: 0.9375
learned_at: 2026-10-15 22:44:38
nodes: [LTXVConcatAVLatent, KSamplerSelect, CFGGuider, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVAudioVAEDecode, LTXVConditioning, VAEDecode, LTXVEmptyLatentAudio, SimpleMath+, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, easy imageSize, EmptyLTXVLatentVideo, LTXVPreprocess, EmptyImage, easy mathInt, MarkdownNote, Fast Groups Muter (rgthree), CLIPTextEncode, LTXVAudioVAEDecode, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, CLIPTextEncode, ManualSigmas, ImageScaleBy, LTXVImgToVideoInplace, ManualSigmas, Note, DualCLIPLoader, LoadImage, easy int, easy int, RandomNoise, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ, VAELoaderKJ, LTXVSeparateAVLatent, VAEDecode, VHS_VideoCombine, ShowText|pysssss, SamplerCustomAdvanced, LTXVSeparateAVLatent, LoraLoaderBlockWeight //Inspire, LoraLoaderBlockWeight //Inspire, LoraLoaderBlockWeight //Inspire, LoraLoaderBlockWeight //Inspire, LoraLoaderBlockWeight //Inspire, LoraLoaderBlockWeight //Inspire, LoraLoaderBlockWeight //Inspire, LoraLoaderBlockWeight //Inspire, LoraLoaderBlockWeight //Inspire, CR Prompt Text, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, LatentUpscaleModelLoader, CR Prompt Text, UNETLoader, PathchSageAttentionKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "lora_name": "All", "strength_clip": 1, "strength_model": "LTX 2.3 - Pixar CGI Toon Style().safetensors", "width": 361}
---

# 视频生成/文生视频/LTX-2.3 Singularity正式优化版（图生视频、首尾帧）优化版_2070498825197940737.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3 Singularity正式优化版（图生视频、首尾帧）优化版_2070498825197940737.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（64 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `VAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `easy imageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `easy imageSize`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `EmptyImage`
- `easy mathInt`
- `MarkdownNote`
- `Fast Groups Muter (rgthree)`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `ImageScaleBy`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `Note`
- `DualCLIPLoader`
- `LoadImage`
- `easy int`
- `easy int`
- `RandomNoise`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LoraLoaderBlockWeight //Inspire` ★核心
- `LoraLoaderBlockWeight //Inspire` ★核心
- `LoraLoaderBlockWeight //Inspire` ★核心
- `LoraLoaderBlockWeight //Inspire` ★核心
- `LoraLoaderBlockWeight //Inspire` ★核心
- `LoraLoaderBlockWeight //Inspire` ★核心
- `LoraLoaderBlockWeight //Inspire` ★核心
- `LoraLoaderBlockWeight //Inspire` ★核心
- `LoraLoaderBlockWeight //Inspire` ★核心
- `CR Prompt Text`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `LatentUpscaleModelLoader`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`
- `lora_name` = `All`
- `strength_model` = `LTX 2.3 - Pixar CGI Toon Style().safetensors`
- `strength_clip` = `1`

## 知识

覆盖率 **94%**（60/64）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`VAEDecode`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`easy imageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`EmptyImage`、`easy mathInt`、`CLIPTextEncode`、`ManualSigmas`、`ImageScaleBy`、`DualCLIPLoader`、`LoadImage`、`easy int`、`RandomNoise`、`SamplerCustomAdvanced`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`LoraLoaderBlockWeight //Inspire`、`CR Prompt Text`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LatentUpscaleModelLoader`、`UNETLoader`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、LoraLoaderBlockWeight //Inspire、CFGGuider、KSamplerSelect
