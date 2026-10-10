---
key: 视频生成/文生视频/大凯辰光-Qwen3自动提示词+wan2.2图生视频_2008174845816741889.json
name: 大凯辰光-Qwen3自动提示词+wan2.2图生视频_2008174845816741889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/大凯辰光-Qwen3自动提示词+wan2.2图生视频_2008174845816741889.json
hash: fc29f0e4fbc111a4
coverage: 0.757576
learned_at: 2026-10-10 23:12:16
nodes: [CLIPTextEncode, VAEDecode, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Seed (rgthree), ShowText|pysssss, easy cleanGpuUsed, Any To String (mtb), WanImageToVideo, ImageResize+, ModelSamplingSD3, LoraLoaderModelOnly, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, INTConstant, Note, CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoadImage, Qwen3_VQA, CLIPTextEncode, easy textSwitch, Note, Textbox]
patterns: []
missing: [Any To String (mtb), easy cleanGpuUsed, easy textSwitch, ImageResize+, Seed (rgthree)]
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/大凯辰光-Qwen3自动提示词+wan2.2图生视频_2008174845816741889.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/大凯辰光-Qwen3自动提示词+wan2.2图生视频_2008174845816741889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `WanImageToVideo`
- `ImageResize+`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `easy textSwitch`
- `Note`
- `Textbox`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（25/33）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`INTConstant`、`WanImageToVideo`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`Qwen3_VQA`、`Textbox`

**缺卡**（5）：`Any To String (mtb)`、`easy cleanGpuUsed`、`easy textSwitch`、`ImageResize+`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
