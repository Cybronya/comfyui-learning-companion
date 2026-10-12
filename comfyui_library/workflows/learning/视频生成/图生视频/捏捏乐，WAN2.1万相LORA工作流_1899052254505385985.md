---
key: 视频生成/图生视频/捏捏乐，WAN2.1万相LORA工作流_1899052254505385985.json
name: 捏捏乐，WAN2.1万相LORA工作流_1899052254505385985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/捏捏乐，WAN2.1万相LORA工作流_1899052254505385985.json
hash: 795e4b33063670dc
coverage: 1
learned_at: 2026-10-12 20:12:51
nodes: [WanVideoTextEncode, WanVideoImageClipEncode, WanVideoVAELoader, WanVideoDecode, WanVideoBlockSwap, WanVideoTorchCompileSettings, LoraLoaderModelOnly, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, LoadImage, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/捏捏乐，WAN2.1万相LORA工作流_1899052254505385985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/捏捏乐，WAN2.1万相LORA工作流_1899052254505385985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（14 个）：
- `WanVideoTextEncode`
- `WanVideoImageClipEncode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `LoraLoaderModelOnly` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadImage`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`WanVideoTextEncode`、`WanVideoImageClipEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoraLoaderModelOnly`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`LoadImage`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode
