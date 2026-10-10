---
key: Wan2.1 高质量文生图_1945360629114839041.json
name: Wan2.1 高质量文生图_1945360629114839041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1 高质量文生图_1945360629114839041.json
hash: 6018731785aeccbf
coverage: 1
learned_at: 2026-10-10 20:59:13
nodes: [WanVideoLoraSelect, WanVideoVAELoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoLoraSelect, WanVideoSampler, SaveImage, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoTextEncodeSingle, FluxResolutionNode, WanVideoEmptyEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect]
patterns: []
missing: []
---

# Wan2.1 高质量文生图_1945360629114839041.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.1 高质量文生图_1945360629114839041.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（16 个）：
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `SaveImage`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `FluxResolutionNode`
- `WanVideoEmptyEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoSampler`、`SaveImage`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`FluxResolutionNode`、`WanVideoEmptyEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoLoraSelect、FluxResolutionNode、SaveImage
