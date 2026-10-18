---
key: 视频生成/图生视频/中文出视频 WAN2.1 万相图生视频_1894627814531051521.json
name: 中文出视频 WAN2.1 万相图生视频_1894627814531051521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/中文出视频 WAN2.1 万相图生视频_1894627814531051521.json
hash: 919e7741fc9a8e16
coverage: 0.73913
learned_at: 2026-10-15 22:29:16
nodes: [WanVideoBlockSwap, LoadWanVideoT5TextEncoder, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, LoadWanVideoClipTextEncoder, Note, easy cleanGpuUsed, WanVideoVAELoader, ImageResizeAdvanced, WanVideoImageClipEncode, WanVideoSampler, VHS_VideoCombine, WanVideoDecode, LoadImage, WanVideoTextEncode, Note, TextCombinerTwo, ShowText|pysssss, RH_Prompter, Note, Note, Textbox]
patterns: []
missing: []
---

# 视频生成/图生视频/中文出视频 WAN2.1 万相图生视频_1894627814531051521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1894627814531051521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（23 个）：
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `Note`
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `ImageResizeAdvanced`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadImage`
- `WanVideoTextEncode`
- `Note`
- `TextCombinerTwo`
- `ShowText|pysssss`
- `RH_Prompter`
- `Note`
- `Note`
- `Textbox`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`easy cleanGpuUsed`、`WanVideoVAELoader`、`ImageResizeAdvanced`、`WanVideoImageClipEncode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadImage`、`WanVideoTextEncode`、`TextCombinerTwo`、`RH_Prompter`、`Textbox`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
