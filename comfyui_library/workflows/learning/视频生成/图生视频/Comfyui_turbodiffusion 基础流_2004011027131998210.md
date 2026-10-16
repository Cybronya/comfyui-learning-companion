---
key: 视频生成/图生视频/Comfyui_turbodiffusion 基础流_2004011027131998210.json
name: Comfyui_turbodiffusion 基础流_2004011027131998210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2004011027131998210.json
hash: dc55c26f9d77371c
coverage: 1
learned_at: 2026-10-15 22:33:52
nodes: [TurboWanVAELoader, LoadImage, TurboWanModelLoader, TurboWanModelLoader, CLIPLoader, CLIPTextEncode, VHS_VideoCombine, TurboDiffusionI2VSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/Comfyui_turbodiffusion 基础流_2004011027131998210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004011027131998210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（8 个）：
- `TurboWanVAELoader`
- `LoadImage`
- `TurboWanModelLoader`
- `TurboWanModelLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `TurboDiffusionI2VSampler` ★核心

## 知识

覆盖率 **100%**（8/8）

**有卡**：`TurboWanVAELoader`、`LoadImage`、`TurboWanModelLoader`、`CLIPLoader`、`CLIPTextEncode`、`VHS_VideoCombine`、`TurboDiffusionI2VSampler`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、TurboDiffusionI2VSampler、TurboWanVAELoader、VHS_VideoCombine、TurboWanModelLoader、sd15-t2i-basic
