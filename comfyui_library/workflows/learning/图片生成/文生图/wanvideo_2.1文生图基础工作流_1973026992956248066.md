---
key: 图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json
name: wanvideo_2.1文生图基础工作流_1973026992956248066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json
hash: 654d10d85ae0cb90
coverage: 0.944444
learned_at: 2026-10-10 20:59:28
nodes: [CLIPTextEncode, CLIPLoader, Note, CLIPTextEncode, WanVideoTextEmbedBridge, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoDecode, WanVideoSampler, WanVideoTeaCache, SaveImage, WanVideoTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json`

## 结构

**节点**（18 个）：
- `CLIPTextEncode`
- `CLIPLoader`
- `Note`
- `CLIPTextEncode`
- `WanVideoTextEmbedBridge`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `SaveImage`
- `WanVideoTextEncode`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`Note`、`WanVideoTextEmbedBridge`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTeaCache`、`SaveImage`
