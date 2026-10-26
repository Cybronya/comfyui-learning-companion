---
key: 图片生成/反推提示词/qwen3.5 千问3.5 图片反推生成提示词文本工作流_2102722770957328386.json
name: qwen3.5 千问3.5 图片反推生成提示词文本工作流_2102722770957328386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.5 千问3.5 图片反推生成提示词文本工作流_2102722770957328386.json
hash: cc0c0ed49e364831
coverage: 0.8
learned_at: 2026-10-26 01:46:59
nodes: [llama_cpp_model_loader, llama_cpp_instruct_adv, easy saveText, PreviewAny, LoadImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/qwen3.5 千问3.5 图片反推生成提示词文本工作流_2102722770957328386.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen3.5 千问3.5 图片反推生成提示词文本工作流_2102722770957328386.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（5 个）：
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `PreviewAny`
- `LoadImage`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`easy saveText`、`LoadImage`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint、sdxl_portrait_controlnet_lora_sampler
