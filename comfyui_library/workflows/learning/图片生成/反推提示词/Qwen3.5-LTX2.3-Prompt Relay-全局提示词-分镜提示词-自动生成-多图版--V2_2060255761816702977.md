---
key: 图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版--V2_2060255761816702977.json
name: Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版--V2_2060255761816702977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版--V2_2060255761816702977.json
hash: 304d06d55d391659
coverage: 0.722222
learned_at: 2026-10-26 01:46:07
nodes: [SaveImage, LoadImage, MultiTextConcatenate, ttN concat, JjkText, ttN concat, RH_Utils, Int, JjkText, MarkdownNote, LoadImage, JjkText, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, easy showAnything, ShowAnything|Mie, Label (rgthree)]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版--V2_2060255761816702977.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-多图版--V2_2060255761816702977.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（18 个）：
- `SaveImage`
- `LoadImage`
- `MultiTextConcatenate`
- `ttN concat`
- `JjkText`
- `ttN concat`
- `RH_Utils`
- `Int`
- `JjkText`
- `MarkdownNote`
- `LoadImage`
- `JjkText`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `easy showAnything`
- `ShowAnything|Mie`
- `Label (rgthree)`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`SaveImage`、`LoadImage`、`MultiTextConcatenate`、`ttN concat`、`RH_Utils`、`Int`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ShowAnything|Mie`、`Label (rgthree)`

**用到的条目**：LoadImage、SaveImage、Int、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、MultiTextConcatenate、RH_Utils
