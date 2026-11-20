---
key: 平台全量/kimodo-with-post-process_2068218265180135425.json
name: kimodo-with-post-process_2068218265180135425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/kimodo-with-post-process_2068218265180135425.json
hash: 283218821a1c6e76
coverage: 0.833333
learned_at: 2026-11-14 01:12:59
nodes: [Kimodo_SaveNPZ, Kimodo_PostProcess, Kimodo_TextEncode, Kimodo_Sampler, Kimodo_Preview3D, Kimodo_Preview, PreviewImage, SaveImage, Kimodo_ExportBVH, PreviewAny, FancyTimerNode, Kimodo_LoadModel]
patterns: []
missing: []
---

# 平台全量/kimodo-with-post-process_2068218265180135425.json

> 来源文件 `comfyui_library/workflows/平台全量/kimodo-with-post-process_2068218265180135425.json`

## 结构

**生成流程**：Sampling → Output → Other

**节点**（12 个）：
- `Kimodo_SaveNPZ`
- `Kimodo_PostProcess`
- `Kimodo_TextEncode`
- `Kimodo_Sampler` ★核心
- `Kimodo_Preview3D`
- `Kimodo_Preview`
- `PreviewImage`
- `SaveImage`
- `Kimodo_ExportBVH`
- `PreviewAny`
- `FancyTimerNode`
- `Kimodo_LoadModel`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`Kimodo_SaveNPZ`、`Kimodo_PostProcess`、`Kimodo_TextEncode`、`Kimodo_Sampler`、`Kimodo_Preview3D`、`Kimodo_Preview`、`SaveImage`、`Kimodo_ExportBVH`、`FancyTimerNode`、`Kimodo_LoadModel`

**用到的条目**：Kimodo_Sampler、Kimodo_TextEncode、Kimodo_Preview、Kimodo_Preview3D、Kimodo_SaveNPZ、SaveImage、FancyTimerNode、Kimodo_ExportBVH
