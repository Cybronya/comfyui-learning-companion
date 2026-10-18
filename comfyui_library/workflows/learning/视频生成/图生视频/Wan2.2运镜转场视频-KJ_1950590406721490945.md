---
key: 视频生成/图生视频/Wan2.2运镜转场视频-KJ_1950590406721490945.json
name: Wan2.2运镜转场视频-KJ_1950590406721490945.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2运镜转场视频-KJ_1950590406721490945.json
hash: 95b51842ed72d4ca
coverage: 0.825
learned_at: 2026-10-15 22:30:55
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, WanVideoLoraSelect, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoTextEncode, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, MathExpression|pysssss, Note, Note, Note, Note, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoModelLoader, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoDecode, LoadImage, easy anythingIndexSwitch, StringReplace, Text Multiline, Note, easy showAnything, Text Multiline, RH_LLMAPI_NODE, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2运镜转场视频-KJ_1950590406721490945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950590406721490945.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note`
- `MathExpression|pysssss`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoDecode`
- `LoadImage`
- `easy anythingIndexSwitch`
- `StringReplace`
- `Text Multiline`
- `Note`
- `easy showAnything`
- `Text Multiline`
- `RH_LLMAPI_NODE`
- `ImageResizeKJv2`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoLoraSelect`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`Primitive integer [Crystools]`、`WanVideoDecode`、`LoadImage`、`easy anythingIndexSwitch`、`StringReplace`、`Text Multiline`、`RH_LLMAPI_NODE`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
