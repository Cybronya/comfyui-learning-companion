---
key: 视频生成/文生视频/Fish-Wan2.2-AIO-首尾帧15秒连续长视频版_1959961684356050946.json
name: Fish-Wan2.2-AIO-首尾帧15秒连续长视频版_1959961684356050946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Fish-Wan2.2-AIO-首尾帧15秒连续长视频版_1959961684356050946.json
hash: 882befcbd6c36c5e
coverage: 0.601695
learned_at: 2026-10-10 22:59:02
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, ShowText|pysssss, CheckpointLoaderSimple, DeepTranslatorTextNode, TorchCompileModel, TorchCompileModelWanVideoV2, TorchCompileModel, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, WanMoeKSampler, TextInput_, workflow>加速节点, workflow>加速节点, CLIPVisionEncode, PreviewImage, StringLength, VHS_PruneOutputs, SimpleMath+, workflow>加速节点, WanImageToVideo, workflow>加速节点, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, WanMoeKSampler, SaveImage, VHS_SplitImages, PrimitiveInt, SimpleMath+, VHS_PruneOutputs, SaveImage, VHS_SelectFilename, StringLength, WanImageToVideo, GetNode, GetNode, GetNode, Int, Int, SetNode, Int, SetNode, GetNode, GetNode, GetNode, workflow>加速节点, workflow>加速节点, Note, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, WanMoeKSampler, VHS_SplitImages, PrimitiveInt, SimpleMath+, VHS_SplitImages, VHS_PruneOutputs, SaveImage, StringLength, GetNode, GetNode, GetNode, VHS_SelectFilename, VHS_SplitImages, VHS_SelectFilename, Note, SimpleMath+, VHS_PruneOutputs, EmptyHunyuanLatentVideo, VAEDecode, CLIPVisionLoader, VAEDecodeTiled, SetNode, WanImageToVideo, CheckpointLoaderSimple, Note, Fast Groups Bypasser (rgthree), SetNode, Int, GetNode, GetNode, GetNode, VAEDecodeTiled, VHS_SplitImages, VAEDecodeTiled, VHS_SplitImages, ImageBatch, PlaySound|pysssss, VHS_GetImageCount, ImageBatch, VHS_LoadVideoPath, VHS_LoadVideoPath, VHS_GetImageCount, VHS_LoadVideoPath, RIFE VFI, Seed Everywhere, WanMoeKSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, VHS_VideoCombine, LoadImage, workflow>Clip Text, workflow>Clip Text, workflow>Clip Text]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss, RIFE VFI, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, workflow>加速节点, workflow>加速节点, workflow>加速节点, workflow>加速节点, workflow>加速节点, workflow>加速节点, Seed Everywhere, workflow>Clip Text, workflow>Clip Text, workflow>Clip Text]
parameters: {"cfg": 4, "checkpoint": "wan2.2-i2v-rapid-aio-nsfw-v9.1.safetensors", "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `workflow>Clip Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `workflow>Clip Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `workflow>Clip Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Fish-Wan2.2-AIO-首尾帧15秒连续长视频版_1959961684356050946.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Fish-Wan2.2-AIO-首尾帧15秒连续长视频版_1959961684356050946.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（118 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `CheckpointLoaderSimple` ★核心
- `DeepTranslatorTextNode`
- `TorchCompileModel`
- `TorchCompileModelWanVideoV2`
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideoV2`
- `WanMoeKSampler` ★核心
- `TextInput_`
- `workflow>加速节点`
- `workflow>加速节点`
- `CLIPVisionEncode`
- `PreviewImage`
- `StringLength`
- `VHS_PruneOutputs`
- `SimpleMath+`
- `workflow>加速节点`
- `WanImageToVideo`
- `workflow>加速节点`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `WanMoeKSampler` ★核心
- `SaveImage`
- `VHS_SplitImages`
- `PrimitiveInt`
- `SimpleMath+`
- `VHS_PruneOutputs`
- `SaveImage`
- `VHS_SelectFilename`
- `StringLength`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `Int`
- `SetNode`
- `Int`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `workflow>加速节点`
- `workflow>加速节点`
- `Note`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `WanMoeKSampler` ★核心
- `VHS_SplitImages`
- `PrimitiveInt`
- `SimpleMath+`
- `VHS_SplitImages`
- `VHS_PruneOutputs`
- `SaveImage`
- `StringLength`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_SelectFilename`
- `VHS_SplitImages`
- `VHS_SelectFilename`
- `Note`
- `SimpleMath+`
- `VHS_PruneOutputs`
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `WanImageToVideo`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `VHS_SplitImages`
- `VAEDecodeTiled` ★核心
- `VHS_SplitImages`
- `ImageBatch`
- `PlaySound|pysssss`
- `VHS_GetImageCount`
- `ImageBatch`
- `VHS_LoadVideoPath`
- `VHS_LoadVideoPath`
- `VHS_GetImageCount`
- `VHS_LoadVideoPath`
- `RIFE VFI`
- `Seed Everywhere`
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `LoadImage`
- `workflow>Clip Text`
- `workflow>Clip Text`
- `workflow>Clip Text`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-nsfw-v9.1.safetensors`
- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **60%**（71/118）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`DeepTranslatorTextNode`、`TorchCompileModel`、`TorchCompileModelWanVideoV2`、`WanMoeKSampler`、`TextInput_`、`CLIPVisionEncode`、`StringLength`、`VHS_PruneOutputs`、`WanImageToVideo`、`SaveImage`、`VHS_SplitImages`、`VHS_SelectFilename`、`Int`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`CLIPVisionLoader`、`VAEDecodeTiled`、`ImageBatch`、`VHS_GetImageCount`、`VHS_LoadVideoPath`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LoadImage`

**缺卡**（19）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`PlaySound|pysssss`、`RIFE VFI`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`workflow>加速节点`、`workflow>加速节点`、`workflow>加速节点`、`workflow>加速节点`、`workflow>加速节点`、`workflow>加速节点`、`Seed Everywhere`、`workflow>Clip Text`、`workflow>Clip Text`、`workflow>Clip Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、SaveImage、LoadImage、WanMoeKSampler、VAEDecodeTiled

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>加速节点` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `workflow>Clip Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `workflow>Clip Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `workflow>Clip Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
