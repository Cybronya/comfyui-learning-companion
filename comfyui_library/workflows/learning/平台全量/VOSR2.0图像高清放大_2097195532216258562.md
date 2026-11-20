---
key: 平台全量/VOSR2.0图像高清放大_2097195532216258562.json
name: VOSR2.0图像高清放大_2097195532216258562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VOSR2.0图像高清放大_2097195532216258562.json
hash: 770e5d9efbfc1ce8
coverage: 0.571429
learned_at: 2026-11-14 01:03:02
nodes: [VOSR2ModelLoader, SaveImage, Image Comparer (rgthree), VOSR2Upscale, PrimitiveInt, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/VOSR2.0图像高清放大_2097195532216258562.json

> 来源文件 `comfyui_library/workflows/平台全量/VOSR2.0图像高清放大_2097195532216258562.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（7 个）：
- `VOSR2ModelLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VOSR2Upscale`
- `PrimitiveInt`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **57%**（4/7）

**有卡**：`VOSR2ModelLoader`、`SaveImage`、`VOSR2Upscale`、`LoadImage`

**用到的条目**：LoadImage、VOSR2Upscale、SaveImage、VOSR2ModelLoader、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_inpaint_sampler_3、image_to_image_controlnet_inpaint_upscale
