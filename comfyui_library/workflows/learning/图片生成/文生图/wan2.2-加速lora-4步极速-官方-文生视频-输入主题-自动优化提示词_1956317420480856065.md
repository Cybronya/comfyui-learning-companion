---
key: 图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json
name: wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json
hash: 737f429303e5117b
coverage: 0.862069
learned_at: 2026-10-15 22:27:58
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, CreateVideo, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, SaveVideo, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, KSamplerAdvanced, CLIPTextEncode, MarkdownNote, CR Text Replace, Int, Int, SimpleMath+, Int, TextBox, easy showAnything, RH_Prompter, easy showAnything, easy cleanGpuUsed, CLIPTextEncode, TextBox]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `CR Text Replace`
- `Int`
- `Int`
- `SimpleMath+`
- `Int`
- `TextBox`
- `easy showAnything`
- `RH_Prompter`
- `easy showAnything`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `TextBox`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`CreateVideo`、`ModelSamplingSD3`、`SaveVideo`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`CR Text Replace`、`Int`、`SimpleMath+`、`TextBox`、`RH_Prompter`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
