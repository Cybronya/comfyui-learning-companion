---
key: 视频生成/文生视频/ltx2.3换头工作流_2043178251316633601.json
name: ltx2.3换头工作流_2043178251316633601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3换头工作流_2043178251316633601.json
hash: e5f6079a8afbccd2
coverage: 0.706522
learned_at: 2026-10-15 22:47:23
nodes: [VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, SetNode, LatentUpscaleModelLoader, SetNode, KSamplerSelect, RandomNoise, LTXVConcatAVLatent, SetLatentNoiseMask, GetNode, KSamplerSelect, RandomNoise, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveFloat, SimpleMath+, SetNode, SetNode, SetNode, CLIPTextEncode, easy showAnything, SolidMask, BasicScheduler, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVCropGuides, BasicScheduler, GetNode, GetNode, GetNode, LTXVConditioning, LTXVAddGuideMulti, CFGGuider, LTXVCropGuides, GetImageSize, LTXVAddGuideMulti, GetNode, GetNode, VAEEncode, LTXVPreprocess, SetNode, ImageScaleBy, SetNode, FaceAnalysisModels, FaceSegmentation, ImageCropByMask, easy cleanGpuUsed, LTXVSeparateAVLatent, LTXVAudioVAEEncode, Int, ImageResizeKJv2, LoadImage, ReservedRegionFrameComposer, LTXVLatentUpsampler, LTXVSeparateAVLatent, GetNode, FlashVSRInitPipe, CreateVideo, GetNode, VAEDecodeTiled, CreateVideo, GetNode, LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, ImageConcanate, LoraLoaderModelOnly, FlashVSRNodeAdv, VHS_VideoCombine, FlashVSRInitPipe, SaveImage, INPAINT_ExpandMask, AILab_QwenVL, VHS_LoadVideo, FlashVSRNodeAdv, CLIPTextEncode, SamplerCustomAdvanced, CFGGuider, GetNode, GetNode, UNETLoader, SetNode, easy showAnything, LoraLoaderModelOnly, LoraLoader, GetNode, VHS_VideoCombine, 1hew_SaveVideo]
patterns: [lora]
missing: []
parameters: {"lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/文生视频/ltx2.3换头工作流_2043178251316633601.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3换头工作流_2043178251316633601.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `SolidMask`
- `BasicScheduler`
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `LTXVAddGuideMulti`
- `CFGGuider`
- `LTXVCropGuides`
- `GetImageSize`
- `LTXVAddGuideMulti`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `LTXVPreprocess`
- `SetNode`
- `ImageScaleBy`
- `SetNode`
- `FaceAnalysisModels`
- `FaceSegmentation`
- `ImageCropByMask`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `Int`
- `ImageResizeKJv2`
- `LoadImage`
- `ReservedRegionFrameComposer`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `FlashVSRInitPipe`
- `CreateVideo`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `FlashVSRNodeAdv`
- `VHS_VideoCombine`
- `FlashVSRInitPipe`
- `SaveImage`
- `INPAINT_ExpandMask`
- `AILab_QwenVL`
- `VHS_LoadVideo`
- `FlashVSRNodeAdv`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LoraLoader` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `1hew_SaveVideo`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **71%**（65/92）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LoraLoaderModelOnly`、`SimpleMath+`、`CLIPTextEncode`、`SolidMask`、`BasicScheduler`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVConditioning`、`LTXVAddGuideMulti`、`CFGGuider`、`GetImageSize`、`VAEEncode`、`LTXVPreprocess`、`ImageScaleBy`、`FaceAnalysisModels`、`FaceSegmentation`、`ImageCropByMask`、`easy cleanGpuUsed`、`LTXVSeparateAVLatent`、`LTXVAudioVAEEncode`、`Int`、`ImageResizeKJv2`、`LoadImage`、`ReservedRegionFrameComposer`、`LTXVLatentUpsampler`、`FlashVSRInitPipe`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ImageConcanate`、`FlashVSRNodeAdv`、`VHS_VideoCombine`、`SaveImage`、`INPAINT_ExpandMask`、`AILab_QwenVL`、`VHS_LoadVideo`、`UNETLoader`、`LoraLoader`、`1hew_SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
