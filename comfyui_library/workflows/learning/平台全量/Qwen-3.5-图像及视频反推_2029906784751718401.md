---
key: 平台全量/Qwen-3.5-图像及视频反推_2029906784751718401.json
name: Qwen-3.5-图像及视频反推_2029906784751718401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-3.5-图像及视频反推_2029906784751718401.json
hash: ca137c6fd825bff4
coverage: 0.8
learned_at: 2026-11-14 00:51:04
nodes: [PreviewAny, easy saveText, LoadImage, llama_cpp_model_loader, PreviewAny, easy saveText, llama_cpp_model_loader, llama_cpp_instruct_adv, VHS_LoadVideo, llama_cpp_instruct_adv]
patterns: []
missing: []
---

# 平台全量/Qwen-3.5-图像及视频反推_2029906784751718401.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-3.5-图像及视频反推_2029906784751718401.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `PreviewAny`
- `easy saveText`
- `LoadImage`
- `llama_cpp_model_loader`
- `PreviewAny`
- `easy saveText`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `VHS_LoadVideo`
- `llama_cpp_instruct_adv`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`easy saveText`、`LoadImage`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`VHS_LoadVideo`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、VHS_LoadVideo、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_face_detailer_sampler
