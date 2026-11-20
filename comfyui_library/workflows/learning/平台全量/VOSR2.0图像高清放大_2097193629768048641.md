---
key: 平台全量/VOSR2.0图像高清放大_2097193629768048641.json
name: VOSR2.0图像高清放大_2097193629768048641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VOSR2.0图像高清放大_2097193629768048641.json
hash: 54faaaab668f1110
coverage: 0.571429
learned_at: 2026-11-14 01:03:01
nodes: [VOSR2ModelLoader, SaveImage, Image Comparer (rgthree), MarkdownNote, VOSR2Upscale, PrimitiveInt, LoadImage]
patterns: []
missing: []
---

# 平台全量/VOSR2.0图像高清放大_2097193629768048641.json

> 来源文件 `comfyui_library/workflows/平台全量/VOSR2.0图像高清放大_2097193629768048641.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（7 个）：
- `VOSR2ModelLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `VOSR2Upscale`
- `PrimitiveInt`
- `LoadImage`

## 知识

覆盖率 **57%**（4/7）

**有卡**：`VOSR2ModelLoader`、`SaveImage`、`VOSR2Upscale`、`LoadImage`

**用到的条目**：LoadImage、VOSR2Upscale、SaveImage、VOSR2ModelLoader、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_inpaint_sampler_3、image_to_image_controlnet_inpaint_upscale
