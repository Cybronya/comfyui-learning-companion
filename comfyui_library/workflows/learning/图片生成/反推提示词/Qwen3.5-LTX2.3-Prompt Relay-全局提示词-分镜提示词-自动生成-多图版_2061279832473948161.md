---
key: 图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版_2061279832473948161.json
name: Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版_2061279832473948161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版_2061279832473948161.json
hash: d171fa700dde0c9b
coverage: 0.625
learned_at: 2026-10-26 01:46:07
nodes: [JjkText, RH_Utils, ttN concat, MultiImageLoader, ttN concat, MultiTextConcatenate, PrimitiveInt, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, easy saveText, PreviewImage, ImageConcatFromBatch, PrimitiveStringMultiline, easy showAnything, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版_2061279832473948161.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版_2061279832473948161.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（16 个）：
- `JjkText`
- `RH_Utils`
- `ttN concat`
- `MultiImageLoader`
- `ttN concat`
- `MultiTextConcatenate`
- `PrimitiveInt`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `PreviewImage`
- `ImageConcatFromBatch`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **62%**（10/16）

**有卡**：`RH_Utils`、`ttN concat`、`MultiImageLoader`、`MultiTextConcatenate`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`easy saveText`、`ImageConcatFromBatch`

**用到的条目**：easy saveText、ImageConcatFromBatch、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、MultiTextConcatenate、RH_Utils、MultiImageLoader
