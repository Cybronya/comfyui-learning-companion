---
key: 视频生成/图生视频/LTX2.3图生视频【优化版】切镜头_2073281072584212480.json
name: LTX2.3图生视频【优化版】切镜头_2073281072584212480.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073281072584212480.json
hash: c9f3dc0e5a2d81d2
coverage: 0.554878
learned_at: 2026-10-15 22:41:02
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyImage, LTXVConcatAVLatent, GetNode, GetNode, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, easy cleanGpuUsed, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, ImageScaleBy, SetNode, SetNode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, GetNode, RandomNoise, GetNode, SetNode, easy cleanGpuUsed, Any To String (mtb), GetNode, GetNode, SetNode, PrimitiveInt, Int, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, CR Text, Display Any (rgthree), easy convertAnything, SetNode, SetNode, easy cleanGpuUsed, LTXVSeparateAVLatent, SetNode, GetNode, CR Text, SetNode, SetNode, GetNode, CFGGuider, GetNode, CLIPTextEncode, llama_cpp_instruct_adv, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, ManualSigmas, SetNode, SetNode, CLIPTextEncode, CR Text, llama_cpp_model_loader, GetNode, GetNode, GetNode, GetNode, easy convertAnything, ttN concat, CR Text Concatenate, SetNode, SetNode, easy boolean, CR Text, easy cleanGpuUsed, CFGGuider, LTXVLatentUpsampler, CR Text, CR Value, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, KSamplerSelect, Int, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVAudioVAEDecode, LTXVPreprocess, ManualSigmas, LTXVImgToVideoInplace, ManualSigmas, MathExpression|pysssss, GetImageSize, GetNode, LatentUpscaleModelLoader, ResizeImagesByLongerEdge, ImpactSwitch, VHS_VideoCombine, Fast Groups Muter (rgthree), easy int, GetNode, VAEDecodeTiled, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, ManualSigmas, VAELoaderKJ, LTX2_NAG, LTXVConcatAVLatent, GetNode, BasicScheduler, ManualSigmas, SaveVideo, ShowText|pysssss, DualCLIPLoader, Any To String (mtb), SetNode, LoadImage, CR Text, SetNode, LoraLoaderModelOnly, SetNode, LTXICLoRALoaderModelOnly, GetNode, LTXVChunkFeedForward, LoraLoaderModelOnly, CR Text, CR Text, VAELoaderKJ, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, UNETLoader, ManualSigmas, KSamplerSelect, VAEDecodeTiled, CreateVideo, RTXVideoSuperResolution, GetNode, LTXVImgToVideoInplace, RTXVideoSuperResolution, VRAMReserver, BasicScheduler, LTXVScheduler]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3图生视频【优化版】切镜头_2073281072584212480.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073281072584212480.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（164 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `Int`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Text`
- `Display Any (rgthree)`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `CR Text`
- `SetNode`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CR Text`
- `llama_cpp_model_loader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `ttN concat`
- `CR Text Concatenate`
- `SetNode`
- `SetNode`
- `easy boolean`
- `CR Text`
- `easy cleanGpuUsed`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `CR Text`
- `CR Value`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `Int`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `MathExpression|pysssss`
- `GetImageSize`
- `GetNode`
- `LatentUpscaleModelLoader`
- `ResizeImagesByLongerEdge`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `easy int`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `VAELoaderKJ`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `GetNode`
- `BasicScheduler`
- `ManualSigmas`
- `SaveVideo`
- `ShowText|pysssss`
- `DualCLIPLoader`
- `Any To String (mtb)`
- `SetNode`
- `LoadImage`
- `CR Text`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `GetNode`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `CR Text`
- `VAELoaderKJ`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `UNETLoader` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `RTXVideoSuperResolution`
- `GetNode`
- `LTXVImgToVideoInplace`
- `RTXVideoSuperResolution`
- `VRAMReserver`
- `BasicScheduler`
- `LTXVScheduler`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **55%**（91/164）

**有卡**：`EmptyImage`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`LTXVConditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`RandomNoise`、`Any To String (mtb)`、`Int`、`LTXVEmptyLatentAudio`、`CR Text`、`Display Any (rgthree)`、`easy convertAnything`、`LTXVSeparateAVLatent`、`CFGGuider`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`ManualSigmas`、`llama_cpp_model_loader`、`ttN concat`、`CR Text Concatenate`、`easy boolean`、`LTXVLatentUpsampler`、`CR Value`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`MathExpression|pysssss`、`GetImageSize`、`LatentUpscaleModelLoader`、`ResizeImagesByLongerEdge`、`VHS_VideoCombine`、`easy int`、`VAEDecodeTiled`、`VAELoaderKJ`、`LTX2_NAG`、`BasicScheduler`、`SaveVideo`、`DualCLIPLoader`、`LoadImage`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTXVChunkFeedForward`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`UNETLoader`、`CreateVideo`、`RTXVideoSuperResolution`、`VRAMReserver`、`LTXVScheduler`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
