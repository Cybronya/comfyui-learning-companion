---
key: 图片生成/反推提示词/qwen3.5 千问3.5 图片反推生成提示词文本工作流_2060646833801744386.json
name: qwen3.5 千问3.5 图片反推生成提示词文本工作流_2060646833801744386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.5 千问3.5 图片反推生成提示词文本工作流_2060646833801744386.json
hash: 26d7c72167b3996e
coverage: 0.833333
learned_at: 2026-10-26 01:46:58
nodes: [llama_cpp_model_loader, LoadImage, easy saveText, llama_cpp_instruct_adv, PreviewAny, ShowAnything|Mie]
patterns: []
missing: []
---

# 图片生成/反推提示词/qwen3.5 千问3.5 图片反推生成提示词文本工作流_2060646833801744386.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen3.5 千问3.5 图片反推生成提示词文本工作流_2060646833801744386.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（6 个）：
- `llama_cpp_model_loader`
- `LoadImage`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `ShowAnything|Mie`

## 知识

覆盖率 **83%**（5/6）

**有卡**：`llama_cpp_model_loader`、`LoadImage`、`easy saveText`、`llama_cpp_instruct_adv`、`ShowAnything|Mie`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、ShowAnything|Mie、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
