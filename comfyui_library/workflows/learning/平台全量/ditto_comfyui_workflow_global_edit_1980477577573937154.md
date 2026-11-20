---
key: 平台全量/ditto_comfyui_workflow_global_edit_1980477577573937154.json
name: ditto_comfyui_workflow_global_edit_1980477577573937154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ditto_comfyui_workflow_global_edit_1980477577573937154.json
hash: f4ead76688201077
coverage: 0.6
learned_at: 2026-11-14 01:10:06
nodes: [WanVideoLoraSelect, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, SetNode, WanVideoSampler, WanVideoSLG, GetNode, VHS_LoadVideo, ImageResizeKJv2, SetNode, SetNode, WanVideoVAELoader, SetNode, GetNode, WanVideoDecode, SetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, WanVideoVACEEncode, GetNode, Note, WanVideoTextEncode]
patterns: []
missing: []
---

# 平台全量/ditto_comfyui_workflow_global_edit_1980477577573937154.json

> 来源文件 `comfyui_library/workflows/平台全量/ditto_comfyui_workflow_global_edit_1980477577573937154.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `GetNode`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoVACEEncode`
- `GetNode`
- `Note`
- `WanVideoTextEncode`

## 知识

覆盖率 **60%**（15/25）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoSLG`、`VHS_LoadVideo`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、ImageResizeKJv2
