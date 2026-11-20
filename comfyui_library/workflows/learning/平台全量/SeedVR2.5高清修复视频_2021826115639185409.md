---
key: 平台全量/SeedVR2.5高清修复视频_2021826115639185409.json
name: SeedVR2.5高清修复视频_2021826115639185409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5高清修复视频_2021826115639185409.json
hash: 8b267c64892d1bf4
coverage: 0.9
learned_at: 2026-11-14 00:59:39
nodes: [SeedVR2LoadVAEModel, easy cleanGpuUsed, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, CreateVideo, SaveVideo, VHS_VideoInfoSource, SeedVR2TorchCompileSettings, Note, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5高清修复视频_2021826115639185409.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5高清修复视频_2021826115639185409.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `SeedVR2LoadVAEModel`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `CreateVideo`
- `SaveVideo`
- `VHS_VideoInfoSource`
- `SeedVR2TorchCompileSettings`
- `Note`
- `VHS_LoadVideo`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`SeedVR2LoadVAEModel`、`easy cleanGpuUsed`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`CreateVideo`、`SaveVideo`、`VHS_VideoInfoSource`、`SeedVR2TorchCompileSettings`、`VHS_LoadVideo`

**用到的条目**：SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2TorchCompileSettings、SeedVR2VideoUpscaler、SaveVideo、CreateVideo、easy cleanGpuUsed、VHS_LoadVideo
