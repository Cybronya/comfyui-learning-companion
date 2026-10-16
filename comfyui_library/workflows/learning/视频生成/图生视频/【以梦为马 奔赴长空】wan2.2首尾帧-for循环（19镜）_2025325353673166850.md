---
key: 视频生成/图生视频/【以梦为马 奔赴长空】wan2.2首尾帧-for循环（19镜）_2025325353673166850.json
name: 【以梦为马 奔赴长空】wan2.2首尾帧-for循环（19镜）_2025325353673166850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2025325353673166850.json
hash: 358e54044c06fa1c
coverage: 0.883333
learned_at: 2026-10-15 22:35:12
nodes: [Anything Everywhere, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, Anything Everywhere, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoDecode, WanVideoApplyNAG, easy cleanGpuUsed, easy cleanGpuUsed, ImageCASharpening+, LayerUtility: PurgeVRAM V2, WanVideoTextEncodeSingle, WanVideoClipVisionEncode, Int, easy batchAnything, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, PreviewImage, easy forLoopStart, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoImageToVideoEncode, Note, PreviewImage, GetImageSize, Compare, easy ifElse, GetImageSize, JWInteger, Note, Note, Int, Int, Note, PreviewImage, ImageResize+, ImageResize+, ImageResize+, ImageResize+, LoadImage, LoadImage, LoadImage, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, JWInteger, LoadImage, LoadImage, MathExpression|pysssss, SetNode, WanVideoSetBlockSwap, LoadImage, LoadImage, LoadImage, ImageResize+, LoadImage, ImageResize+, LoadImage, LoadImage, LoadImage, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageResize+, RHHiddenNodes, LoadImage, LoadImage, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, WanVideoTextEncodeSingle, easy forLoopEnd, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, VHS_VideoCombine, easy anythingIndexSwitch, LoadAudio, AudioCrop, PreviewAudio, Float, AdjustAudio, VHS_VideoCombine, AudioCombine, RH_Captioner, easy showAnything, Note, HunyuanVideoFoley, ImageResize+, ImageResize+, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/【以梦为马 奔赴长空】wan2.2首尾帧-for循环（19镜）_2025325353673166850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2025325353673166850.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（120 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `WanVideoApplyNAG`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTextEncodeSingle`
- `WanVideoClipVisionEncode`
- `Int`
- `easy batchAnything`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PreviewImage`
- `easy forLoopStart`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `Note`
- `PreviewImage`
- `GetImageSize`
- `Compare`
- `easy ifElse`
- `GetImageSize`
- `JWInteger`
- `Note`
- `Note`
- `Int`
- `Int`
- `Note`
- `PreviewImage`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `MathExpression|pysssss`
- `SetNode`
- `WanVideoSetBlockSwap`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `LoadImage`
- `ImageResize+`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `RHHiddenNodes`
- `LoadImage`
- `LoadImage`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `WanVideoTextEncodeSingle`
- `easy forLoopEnd`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `LoadAudio`
- `AudioCrop`
- `PreviewAudio`
- `Float`
- `AdjustAudio`
- `VHS_VideoCombine`
- `AudioCombine`
- `RH_Captioner`
- `easy showAnything`
- `Note`
- `HunyuanVideoFoley`
- `ImageResize+`
- `ImageResize+`
- `Text Multiline`

## 知识

覆盖率 **88%**（106/120）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoDecode`、`WanVideoApplyNAG`、`easy cleanGpuUsed`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`WanVideoTextEncodeSingle`、`WanVideoClipVisionEncode`、`Int`、`easy batchAnything`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`easy forLoopStart`、`WanVideoImageToVideoEncode`、`GetImageSize`、`Compare`、`JWInteger`、`ImageResize+`、`LoadImage`、`MathExpression|pysssss`、`RHHiddenNodes`、`easy forLoopEnd`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`LoadAudio`、`AudioCrop`、`PreviewAudio`、`Float`、`AdjustAudio`、`AudioCombine`、`RH_Captioner`、`HunyuanVideoFoley`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
