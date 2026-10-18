---
key: 视频生成/图生视频/【全能图片V1分镜】Wan2.2-aniwan（一键成片）_1978583926098776065.json
name: 【全能图片V1分镜】Wan2.2-aniwan（一键成片）_1978583926098776065.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【全能图片V1分镜】Wan2.2-aniwan（一键成片）_1978583926098776065.json
hash: 5d65dc1c11ed0a4c
coverage: 0.705128
learned_at: 2026-10-15 22:32:19
nodes: [Anything Everywhere, Anything Everywhere, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoVAELoader, Note, Note, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, CR Text, WanVideoBlockSwap, Int, SetNode, ColorCorrectOfUtils, easy batchAnything, easy forLoopEnd, ImageResize+, ImageResize+, Note, PreviewImage, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoDecode, PreviewImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, Note, ImageCASharpening+, SetNode, easy imageListToImageBatch, PreviewImage, GetNode, WanVideoClipVisionEncode, RHHiddenNodes, BatchCount+, GetNode, WanVideoSampler, WanVideoImageToVideoEncode, easy forLoopStart, RH_Nano_Banana_Image2Image, CR Text Concatenate, CR Text, VHS_Unbatch, LoadImage, JjkText, MathExpression|pysssss, JWInteger, Note, VHS_LoadAudioUpload, PreviewAudio, Float, Float, Note, WanVideoTextEncode, Int, Int, PrimitiveNode, Note, Text Load Line From File, VHS_VideoCombine, RHHiddenNodes, Note, WanVideoModelLoader, Note, PrimitiveBoolean, easy ifElse, easy ifElse, PrimitiveBoolean, RHHiddenNodes, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/【全能图片V1分镜】Wan2.2-aniwan（一键成片）_1978583926098776065.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978583926098776065.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（78 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoBlockSwap`
- `Anything Everywhere`
- `CLIPVisionLoader`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `CR Text`
- `WanVideoBlockSwap`
- `Int`
- `SetNode`
- `ColorCorrectOfUtils`
- `easy batchAnything`
- `easy forLoopEnd`
- `ImageResize+`
- `ImageResize+`
- `Note`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `PreviewImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `Note`
- `ImageCASharpening+`
- `SetNode`
- `easy imageListToImageBatch`
- `PreviewImage`
- `GetNode`
- `WanVideoClipVisionEncode`
- `RHHiddenNodes`
- `BatchCount+`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `easy forLoopStart`
- `RH_Nano_Banana_Image2Image`
- `CR Text Concatenate`
- `CR Text`
- `VHS_Unbatch`
- `LoadImage`
- `JjkText`
- `MathExpression|pysssss`
- `JWInteger`
- `Note`
- `VHS_LoadAudioUpload`
- `PreviewAudio`
- `Float`
- `Float`
- `Note`
- `WanVideoTextEncode`
- `Int`
- `Int`
- `PrimitiveNode`
- `Note`
- `Text Load Line From File`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `PrimitiveBoolean`
- `easy ifElse`
- `easy ifElse`
- `PrimitiveBoolean`
- `RHHiddenNodes`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`

## 知识

覆盖率 **71%**（55/78）

**有卡**：`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`CR Text`、`Int`、`ColorCorrectOfUtils`、`easy batchAnything`、`easy forLoopEnd`、`ImageResize+`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`ImageCASharpening+`、`easy imageListToImageBatch`、`WanVideoClipVisionEncode`、`RHHiddenNodes`、`BatchCount+`、`WanVideoImageToVideoEncode`、`easy forLoopStart`、`RH_Nano_Banana_Image2Image`、`CR Text Concatenate`、`VHS_Unbatch`、`LoadImage`、`MathExpression|pysssss`、`JWInteger`、`VHS_LoadAudioUpload`、`PreviewAudio`、`Float`、`WanVideoTextEncode`、`Text Load Line From File`、`PrimitiveBoolean`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
