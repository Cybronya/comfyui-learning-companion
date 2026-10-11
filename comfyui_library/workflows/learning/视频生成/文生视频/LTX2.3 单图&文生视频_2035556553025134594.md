---
key: 视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json
name: LTX2.3 单图&文生视频_2035556553025134594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json
hash: e889dbbc0605b103
coverage: 0.411765
learned_at: 2026-10-11 03:48:35
nodes: [GetNode, SetNode, SamplerCustomAdvanced, GetNode, CFGGuider, GetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, SetNode, SetNode, ManualSigmas, GetNode, LTXVAudioVAEDecode, GetNode, ManualSigmas, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVConditioning, GetNode, SetNode, GetNode, GetNode, GetNode, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, SetNode, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, LTXVPreprocess, GetNode, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, GetNode, KSamplerSelect, RandomNoise, GetNode, PathchSageAttentionKJ, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, Note, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, SetNode, Note, MathExpression|pysssss, MathExpression|pysssss, PrimitiveInt, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, EmptyLTXVLatentVideo, VAELoaderKJ, CLIPTextEncode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, GetNode, LTXVCropGuides, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVLatentUpsampler, RandomNoise, DualCLIPLoader, UNETLoader, easy cleanGpuUsed, LTX2_NAG, GetNode, SetNode, GetNode, PrimitiveInt, ShowText|pysssss, LoadImage, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, PrimitiveInt, PrimitiveInt, llama_cpp_model_loader, CR Text, llama_cpp_instruct_adv]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（102 个）：
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
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
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
- `LTX2_NAG`
- `GetNode`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `ShowText|pysssss`
- `LoadImage`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PrimitiveInt`
- `PrimitiveInt`
- `llama_cpp_model_loader`
- `CR Text`
- `llama_cpp_instruct_adv`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **41%**（42/102）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`RandomNoise`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`CLIPTextEncode`、`PrimitiveBoolean`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`DualCLIPLoader`、`UNETLoader`、`LTX2_NAG`、`LoadImage`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`

**缺卡**（7）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
