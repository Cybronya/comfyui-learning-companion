---
key: 平台全量/【阡陌】SeedVR 2.5 视频超高清放大工作流_2013232523886731266.json
name: 【阡陌】SeedVR 2.5 视频超高清放大工作流_2013232523886731266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】SeedVR 2.5 视频超高清放大工作流_2013232523886731266.json
hash: 6d1c4eb5a7b803db
coverage: 0.833333
learned_at: 2026-11-14 01:26:18
nodes: [Note, SeedVR2TorchCompileSettings, Note, JoinImageWithAlpha, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, GetVideoComponents, CreateVideo, SeedVR2LoadDiTModel, LoadImage, LoadVideo, SaveVideo]
patterns: []
missing: []
---

# 平台全量/【阡陌】SeedVR 2.5 视频超高清放大工作流_2013232523886731266.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】SeedVR 2.5 视频超高清放大工作流_2013232523886731266.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `Note`
- `SeedVR2TorchCompileSettings`
- `Note`
- `JoinImageWithAlpha`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `GetVideoComponents`
- `CreateVideo`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `LoadVideo`
- `SaveVideo`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`SeedVR2TorchCompileSettings`、`JoinImageWithAlpha`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`GetVideoComponents`、`CreateVideo`、`SeedVR2LoadDiTModel`、`LoadImage`、`LoadVideo`、`SaveVideo`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2TorchCompileSettings、SeedVR2VideoUpscaler、SaveVideo、CreateVideo、GetVideoComponents
