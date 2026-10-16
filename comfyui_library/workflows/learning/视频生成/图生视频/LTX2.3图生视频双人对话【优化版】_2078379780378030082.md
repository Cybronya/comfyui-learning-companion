---
key: 视频生成/图生视频/LTX2.3图生视频双人对话【优化版】_2078379780378030082.json
name: LTX2.3图生视频双人对话【优化版】_2078379780378030082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2078379780378030082.json
hash: 524ec3d49c1bca56
coverage: 0.564706
learned_at: 2026-10-15 22:41:51
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyImage, LTXVConcatAVLatent, GetNode, GetNode, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, easy cleanGpuUsed, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, ImageScaleBy, SetNode, SetNode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, GetNode, RandomNoise, GetNode, SetNode, easy cleanGpuUsed, GetNode, GetNode, SetNode, PrimitiveInt, Int, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, CR Text, Display Any (rgthree), SetNode, SetNode, easy cleanGpuUsed, LTXVSeparateAVLatent, SetNode, GetNode, CR Text, SetNode, SetNode, GetNode, CFGGuider, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, SetNode, SetNode, ManualSigmas, SetNode, SetNode, CLIPTextEncode, CR Text, GetNode, GetNode, easy convertAnything, ttN concat, CR Text Concatenate, SetNode, easy boolean, easy cleanGpuUsed, CFGGuider, LTXVLatentUpsampler, CR Text, CR Value, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, KSamplerSelect, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVAudioVAEDecode, LTXVPreprocess, ManualSigmas, LTXVImgToVideoInplace, MathExpression|pysssss, GetImageSize, GetNode, ResizeImagesByLongerEdge, ImpactSwitch, VHS_VideoCombine, Fast Groups Muter (rgthree), GetNode, VAEDecodeTiled, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, LTX2_NAG, LTXVConcatAVLatent, GetNode, ManualSigmas, SetNode, SetNode, LoraLoaderModelOnly, SetNode, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, KSamplerSelect, GetNode, LTXVImgToVideoInplace, VRAMReserver, LTXVScheduler, VAELoaderKJ, DualCLIPLoader, ManualSigmas, GetNode, ManualSigmas, UNETLoader, VAELoaderKJ, CheckpointLoaderSimple, BasicScheduler, easy convertAnything, VAEDecodeTiled, RTXVideoSuperResolution, RTXVideoSuperResolution, CR Text, Any To String (mtb), CheckpointLoaderSimple, ManualSigmas, CR Text, CR Text, CR Text, CR Text, BasicScheduler, CreateVideo, LatentUpscaleModelLoader, GetNode, GetNode, GetNode, RH_LLMAPI_NODE, ShowText|pysssss, SaveVideo, CR Text, CR Text, llama_cpp_model_loader, llama_cpp_instruct_adv, ShowText|pysssss, Any To String (mtb), SetNode, LoadImage, CR Text, easy int, Int]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-23b-distilled-1.1.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3图生视频双人对话【优化版】_2078379780378030082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078379780378030082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（170 个）：
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
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `ttN concat`
- `CR Text Concatenate`
- `SetNode`
- `easy boolean`
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
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `MathExpression|pysssss`
- `GetImageSize`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `GetNode`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `VRAMReserver`
- `LTXVScheduler`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `ManualSigmas`
- `GetNode`
- `ManualSigmas`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `CheckpointLoaderSimple` ★核心
- `BasicScheduler`
- `easy convertAnything`
- `VAEDecodeTiled` ★核心
- `RTXVideoSuperResolution`
- `RTXVideoSuperResolution`
- `CR Text`
- `Any To String (mtb)`
- `CheckpointLoaderSimple` ★核心
- `ManualSigmas`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `BasicScheduler`
- `CreateVideo`
- `LatentUpscaleModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `SaveVideo`
- `CR Text`
- `CR Text`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `Any To String (mtb)`
- `SetNode`
- `LoadImage`
- `CR Text`
- `easy int`
- `Int`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-23b-distilled-1.1.safetensors`

## 知识

覆盖率 **56%**（96/170）

**有卡**：`EmptyImage`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`LTXVConditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`RandomNoise`、`Int`、`LTXVEmptyLatentAudio`、`CR Text`、`Display Any (rgthree)`、`LTXVSeparateAVLatent`、`CFGGuider`、`CLIPTextEncode`、`ManualSigmas`、`easy convertAnything`、`ttN concat`、`CR Text Concatenate`、`easy boolean`、`LTXVLatentUpsampler`、`CR Value`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`MathExpression|pysssss`、`GetImageSize`、`ResizeImagesByLongerEdge`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`VRAMReserver`、`LTXVScheduler`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`CheckpointLoaderSimple`、`BasicScheduler`、`RTXVideoSuperResolution`、`Any To String (mtb)`、`CreateVideo`、`LatentUpscaleModelLoader`、`RH_LLMAPI_NODE`、`SaveVideo`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LoadImage`、`easy int`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
