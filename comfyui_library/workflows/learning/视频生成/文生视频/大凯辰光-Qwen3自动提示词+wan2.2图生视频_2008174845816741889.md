---
key: 视频生成/文生视频/大凯辰光-Qwen3自动提示词+wan2.2图生视频_2008174845816741889.json
name: 大凯辰光-Qwen3自动提示词+wan2.2图生视频_2008174845816741889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/大凯辰光-Qwen3自动提示词+wan2.2图生视频_2008174845816741889.json
hash: fc29f0e4fbc111a4
coverage: 0.909091
learned_at: 2026-10-15 22:48:31
nodes: [CLIPTextEncode, VAEDecode, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Seed (rgthree), ShowText|pysssss, easy cleanGpuUsed, Any To String (mtb), WanImageToVideo, ImageResize+, ModelSamplingSD3, LoraLoaderModelOnly, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, INTConstant, Note, CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoadImage, Qwen3_VQA, CLIPTextEncode, easy textSwitch, Note, Textbox]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
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

覆盖率 **91%**（30/33）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`INTConstant`、`Seed (rgthree)`、`easy cleanGpuUsed`、`Any To String (mtb)`、`WanImageToVideo`、`ImageResize+`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`Qwen3_VQA`、`easy textSwitch`、`Textbox`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
