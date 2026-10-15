---
key: 视频生成/文生视频/ComfyUI Wan 2.1 可实现任意轨迹指令运动控制 AI 视频生成工作流_1928353858429566977.json
name: ComfyUI Wan 2.1 可实现任意轨迹指令运动控制 AI 视频生成工作流_1928353858429566977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ComfyUI Wan 2.1 可实现任意轨迹指令运动控制 AI 视频生成工作流_1928353858429566977.json
hash: 001e8b05790afa38
coverage: 0.736842
learned_at: 2026-10-15 22:44:06
nodes: [CLIPVisionLoader, WanVideoBlockSwap, Note, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, PrimitiveNode, Note, Note, Note, Note, Note, Fast Groups Bypasser (rgthree), LoadImage, SplineEditor, ImageResizeKJv2, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, VHS_VideoCombine, Reroute, WanVideoATITracksVisualize, SplineEditor, StringConstantMultiline, SplineEditor, VHS_VideoCombine, WanVideoATITracks, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoDecode, AppendStringsToList, AppendStringsToList, WanVideoATITracksVisualize, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/ComfyUI Wan 2.1 可实现任意轨迹指令运动控制 AI 视频生成工作流_1928353858429566977.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ComfyUI Wan 2.1 可实现任意轨迹指令运动控制 AI 视频生成工作流_1928353858429566977.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `PrimitiveNode`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SplineEditor`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoATITracksVisualize`
- `SplineEditor`
- `StringConstantMultiline`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoATITracks`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `AppendStringsToList`
- `AppendStringsToList`
- `WanVideoATITracksVisualize`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `Note`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`LoadImage`、`SplineEditor`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoATITracksVisualize`、`StringConstantMultiline`、`WanVideoATITracks`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`AppendStringsToList`、`easy clearCacheAll`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
