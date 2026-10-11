---
key: 视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json
name: LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json
hash: 7493c489e0552ea1
coverage: 0.419355
learned_at: 2026-10-11 03:48:35
nodes: [GetNode, SetNode, SetNode, CFGGuider, GetNode, GetNode, GetNode, LTXVLatentUpsampler, SetNode, ManualSigmas, GetNode, LTXVAudioVAEDecode, GetNode, easy cleanGpuUsed, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, GetNode, SetNode, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, UNETLoader, SetNode, VAELoaderKJ, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, GetNode, KSamplerSelect, RandomNoise, GetNode, PathchSageAttentionKJ, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveBoolean, SetNode, SetNode, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, MathExpression|pysssss, MathExpression|pysssss, SetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, Note, SetNode, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, SetNode, GetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, ComfyMathExpression, VHS_VideoCombine, SetNode, Note, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, LTXVImgToVideoInplaceKJ, DualCLIPLoader, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, LoadImage, WujiCleaner, LTX2_NAG, SetNode, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, LTXVImgToVideoInplace, GetNode, WujiCleaner, WujiCleaner, SamplerCustomAdvanced, LTXVEmptyLatentAudio, WujiCleaner, GetNode, LTXVConditioning, GetNode, llama_cpp_instruct_adv, WujiCleaner, GetNode, GetNode, GetNode, GetNode, easy imageConcat, easy imageConcat, llama_cpp_model_loader, Note, easy cleanGpuUsed, CLIPTextEncode, SetNode, SamplerCustomAdvanced, PrimitiveInt, ShowText|pysssss, CLIPTextEncode, CR Text]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, easy imageConcat, easy imageConcat]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（124 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `easy cleanGpuUsed`
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
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `DualCLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WujiCleaner`
- `LTX2_NAG`
- `SetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `GetNode`
- `WujiCleaner`
- `WujiCleaner`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `WujiCleaner`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `llama_cpp_instruct_adv`
- `WujiCleaner`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy imageConcat`
- `easy imageConcat`
- `llama_cpp_model_loader`
- `Note`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **42%**（52/124）

**有卡**：`CFGGuider`、`LTXVLatentUpsampler`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LatentUpscaleModelLoader`、`KSamplerSelect`、`RandomNoise`、`PathchSageAttentionKJ`、`PrimitiveBoolean`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`VHS_VideoCombine`、`LTXVCropGuides`、`LTXVImgToVideoInplaceKJ`、`DualCLIPLoader`、`LoadImage`、`WujiCleaner`、`LTX2_NAG`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`CLIPTextEncode`

**缺卡**（10）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageConcat`、`easy imageConcat`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
