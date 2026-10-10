---
key: 视频生成/文生视频/🈚️Wan2.2-native-Lightx-文生_图生视频_首中尾帧·多合一_1949884683304747009.json
name: 🈚️Wan2.2-native-Lightx-文生_图生视频_首中尾帧·多合一_1949884683304747009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🈚️Wan2.2-native-Lightx-文生_图生视频_首中尾帧·多合一_1949884683304747009.json
hash: aa051027b7f3203d
coverage: 0.361963
learned_at: 2026-10-10 23:14:48
nodes: [ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, Wan22PromptSelector, ModelSamplingSD3, SetNode, ModelSamplingSD3, SetNode, SetNode, GetNode, GetNode, easy cleanGpuUsed, VAEDecode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, CLIPLoader, VAELoader, GetNode, GetNode, PreviewImage, GetNode, GetNode, PreviewImage, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, easy showAnything, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, Anything Everywhere, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, RIFE VFI, CM_FloatToInt, easy mathInt, CM_IntToFloat, PrimitiveNode, GetNode, GetNode, GetNode, easy promptConcat, Note, CR Prompt Text, SetNode, wanBlock_Swap, Fast Groups Bypasser (rgthree), VHS_VideoCombine, ImageResizeKJv2, easy seed, GetNode, SetNode, GetNode, ImpactFloat, KSamplerAdvanced, Int, Int, PreviewImage, CR Prompt Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), KSamplerAdvanced, WanFirstMiddleLastFrameToVideo, GetNode, GetNode, GetNode, Any Switch (rgthree), SetNode, easy promptConcat, UNETLoader, Int, easy showAnything, UNETLoader, UNETLoader, LoraLoaderModelOnly, Note, RH_LLMAPI_NODE, Note, Note, CR Prompt Text, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionLoader, wanBlock_Swap, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海图像组合批次, ImageConcatFromBatch, easy showAnything, Wan22PromptSelector, AILab_QwenVL, CR Prompt Text, LayerUtility: TextJoin, LoraLoaderModelOnly, CR Prompt Text, Note, INTConstant, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), easy showAnything, ImpactSwitch, Note, INTConstant, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage, PreviewImage, LoadImage, LoadImage]
patterns: []
missing: [LayerUtility: TextJoin, RIFE VFI, easy cleanGpuUsed, easy mathInt, 孤海图像组合批次, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy promptConcat, easy promptConcat, easy seed]
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `孤海图像组合批次` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/🈚️Wan2.2-native-Lightx-文生_图生视频_首中尾帧·多合一_1949884683304747009.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🈚️Wan2.2-native-Lightx-文生_图生视频_首中尾帧·多合一_1949884683304747009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（163 个）：
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Wan22PromptSelector`
- `ModelSamplingSD3`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Anything Everywhere`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `RIFE VFI`
- `CM_FloatToInt`
- `easy mathInt`
- `CM_IntToFloat`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy promptConcat`
- `Note`
- `CR Prompt Text`
- `SetNode`
- `wanBlock_Swap`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `easy seed`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImpactFloat`
- `KSamplerAdvanced` ★核心
- `Int`
- `Int`
- `PreviewImage`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `easy promptConcat`
- `UNETLoader` ★核心
- `Int`
- `easy showAnything`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `RH_LLMAPI_NODE`
- `Note`
- `Note`
- `CR Prompt Text`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `wanBlock_Swap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海图像组合批次`
- `ImageConcatFromBatch`
- `easy showAnything`
- `Wan22PromptSelector`
- `AILab_QwenVL`
- `CR Prompt Text`
- `LayerUtility: TextJoin`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `Note`
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `ImpactSwitch`
- `Note`
- `INTConstant`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **36%**（59/163）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`Wan22PromptSelector`、`ModelSamplingSD3`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`ImageResizeKJv2`、`CM_FloatToInt`、`CM_IntToFloat`、`wanBlock_Swap`、`VHS_VideoCombine`、`ImpactFloat`、`KSamplerAdvanced`、`Int`、`LoraLoaderModelOnly`、`WanFirstMiddleLastFrameToVideo`、`UNETLoader`、`RH_LLMAPI_NODE`、`CLIPVisionLoader`、`ImageConcatFromBatch`、`AILab_QwenVL`、`INTConstant`、`LoadImage`

**缺卡**（13）：`LayerUtility: TextJoin`、`RIFE VFI`、`easy cleanGpuUsed`、`easy mathInt`、`孤海图像组合批次`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`easy promptConcat`、`easy promptConcat`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `孤海图像组合批次` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
