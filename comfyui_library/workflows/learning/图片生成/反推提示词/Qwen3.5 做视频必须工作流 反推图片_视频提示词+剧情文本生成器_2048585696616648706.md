---
key: 图片生成/反推提示词/Qwen3.5 做视频必须工作流 反推图片_视频提示词+剧情文本生成器_2048585696616648706.json
name: Qwen3.5 做视频必须工作流 反推图片_视频提示词+剧情文本生成器_2048585696616648706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 做视频必须工作流 反推图片_视频提示词+剧情文本生成器_2048585696616648706.json
hash: 24cbea4f5792e918
coverage: 0.789474
learned_at: 2026-10-26 01:46:05
nodes: [llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, llama_cpp_model_loader, llama_cpp_instruct_adv, easy saveText, PreviewAny, llama_cpp_instruct_adv, easy saveText, VHS_LoadVideo, LoadImage, llama_cpp_instruct_adv, easy saveText, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, Fast Groups Bypasser (rgthree), CR Text]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5 做视频必须工作流 反推图片_视频提示词+剧情文本生成器_2048585696616648706.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5 做视频必须工作流 反推图片_视频提示词+剧情文本生成器_2048585696616648706.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（19 个）：
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `VHS_LoadVideo`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PreviewAny`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`easy saveText`、`VHS_LoadVideo`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo、CR Text、sd15-t2i-basic
