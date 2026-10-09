---
key: 图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json
name: wanvideo_2.1文生图基础工作流_1973026992956248066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json
hash: 654d10d85ae0cb90
coverage: 0.944444
learned_at: 2026-10-09 19:50:52
nodes: [CLIPTextEncode, CLIPLoader, Note, CLIPTextEncode, WanVideoTextEmbedBridge, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoDecode, WanVideoSampler, WanVideoTeaCache, SaveImage, WanVideoTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1973026992956248066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Output → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Note`
- `CLIPTextEncode` ★核心
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
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `SaveImage`
- `WanVideoTextEncode`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`WanVideoTextEmbedBridge`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTeaCache`、`SaveImage`、`WanVideoTextEncode`

**用到的条目**：CLIPTextEncode、CLIPLoader、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
