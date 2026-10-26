---
key: 图片生成/反推提示词/Qwen3.5多分镜描述_2055464852449177602.json
name: Qwen3.5多分镜描述_2055464852449177602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5多分镜描述_2055464852449177602.json
hash: c885655b8bdadd89
coverage: 0.9375
learned_at: 2026-10-26 01:46:10
nodes: [llama_cpp_parameters, Text Multiline, llama_cpp_instruct_adv, LoadImage, LoadImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ttN text, llama_cpp_model_loader, ImageBatchMulti, LoadImage, LoadImage, LoadImage, easy showAnything, easy saveText]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5多分镜描述_2055464852449177602.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5多分镜描述_2055464852449177602.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（16 个）：
- `llama_cpp_parameters`
- `Text Multiline`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ttN text`
- `llama_cpp_model_loader`
- `ImageBatchMulti`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `easy saveText`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`llama_cpp_parameters`、`Text Multiline`、`llama_cpp_instruct_adv`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ttN text`、`llama_cpp_model_loader`、`ImageBatchMulti`、`easy saveText`

**用到的条目**：LoadImage、easy saveText、ImageBatchMulti、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、LayerUtility: ImageScaleByAspectRatio V2、Text Multiline
