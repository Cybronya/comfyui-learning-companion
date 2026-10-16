---
key: 视频生成/图生视频/NB➕LTX 2.3_2043280274267574273.json
name: NB➕LTX 2.3_2043280274267574273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043280274267574273.json
hash: 83847831741e21f7
coverage: 0.901408
learned_at: 2026-10-15 22:36:31
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, VAELoader, VAELoaderKJ, DualCLIPLoader, KSamplerSelect, CFGGuider, ManualSigmas, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVLatentUpsampler, PrimitiveInt, CreateVideo, Reroute, LatentUpscaleModelLoader, LTXVImgToVideoInplace, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, llama_cpp_unload_model, LayerUtility: PurgeVRAM V2, ResizeImagesByLongerEdge, LTXVConcatAVLatent, LTXVImgToVideoInplace, ComfyMathExpression, UNETLoader, LTX2_NAG, TextInput_, LTXVPreprocess, EmptyLTXVLatentVideo, TextInput_, PrimitiveBoolean, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVChunkFeedForward, ComfyMathExpression, ComfyMathExpression, JoinStrings, ShowText|pysssss, LoadImage, LoadImage, LoadImage, LoadImage, SimpleCalculatorKJ, LTXVEmptyLatentAudio, llama_cpp_model_loader, LoadImage, llama_cpp_parameters, ResizeImageMaskNode, SaveVideo, Bjornulf_LoopBasicBatch, llama_cpp_instruct_adv, MinNode, INTConstant, PrimitiveInt, PrimitiveInt, RH_Nano_Banana2_Gemini31Flash, SaveImage, CR Text, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/NB➕LTX 2.3_2043280274267574273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043280274267574273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVLatentUpsampler` ★核心
- `PrimitiveInt`
- `CreateVideo`
- `Reroute`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `llama_cpp_unload_model`
- `LayerUtility: PurgeVRAM V2`
- `ResizeImagesByLongerEdge`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `LTX2_NAG`
- `TextInput_`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `TextInput_`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `JoinStrings`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SimpleCalculatorKJ`
- `LTXVEmptyLatentAudio` ★核心
- `llama_cpp_model_loader`
- `LoadImage`
- `llama_cpp_parameters`
- `ResizeImageMaskNode`
- `SaveVideo`
- `Bjornulf_LoopBasicBatch`
- `llama_cpp_instruct_adv`
- `MinNode`
- `INTConstant`
- `PrimitiveInt`
- `PrimitiveInt`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `CR Text`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（64/71）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`VAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`CreateVideo`、`LatentUpscaleModelLoader`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`CLIPTextEncode`、`LTXVConditioning`、`llama_cpp_unload_model`、`LayerUtility: PurgeVRAM V2`、`ResizeImagesByLongerEdge`、`ComfyMathExpression`、`UNETLoader`、`LTX2_NAG`、`TextInput_`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`JoinStrings`、`LoadImage`、`SimpleCalculatorKJ`、`LTXVEmptyLatentAudio`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ResizeImageMaskNode`、`SaveVideo`、`Bjornulf_LoopBasicBatch`、`llama_cpp_instruct_adv`、`MinNode`、`INTConstant`、`RH_Nano_Banana2_Gemini31Flash`、`SaveImage`、`CR Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
