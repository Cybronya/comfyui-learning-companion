---
key: 视频生成/图生视频/Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json
name: Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1959544112867389442.json
hash: d4dfc2d8838d4040
coverage: 0.833333
learned_at: 2026-10-15 22:31:24
nodes: [WanVideoDecode, INTConstant, GetImageSizeAndCount, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, INTConstant, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, Note, Note, WanVideoBlockSwap, WanVideoTextEncode, WanVideoModelLoader, LoadWanVideoT5TextEncoder, PrimitiveString, ttN text, ShowText|pysssss, easy promptReplace, Note, WanVideoImageToVideoEncode, LoadImage, PrimitiveString, ImageResizeKJv2, Int, Int, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1959544112867389442.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoDecode`
- `INTConstant`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveString`
- `ttN text`
- `ShowText|pysssss`
- `easy promptReplace`
- `Note`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `PrimitiveString`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `Int`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`WanVideoDecode`、`INTConstant`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`ttN text`、`easy promptReplace`、`WanVideoImageToVideoEncode`、`LoadImage`、`ImageResizeKJv2`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
