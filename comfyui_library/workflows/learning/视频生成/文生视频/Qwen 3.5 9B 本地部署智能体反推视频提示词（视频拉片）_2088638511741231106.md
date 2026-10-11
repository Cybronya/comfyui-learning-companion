---
key: 视频生成/文生视频/Qwen 3.5 9B 本地部署智能体反推视频提示词（视频拉片）_2088638511741231106.json
name: Qwen 3.5 9B 本地部署智能体反推视频提示词（视频拉片）_2088638511741231106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen 3.5 9B 本地部署智能体反推视频提示词（视频拉片）_2088638511741231106.json
hash: 55f8d384877c3c4f
coverage: 0.733333
learned_at: 2026-10-11 20:53:47
nodes: [CR Text Concatenate, llama_cpp_parameters, Text, CR Prompt Text, llama_cpp_instruct_adv, easy showAnything, LoadImage, LoadImage, MarkdownNote, PixaromaLabel, PixaromaLabel, llama_cpp_model_loader, LoadVideoUI, ImageFromBatch, SaveImage]
patterns: []
missing: [CR Text Concatenate, CR Prompt Text]
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Qwen 3.5 9B 本地部署智能体反推视频提示词（视频拉片）_2088638511741231106.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen 3.5 9B 本地部署智能体反推视频提示词（视频拉片）_2088638511741231106.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（15 个）：
- `CR Text Concatenate`
- `llama_cpp_parameters`
- `Text`
- `CR Prompt Text`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `PixaromaLabel`
- `PixaromaLabel`
- `llama_cpp_model_loader`
- `LoadVideoUI`
- `ImageFromBatch`
- `SaveImage`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`llama_cpp_parameters`、`Text`、`llama_cpp_instruct_adv`、`LoadImage`、`PixaromaLabel`、`llama_cpp_model_loader`、`LoadVideoUI`、`ImageFromBatch`、`SaveImage`

**缺卡**（2）：`CR Text Concatenate`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveImage、ImageFromBatch、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、PixaromaLabel、Text

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
