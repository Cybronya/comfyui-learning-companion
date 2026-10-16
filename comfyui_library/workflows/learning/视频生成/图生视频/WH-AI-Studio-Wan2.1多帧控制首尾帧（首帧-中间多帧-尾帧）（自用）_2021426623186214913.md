---
key: 视频生成/图生视频/WH-AI-Studio-Wan2.1多帧控制首尾帧（首帧-中间多帧-尾帧）（自用）_2021426623186214913.json
name: WH-AI-Studio-Wan2.1多帧控制首尾帧（首帧-中间多帧-尾帧）（自用）_2021426623186214913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2021426623186214913.json
hash: ae512d56875b94a9
coverage: 0.952381
learned_at: 2026-10-15 22:35:08
nodes: [ForLoopOpen, ColorMatch, ImageResize+, GetImageRangeFromBatch, WanVideoImageToVideoEncode, easy batchAnything, MathExpression|pysssss, easy ifElse, VHS_GetImageCount, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, GetImageSizeAndCount, RIFE VFI, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, SDVM Image List Repeat, ImageListToBatch+, VHS_GetImageCount, Int Input [DVB], WanVideoSLG, WanVideoBlockSwap, easy cleanGpuUsed, Int Input [DVB], Int Input [DVB], Int Input [DVB], Int, Int, LayerUtility: PurgeVRAM, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, SetNode, InversionDemoLazyIndexSwitch, InversionDemoLazyIndexSwitch, CM_IntToBool, MathExpression|pysssss, MathExpression|pysssss, InversionDemoLazyIndexSwitch, LayerUtility: PurgeVRAM, ForLoopClose, WanVideoModelLoader, WanVideoTeaCache, Int Input [DVB], InversionDemoLazyIndexSwitch, MathExpression|pysssss, Int Input [DVB], MathExpression|pysssss, WanVideoTextEncode, LoadImage, LoadImage, LoadImage, LoadImage, Text Multiline, Text Multiline, Text Multiline, LoadImage, Text Multiline, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/WH-AI-Studio-Wan2.1多帧控制首尾帧（首帧-中间多帧-尾帧）（自用）_2021426623186214913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021426623186214913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（63 个）：
- `ForLoopOpen`
- `ColorMatch`
- `ImageResize+`
- `GetImageRangeFromBatch`
- `WanVideoImageToVideoEncode`
- `easy batchAnything`
- `MathExpression|pysssss`
- `easy ifElse`
- `VHS_GetImageCount`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `SetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `RIFE VFI`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `SDVM Image List Repeat`
- `ImageListToBatch+`
- `VHS_GetImageCount`
- `Int Input [DVB]`
- `WanVideoSLG`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `Int Input [DVB]`
- `Int Input [DVB]`
- `Int Input [DVB]`
- `Int`
- `Int`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `SetNode`
- `InversionDemoLazyIndexSwitch`
- `InversionDemoLazyIndexSwitch`
- `CM_IntToBool`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `InversionDemoLazyIndexSwitch`
- `LayerUtility: PurgeVRAM`
- `ForLoopClose`
- `WanVideoModelLoader`
- `WanVideoTeaCache`
- `Int Input [DVB]`
- `InversionDemoLazyIndexSwitch`
- `MathExpression|pysssss`
- `Int Input [DVB]`
- `MathExpression|pysssss`
- `WanVideoTextEncode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `LoadImage`
- `Text Multiline`
- `WanVideoDecode`

## 知识

覆盖率 **95%**（60/63）

**有卡**：`ForLoopOpen`、`ColorMatch`、`ImageResize+`、`GetImageRangeFromBatch`、`WanVideoImageToVideoEncode`、`easy batchAnything`、`MathExpression|pysssss`、`VHS_GetImageCount`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`GetImageSizeAndCount`、`RIFE VFI`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`SDVM Image List Repeat`、`ImageListToBatch+`、`Int Input [DVB]`、`WanVideoSLG`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`Int`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`WanVideoSampler`、`InversionDemoLazyIndexSwitch`、`CM_IntToBool`、`ForLoopClose`、`WanVideoModelLoader`、`WanVideoTeaCache`、`WanVideoTextEncode`、`LoadImage`、`Text Multiline`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
