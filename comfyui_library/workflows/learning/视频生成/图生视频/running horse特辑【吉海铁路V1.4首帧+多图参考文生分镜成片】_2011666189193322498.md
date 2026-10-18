---
key: 视频生成/图生视频/running horse特辑【吉海铁路V1.4首帧+多图参考文生分镜成片】_2011666189193322498.json
name: running horse特辑【吉海铁路V1.4首帧+多图参考文生分镜成片】_2011666189193322498.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/running horse特辑【吉海铁路V1.4首帧+多图参考文生分镜成片】_2011666189193322498.json
hash: 2ab63313b9a95b0f
coverage: 0.642857
learned_at: 2026-10-15 22:34:24
nodes: [SetNode, RH_Translator, LoadImage, easy promptConcat, InversionDemoLazySwitch, Float, SetNode, SaveVideo, SetNode, GetNode, ProcessString, SetNode, WanVideoEncode, WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, UNETLoader, MathExpression|pysssss, ImageFromBatch+, GetNode, GetNode, PathchSageAttentionKJ, SetNode, WanFirstLastFrameToVideo, CLIPTextEncode, WanFirstLastFrameToVideo, GetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, WanMoeKSampler, GetNode, VAEDecodeTiled, FlashVSR_SM_Model, CreateVideo, WanMoeKSampler, GetNode, CLIPTextEncode, SetNode, CLIPLoader, GetNode, SetNode, UNETLoader, PathchSageAttentionKJ, GetNode, WanVideoNAG, easy cleanGpuUsed, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_KSampler, CLIPTextEncode, easy forLoopEnd, ImageBatchExtendWithOverlap, easy forLoopStart, GetNode, MathExpression|pysssss, KSampler, SetNode, VAELoader, PreviewImage, MathExpression|pysssss, easy promptLine, easy showAnything, VAEDecode, ImageListToBatch_, SetNode, GetImageSize, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, SetNode, Anything Everywhere3, RH_LLMAPI_NODE, easy promptLine, GetNode, GetNode, RH_LLMAPI_NODE, ImageFromBatch, ImageFromBatch, easy promptLine, RH_LLMAPI_NODE, LoadImage, LoadImage, JjkText, Int, PrimitiveBoolean, LoadImage, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 1053700165751892, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/running horse特辑【吉海铁路V1.4首帧+多图参考文生分镜成片】_2011666189193322498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011666189193322498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
- `SetNode`
- `RH_Translator`
- `LoadImage`
- `easy promptConcat`
- `InversionDemoLazySwitch`
- `Float`
- `SetNode`
- `SaveVideo`
- `SetNode`
- `GetNode`
- `ProcessString`
- `SetNode`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `WanMoeKSampler` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `FlashVSR_SM_Model`
- `CreateVideo`
- `WanMoeKSampler` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `GetNode`
- `WanVideoNAG`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_KSampler` ★核心
- `CLIPTextEncode` ★核心
- `easy forLoopEnd`
- `ImageBatchExtendWithOverlap`
- `easy forLoopStart`
- `GetNode`
- `MathExpression|pysssss`
- `KSampler` ★核心
- `SetNode`
- `VAELoader`
- `PreviewImage`
- `MathExpression|pysssss`
- `easy promptLine`
- `easy showAnything`
- `VAEDecode` ★核心
- `ImageListToBatch_`
- `SetNode`
- `GetImageSize`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `SetNode`
- `Anything Everywhere3`
- `RH_LLMAPI_NODE`
- `easy promptLine`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `ImageFromBatch`
- `ImageFromBatch`
- `easy promptLine`
- `RH_LLMAPI_NODE`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `Int`
- `PrimitiveBoolean`
- `LoadImage`
- `Int`

## 关键参数

- `seed` = `1053700165751892`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（63/98）

**有卡**：`RH_Translator`、`LoadImage`、`easy promptConcat`、`InversionDemoLazySwitch`、`Float`、`SaveVideo`、`ProcessString`、`WanVideoEncode`、`WanVideoVAELoader`、`UNETLoader`、`MathExpression|pysssss`、`ImageFromBatch+`、`PathchSageAttentionKJ`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`VAEDecodeTiled`、`WanMoeKSampler`、`FlashVSR_SM_Model`、`CreateVideo`、`CLIPLoader`、`WanVideoNAG`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSR_SM_KSampler`、`easy forLoopEnd`、`ImageBatchExtendWithOverlap`、`easy forLoopStart`、`KSampler`、`VAELoader`、`easy promptLine`、`VAEDecode`、`ImageListToBatch_`、`GetImageSize`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`RH_LLMAPI_NODE`、`ImageFromBatch`、`Int`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
