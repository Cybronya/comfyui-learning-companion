---
key: 视频生成/图生视频/wanvideo2.1_svi_infinite_generate_1983813929321308162.json
name: wanvideo2.1_svi_infinite_generate_1983813929321308162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983813929321308162.json
hash: 3c5b7e04ce401623
coverage: 0.533333
learned_at: 2026-10-15 22:32:46
nodes: [WanVideoLoraSelectMulti, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, SetNode, CLIPVisionLoader, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, SetNode, WanVideoClipVisionEncode, GetNode, WanVideoModelLoader, WanVideoVAELoader, ImageResizeKJv2, WanVideoSampler, WanVideoImageToVideoEncode, LoadImage, Note, Note, AILab_QwenVL, PreviewAny, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo2.1_svi_infinite_generate_1983813929321308162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983813929321308162.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `Note`
- `Note`
- `AILab_QwenVL`
- `PreviewAny`
- `VHS_VideoCombine`

## 知识

覆盖率 **53%**（16/30）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`LoadImage`、`AILab_QwenVL`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
