---
key: 图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json
name: wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json
hash: 737f429303e5117b
coverage: 0.758621
learned_at: 2026-10-10 20:59:27
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, CreateVideo, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, SaveVideo, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, KSamplerAdvanced, CLIPTextEncode, MarkdownNote, CR Text Replace, Int, Int, SimpleMath+, Int, TextBox, easy showAnything, RH_Prompter, easy showAnything, easy cleanGpuUsed, CLIPTextEncode, TextBox]
patterns: []
missing: [CR Text Replace, SimpleMath+, easy cleanGpuUsed]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2-加速lora-4步极速-官方-文生视频-输入主题-自动优化提示词_1956317420480856065.json`

## 结构

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `VAEDecode`
- `CreateVideo`
- `UNETLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `SaveVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `CLIPTextEncode`
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
- `CLIPTextEncode`
- `TextBox`

## 关键参数

- `cfg` = `4`
- `denoise` = `simple`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `seed` = `disable`
- `steps` = `fixed`

## 知识

覆盖率 **76%**（22/29）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`CreateVideo`、`ModelSamplingSD3`、`MarkdownNote`、`SaveVideo`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`CR Text Replace`、`Int`、`SimpleMath+`

**缺卡**（3）：`CR Text Replace`、`SimpleMath+`、`easy cleanGpuUsed`

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
