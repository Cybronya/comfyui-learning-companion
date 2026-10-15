---
key: 视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json
name: Wan2.2文生视频工作流4步急速版_2045802208008081409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json
hash: 30ad0246b88bdd61
coverage: 1
learned_at: 2026-10-15 22:47:15
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoVAELoader, WanVideoSampler, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, CreateCFGScheduleFloatList, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（14 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、VHS_VideoCombine
