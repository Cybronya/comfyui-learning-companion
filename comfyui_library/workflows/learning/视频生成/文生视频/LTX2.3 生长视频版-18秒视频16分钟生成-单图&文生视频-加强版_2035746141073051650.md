---
key: 视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json
name: LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json
hash: 0e71f5cf7960077d
coverage: 0.485437
learned_at: 2026-10-15 22:45:01
nodes: [GetNode, SetNode, SamplerCustomAdvanced, GetNode, CFGGuider, GetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, SetNode, SetNode, ManualSigmas, GetNode, LTXVAudioVAEDecode, GetNode, ManualSigmas, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVConditioning, GetNode, SetNode, GetNode, GetNode, GetNode, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, SetNode, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, LTXVPreprocess, GetNode, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, GetNode, KSamplerSelect, RandomNoise, GetNode, PathchSageAttentionKJ, GetNode, GetNode, GetNode, GetNode, GetNode, Note, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, SetNode, Note, MathExpression|pysssss, MathExpression|pysssss, PrimitiveInt, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, EmptyLTXVLatentVideo, VAELoaderKJ, CLIPTextEncode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, GetNode, LTXVCropGuides, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVLatentUpsampler, RandomNoise, DualCLIPLoader, UNETLoader, easy cleanGpuUsed, SetNode, GetNode, llama_cpp_model_loader, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, llama_cpp_instruct_adv, CLIPTextEncode, LoadImage, ShowText|pysssss, LTX2_NAG, CR Text, PrimitiveInt, GetNode, WujiCleaner, VHS_VideoCombine, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（103 个）：
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `SetNode`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `SetNode`
- `LatentUpscaleModelLoader`
- `LTXVPreprocess`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `PrimitiveBoolean`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `llama_cpp_model_loader`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ShowText|pysssss`
- `LTX2_NAG`
- `CR Text`
- `PrimitiveInt`
- `GetNode`
- `WujiCleaner`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **49%**（50/103）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`RandomNoise`、`PathchSageAttentionKJ`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`DualCLIPLoader`、`UNETLoader`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LoadImage`、`LTX2_NAG`、`CR Text`、`WujiCleaner`、`VHS_VideoCombine`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
