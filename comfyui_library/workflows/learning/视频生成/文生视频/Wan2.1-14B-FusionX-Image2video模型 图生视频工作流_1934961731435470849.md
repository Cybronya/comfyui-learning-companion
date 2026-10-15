---
key: 视频生成/文生视频/Wan2.1-14B-FusionX-Image2video模型 图生视频工作流_1934961731435470849.json
name: Wan2.1-14B-FusionX-Image2video模型 图生视频工作流_1934961731435470849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1-14B-FusionX-Image2video模型 图生视频工作流_1934961731435470849.json
hash: c607c2b4efbcb79e
coverage: 0.909091
learned_at: 2026-10-15 22:47:08
nodes: [ImageResizeKJv2, WanVideoImageToVideoEncode, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoDecode, VHS_VideoCombine, MarkdownNote, CLIPVisionLoader, WanVideoTextEncode, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, LoadImage, ImageResizeKJv2, LoadImage, MarkdownNote, WanVideoSampler, TextInput_, WanVideoClipVisionEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1-14B-FusionX-Image2video模型 图生视频工作流_1934961731435470849.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1-14B-FusionX-Image2video模型 图生视频工作流_1934961731435470849.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `CLIPVisionLoader`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `MarkdownNote`
- `WanVideoSampler` ★核心
- `TextInput_`
- `WanVideoClipVisionEncode`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`easy clearCacheAll`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoSampler`、`TextInput_`、`WanVideoClipVisionEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
