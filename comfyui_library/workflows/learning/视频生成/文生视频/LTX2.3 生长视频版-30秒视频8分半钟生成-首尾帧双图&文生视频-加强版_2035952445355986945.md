---
key: 视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json
name: LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json
hash: cbf64790c29d877d
coverage: 0.504425
learned_at: 2026-10-15 22:45:01
nodes: [GetNode, SetNode, SamplerCustomAdvanced, CFGGuider, GetNode, GetNode, GetNode, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, SetNode, ManualSigmas, GetNode, LTXVAudioVAEDecode, GetNode, easy cleanGpuUsed, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, GetNode, SetNode, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, UNETLoader, SetNode, VAELoaderKJ, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, GetNode, LTXVEmptyLatentAudio, KSamplerSelect, RandomNoise, GetNode, PathchSageAttentionKJ, RandomNoise, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveBoolean, GetNode, SetNode, SetNode, LTXVPreprocess, LTXVPreprocess, MathExpression|pysssss, MathExpression|pysssss, SetNode, SetNode, LTXVConcatAVLatent, SetNode, GetNode, Note, SetNode, PrimitiveInt, PrimitiveInt, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, VHS_VideoCombine, ComfyMathExpression, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, LTXVCropGuides, LTXVImgToVideoInplaceKJ, DualCLIPLoader, PrimitiveInt, easy cleanGpuUsed, WujiCleaner, SetNode, WujiCleaner, SetNode, LTXVConditioning, Note, SetNode, SetNode, EmptyLTXVLatentVideo, LoadImage, LoadImage, GetNode, GetNode, easy imageConcat, LTX2_NAG, ComfyMathExpression, PrimitiveInt, PrimitiveInt, GetNode, WujiCleaner, LTXVConcatAVLatent, WujiCleaner, llama_cpp_instruct_adv, easy cleanGpuUsed, ShowText|pysssss, CLIPTextEncode, GetNode, CLIPTextEncode, GetNode, CR Text, llama_cpp_model_loader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（113 个）：
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoaderKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `SetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetNode`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `Note`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVImgToVideoInplaceKJ`
- `DualCLIPLoader`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `WujiCleaner`
- `SetNode`
- `WujiCleaner`
- `SetNode`
- `LTXVConditioning`
- `Note`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `easy imageConcat`
- `LTX2_NAG`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetNode`
- `WujiCleaner`
- `LTXVConcatAVLatent`
- `WujiCleaner`
- `llama_cpp_instruct_adv`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CR Text`
- `llama_cpp_model_loader`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（57/113）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`easy cleanGpuUsed`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`RandomNoise`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`LTXVPreprocess`、`MathExpression|pysssss`、`LTXVConcatAVLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`ComfyMathExpression`、`LTXVCropGuides`、`LTXVImgToVideoInplaceKJ`、`DualCLIPLoader`、`WujiCleaner`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LoadImage`、`easy imageConcat`、`LTX2_NAG`、`llama_cpp_instruct_adv`、`CLIPTextEncode`、`CR Text`、`llama_cpp_model_loader`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
