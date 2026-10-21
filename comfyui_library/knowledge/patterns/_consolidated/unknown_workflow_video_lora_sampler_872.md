---
name: unknown_workflow_video_lora_sampler_872
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7135
common_nodes: [Anything Everywhere, BatchCount+, CLIPVisionLoader, CR Text, CR Text Concatenate, ColorCorrectOfUtils, CreateCFGScheduleFloatList, Float, GetNode, ImageCASharpening+, ImageResize+, Int, JWInteger, JjkText, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewAudio, PreviewImage, PrimitiveBoolean, RHHiddenNodes, RH_Nano_Banana_Image2Image, SetNode, Text Load Line From File, VHS_LoadAudioUpload, VHS_Unbatch, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy ifElse, easy imageListToImageBatch]
problems: []
missing: []
members: [视频生成/图生视频/1978583926098776065.json, 视频生成/图生视频/1983855696577990658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_872

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1978583926098776065.json、视频生成/图生视频/1983855696577990658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BatchCount+`
- `CLIPVisionLoader`
- `CR Text`
- `CR Text Concatenate`
- `ColorCorrectOfUtils`
- `CreateCFGScheduleFloatList`
- `Float`
- `GetNode`
- `ImageCASharpening+`
- `ImageResize+`
- `Int`
- `JWInteger`
- `JjkText`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveBoolean`
- `RHHiddenNodes`
- `RH_Nano_Banana_Image2Image`
- `SetNode`
- `Text Load Line From File`
- `VHS_LoadAudioUpload`
- `VHS_Unbatch`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
