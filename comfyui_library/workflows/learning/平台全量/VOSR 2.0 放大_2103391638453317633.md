---
key: 平台全量/VOSR 2.0 放大_2103391638453317633.json
name: VOSR 2.0 放大_2103391638453317633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VOSR 2.0 放大_2103391638453317633.json
hash: 9ff7e68d2600d00a
coverage: 0.833333
learned_at: 2026-11-14 01:02:49
nodes: [LoadImage, SaveImage, Image Comparer (rgthree), VOSR2Upscale, VOSR2ModelLoader, Int]
patterns: []
missing: []
---

# 平台全量/VOSR 2.0 放大_2103391638453317633.json

> 来源文件 `comfyui_library/workflows/平台全量/VOSR 2.0 放大_2103391638453317633.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（6 个）：
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `Int`

## 知识

覆盖率 **83%**（5/6）

**有卡**：`LoadImage`、`SaveImage`、`VOSR2Upscale`、`VOSR2ModelLoader`、`Int`

**用到的条目**：LoadImage、VOSR2Upscale、SaveImage、Int、VOSR2ModelLoader、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_inpaint_sampler_3
