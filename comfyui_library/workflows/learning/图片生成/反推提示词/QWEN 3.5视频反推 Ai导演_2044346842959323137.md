---
key: 图片生成/反推提示词/QWEN 3.5视频反推 Ai导演_2044346842959323137.json
name: QWEN 3.5视频反推 Ai导演_2044346842959323137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/QWEN 3.5视频反推 Ai导演_2044346842959323137.json
hash: 736fb618ce373e74
coverage: 0.875
learned_at: 2026-10-26 01:45:48
nodes: [PreviewAny, easy saveText, easy cleanGpuUsed, llama_cpp_parameters, llama_cpp_model_loader, GetVideoComponents, LoadVideo, llama_cpp_instruct_adv]
patterns: []
missing: []
---

# 图片生成/反推提示词/QWEN 3.5视频反推 Ai导演_2044346842959323137.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/QWEN 3.5视频反推 Ai导演_2044346842959323137.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `PreviewAny`
- `easy saveText`
- `easy cleanGpuUsed`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `GetVideoComponents`
- `LoadVideo`
- `llama_cpp_instruct_adv`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`easy saveText`、`easy cleanGpuUsed`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`GetVideoComponents`、`LoadVideo`、`llama_cpp_instruct_adv`

**用到的条目**：easy saveText、GetVideoComponents、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、LoadVideo、easy cleanGpuUsed、sd15-t2i-basic
