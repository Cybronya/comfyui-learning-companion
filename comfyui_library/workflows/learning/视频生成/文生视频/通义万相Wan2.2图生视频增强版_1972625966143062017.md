---
key: 视频生成/文生视频/通义万相Wan2.2图生视频增强版_1972625966143062017.json
name: 通义万相Wan2.2图生视频增强版_1972625966143062017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/通义万相Wan2.2图生视频增强版_1972625966143062017.json
hash: f870010d04ed32c9
coverage: 0.828571
learned_at: 2026-10-15 22:49:04
nodes: [Int, Note, Note, Note, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, WanVideoSampler, GetImageSizeAndCount, WanVideoDecode, RIFE VFI, INTConstant, Int, Note, Int, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, Note, ImageResizeKJv2, INTConstant, RH_LLMAPI_NODE, ShowText|pysssss, WanVideoTextEncode, LoadImage, Text Concatenate, Text Multiline, Wan22PromptSelector]
patterns: []
missing: []
---

# 视频生成/文生视频/通义万相Wan2.2图生视频增强版_1972625966143062017.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/通义万相Wan2.2图生视频增强版_1972625966143062017.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `Int`
- `Note`
- `Note`
- `Note`
- `WanVideoImageToVideoEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `RIFE VFI`
- `INTConstant`
- `Int`
- `Note`
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Note`
- `ImageResizeKJv2`
- `INTConstant`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `WanVideoTextEncode`
- `LoadImage`
- `Text Concatenate`
- `Text Multiline`
- `Wan22PromptSelector`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`Int`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`RIFE VFI`、`INTConstant`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`RH_LLMAPI_NODE`、`WanVideoTextEncode`、`LoadImage`、`Text Concatenate`、`Text Multiline`、`Wan22PromptSelector`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
