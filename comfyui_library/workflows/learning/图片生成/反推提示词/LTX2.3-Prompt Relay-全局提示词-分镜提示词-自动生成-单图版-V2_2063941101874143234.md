---
key: 图片生成/反推提示词/LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-单图版-V2_2063941101874143234.json
name: LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-单图版-V2_2063941101874143234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-单图版-V2_2063941101874143234.json
hash: 208bddedfc061a8c
coverage: 0.818182
learned_at: 2026-10-26 01:45:30
nodes: [SaveImage, LoadImage, RH_Utils, ttN concat, MultiTextConcatenate, ttN concat, RH_Utils, JjkText, ttN concat, Label (rgthree), MarkdownNote, LoadImage, JjkText, llama_cpp_model_loader, llama_cpp_parameters, easy showAnything, Int, Int, RH_LLMAPI_Pro_Node, RHHiddenNodes, llama_cpp_instruct_adv, ShowAnything|Mie]
patterns: []
missing: []
---

# 图片生成/反推提示词/LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-单图版-V2_2063941101874143234.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/LTX2.3-Prompt Relay-全局提示词-分镜提示词-自动生成-单图版-V2_2063941101874143234.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（22 个）：
- `SaveImage`
- `LoadImage`
- `RH_Utils`
- `ttN concat`
- `MultiTextConcatenate`
- `ttN concat`
- `RH_Utils`
- `JjkText`
- `ttN concat`
- `Label (rgthree)`
- `MarkdownNote`
- `LoadImage`
- `JjkText`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `easy showAnything`
- `Int`
- `Int`
- `RH_LLMAPI_Pro_Node`
- `RHHiddenNodes`
- `llama_cpp_instruct_adv`
- `ShowAnything|Mie`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`SaveImage`、`LoadImage`、`RH_Utils`、`ttN concat`、`MultiTextConcatenate`、`Label (rgthree)`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`Int`、`RH_LLMAPI_Pro_Node`、`RHHiddenNodes`、`llama_cpp_instruct_adv`、`ShowAnything|Mie`

**用到的条目**：LoadImage、SaveImage、Int、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、MultiTextConcatenate、RH_LLMAPI_Pro_Node
