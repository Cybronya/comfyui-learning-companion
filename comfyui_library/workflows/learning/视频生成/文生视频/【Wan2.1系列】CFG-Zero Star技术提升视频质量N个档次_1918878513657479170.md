---
key: 视频生成/文生视频/【Wan2.1系列】CFG-Zero Star技术提升视频质量N个档次_1918878513657479170.json
name: 【Wan2.1系列】CFG-Zero Star技术提升视频质量N个档次_1918878513657479170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1918878513657479170.json
hash: 9d3e77da173496c7
coverage: 0.909091
learned_at: 2026-10-15 22:43:23
nodes: [LoadWanVideoT5TextEncoder, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoBlockSwap, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoTeaCache, WanVideoBlockSwap, WanVideoImageToVideoEncode, CLIPVisionLoader, WanVideoEnhanceAVideo, WanVideoDecode, WanVideoClipVisionEncode, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoVAELoader, WanVideoSampler, WanVideoVAELoader, ImageResizeKJ, PreviewImage, WanVideoModelLoader, LoadImage, VHS_VideoCombine, WanVideoSampler, Fast Groups Bypasser (rgthree), WanVideoTextEncode, WanVideoExperimentalArgs, VHS_VideoCombine, WanVideoTextEncode, WanVideoExperimentalArgs, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/【Wan2.1系列】CFG-Zero Star技术提升视频质量N个档次_1918878513657479170.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1918878513657479170.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoModelLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `WanVideoTextEncode`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoExperimentalArgs`
- `MarkdownNote`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoSampler`、`ImageResizeKJ`、`LoadImage`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoExperimentalArgs`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
