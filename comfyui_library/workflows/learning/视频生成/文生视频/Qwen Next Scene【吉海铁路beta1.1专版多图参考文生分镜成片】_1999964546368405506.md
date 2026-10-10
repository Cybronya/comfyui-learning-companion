---
key: 视频生成/文生视频/Qwen Next Scene【吉海铁路beta1.1专版多图参考文生分镜成片】_1999964546368405506.json
name: Qwen Next Scene【吉海铁路beta1.1专版多图参考文生分镜成片】_1999964546368405506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen Next Scene【吉海铁路beta1.1专版多图参考文生分镜成片】_1999964546368405506.json
hash: 08c9cd6d7b76dbf7
coverage: 0.716216
learned_at: 2026-10-11 02:57:37
nodes: [CLIPLoader, LoraLoaderModelOnly, EmptySD3LatentImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionLoader, wanBlockSwap, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, wanBlockSwap, ModelSamplingSD3, PathchSageAttentionKJ, CLIPLoader, CLIPTextEncode, ModelPatchTorchSettings, ModelPatchTorchSettings, KSamplerAdvanced, KSamplerAdvanced, VAELoader, GetNode, SetNode, CLIPTextEncode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetNode, Anything Everywhere3, VAELoader, LoraLoaderModelOnly, UNETLoader, VAEDecode, SetNode, VAEDecode, easy promptLine, KSampler, Bjornulf_AnythingToText, SetNode, LoraLoaderModelOnly, GetNode, CreateVideo, RH_Translator, Int, LoadImage, FluxResolutionNode, easy showAnything, easy promptConcat, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ProcessString, RH_LLMAPI_NODE, WanMultiFrameRefToVideo, BatchCount+, MathExpression|pysssss, InversionDemoLazySwitch, GetNode, RebatchImages, SaveVideo, easy cleanGpuUsed, GetImageSize, FlashVSR_SM_KSampler, FlashVSR_SM_Model, JjkText, LoadImage, LoadImage, LoadImage, Float, Int, SetNode, PrimitiveBoolean]
patterns: []
missing: [BatchCount+, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, easy cleanGpuUsed, easy promptConcat, easy promptLine]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 768, "steps": 1001593196}
discoveries: [次要节点 `BatchCount+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Qwen Next Scene【吉海铁路beta1.1专版多图参考文生分镜成片】_1999964546368405506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen Next Scene【吉海铁路beta1.1专版多图参考文生分镜成片】_1999964546368405506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Anything Everywhere3`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `easy promptLine`
- `KSampler` ★核心
- `Bjornulf_AnythingToText`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `CreateVideo`
- `RH_Translator`
- `Int`
- `LoadImage`
- `FluxResolutionNode`
- `easy showAnything`
- `easy promptConcat`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `WanMultiFrameRefToVideo`
- `BatchCount+`
- `MathExpression|pysssss`
- `InversionDemoLazySwitch`
- `GetNode`
- `RebatchImages`
- `SaveVideo`
- `easy cleanGpuUsed`
- `GetImageSize`
- `FlashVSR_SM_KSampler` ★核心
- `FlashVSR_SM_Model`
- `JjkText`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Float`
- `Int`
- `SetNode`
- `PrimitiveBoolean`

## 关键参数

- `seed` = `768`
- `steps` = `1001593196`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **72%**（53/74）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`UNETLoader`、`CLIPVisionLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`VAEDecode`、`KSampler`、`Bjornulf_AnythingToText`、`CreateVideo`、`RH_Translator`、`Int`、`LoadImage`、`FluxResolutionNode`、`TextEncodeQwenImageEditPlus`、`ProcessString`、`RH_LLMAPI_NODE`、`WanMultiFrameRefToVideo`、`InversionDemoLazySwitch`、`RebatchImages`、`SaveVideo`、`GetImageSize`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`、`Float`、`PrimitiveBoolean`

**缺卡**（6）：`BatchCount+`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy promptConcat`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `BatchCount+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
