---
key: 平台全量/VOSR 2.0 视频高清放大_2114921205957488642.json
name: VOSR 2.0 视频高清放大_2114921205957488642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VOSR 2.0 视频高清放大_2114921205957488642.json
hash: 98df3fa3badb1b22
coverage: 1
learned_at: 2026-11-14 01:02:49
nodes: [LoadVideo, DF_Integer, GetVideoComponents, VOSR2Upscale, VOSR2ModelLoader, SaveVideo, CreateVideo]
patterns: []
missing: []
---

# 平台全量/VOSR 2.0 视频高清放大_2114921205957488642.json

> 来源文件 `comfyui_library/workflows/平台全量/VOSR 2.0 视频高清放大_2114921205957488642.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（7 个）：
- `LoadVideo`
- `DF_Integer`
- `GetVideoComponents`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `SaveVideo`
- `CreateVideo`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`LoadVideo`、`DF_Integer`、`GetVideoComponents`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SaveVideo`、`CreateVideo`

**用到的条目**：VOSR2Upscale、SaveVideo、CreateVideo、DF_Integer、GetVideoComponents、LoadVideo、VOSR2ModelLoader、image_to_image_controlnet_face_detailer_lora
