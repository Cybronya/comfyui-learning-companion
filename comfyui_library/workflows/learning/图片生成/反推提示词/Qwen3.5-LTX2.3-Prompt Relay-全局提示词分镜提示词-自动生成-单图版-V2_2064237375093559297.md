---
key: 图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词分镜提示词-自动生成-单图版-V2_2064237375093559297.json
name: Qwen3.5-LTX2.3-Prompt Relay-全局提示词分镜提示词-自动生成-单图版-V2_2064237375093559297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词分镜提示词-自动生成-单图版-V2_2064237375093559297.json
hash: 02a4f07167e23985
coverage: 0.8
learned_at: 2026-10-26 01:46:08
nodes: [SaveImage, LoadImage, RH_Utils, ttN concat, MultiTextConcatenate, ttN concat, RH_Utils, JjkText, ttN concat, Label (rgthree), JjkText, Int, Int, LoadImage, llama_cpp_parameters, easy cleanGpuUsed, easy showAnything, llama_cpp_model_loader, ShowAnything|Mie, RH_LLMAPI_Pro_Node, RHHiddenNodes, llama_cpp_instruct_adv, SaveText, easy showAnything, MarkdownNote]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词分镜提示词-自动生成-单图版-V2_2064237375093559297.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5-LTX2.3-Prompt Relay-全局提示词分镜提示词-自动生成-单图版-V2_2064237375093559297.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（25 个）：
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
- `JjkText`
- `Int`
- `Int`
- `LoadImage`
- `llama_cpp_parameters`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_model_loader`
- `ShowAnything|Mie`
- `RH_LLMAPI_Pro_Node`
- `RHHiddenNodes`
- `llama_cpp_instruct_adv`
- `SaveText`
- `easy showAnything`
- `MarkdownNote`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`SaveImage`、`LoadImage`、`RH_Utils`、`ttN concat`、`MultiTextConcatenate`、`Label (rgthree)`、`Int`、`llama_cpp_parameters`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`ShowAnything|Mie`、`RH_LLMAPI_Pro_Node`、`RHHiddenNodes`、`llama_cpp_instruct_adv`、`SaveText`

**用到的条目**：LoadImage、SaveImage、SaveText、Int、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、MultiTextConcatenate
