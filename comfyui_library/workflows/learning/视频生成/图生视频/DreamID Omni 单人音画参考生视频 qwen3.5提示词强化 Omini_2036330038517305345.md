---
key: 视频生成/图生视频/DreamID Omni 单人音画参考生视频 qwen3.5提示词强化 Omini_2036330038517305345.json
name: DreamID Omni 单人音画参考生视频 qwen3.5提示词强化 Omini_2036330038517305345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/DreamID Omni 单人音画参考生视频 qwen3.5提示词强化 Omini_2036330038517305345.json
hash: 041a4e8197f5a766
coverage: 0.823529
learned_at: 2026-10-15 22:35:51
nodes: [SaveVideo, SoundFlow_TrimAudio, SoundFlow_TrimAudio, llama_cpp_parameters, llama_cpp_model_loader, SaveVideo, RunningHub DreamID-Omni Sampler, easy getNode, llama_cpp_parameters, RunningHub DreamID-Omni Sampler, easy showAnything, LoadImage, Image Batch, LoadImage, llama_cpp_instruct_adv, llama_cpp_model_loader, ImageResize+, easy getNode, Int, Int, ImageResize+, llama_cpp_instruct_adv, JjkText, LoadAudio, LoadAudio, easy setNode, easy setNode, easy showAnything, Note, easy getNode, easy getNode, JjkText, Fast Groups Bypasser (rgthree), RunningHub DreamID-Omni Loader]
patterns: []
missing: []
---

# 视频生成/图生视频/DreamID Omni 单人音画参考生视频 qwen3.5提示词强化 Omini_2036330038517305345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036330038517305345.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（34 个）：
- `SaveVideo`
- `SoundFlow_TrimAudio`
- `SoundFlow_TrimAudio`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `SaveVideo`
- `RunningHub DreamID-Omni Sampler` ★核心
- `easy getNode`
- `llama_cpp_parameters`
- `RunningHub DreamID-Omni Sampler` ★核心
- `easy showAnything`
- `LoadImage`
- `Image Batch`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `ImageResize+`
- `easy getNode`
- `Int`
- `Int`
- `ImageResize+`
- `llama_cpp_instruct_adv`
- `JjkText`
- `LoadAudio`
- `LoadAudio`
- `easy setNode`
- `easy setNode`
- `easy showAnything`
- `Note`
- `easy getNode`
- `easy getNode`
- `JjkText`
- `Fast Groups Bypasser (rgthree)`
- `RunningHub DreamID-Omni Loader`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`SaveVideo`、`SoundFlow_TrimAudio`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`RunningHub DreamID-Omni Sampler`、`easy getNode`、`LoadImage`、`Image Batch`、`llama_cpp_instruct_adv`、`ImageResize+`、`Int`、`LoadAudio`、`easy setNode`、`RunningHub DreamID-Omni Loader`

**用到的条目**：LoadImage、RunningHub DreamID-Omni Sampler、ImageResize+、SaveVideo、Int、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters
