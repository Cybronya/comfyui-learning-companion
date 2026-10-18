---
key: 视频生成/图生视频/Qwen3自动提示词+wan2.2图生视频N版_2011091224547037185.json
name: Qwen3自动提示词+wan2.2图生视频N版_2011091224547037185.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen3自动提示词+wan2.2图生视频N版_2011091224547037185.json
hash: fac72d45f2c55a1f
coverage: 0.914286
learned_at: 2026-10-15 22:34:21
nodes: [CLIPTextEncode, ModelSamplingSD3, KSamplerAdvanced, INTConstant, INTConstant, Seed (rgthree), ShowText|pysssss, easy cleanGpuUsed, Any To String (mtb), WanImageToVideo, ImageResize+, ModelSamplingSD3, LoraLoaderModelOnly, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, CLIPLoader, UNETLoader, UNETLoader, Qwen3_VQA, CLIPTextEncode, easy textSwitch, Note, Textbox, INTConstant, INTConstant, INTConstant, VAELoader, VAEDecodeTiled, TT_img_enc, SaveLatent, KSamplerAdvanced, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Qwen3自动提示词+wan2.2图生视频N版_2011091224547037185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011091224547037185.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
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
- `Note`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `easy textSwitch`
- `Note`
- `Textbox`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `TT_img_enc`
- `SaveLatent`
- `KSamplerAdvanced` ★核心
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`INTConstant`、`Seed (rgthree)`、`easy cleanGpuUsed`、`Any To String (mtb)`、`WanImageToVideo`、`ImageResize+`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`CLIPLoader`、`UNETLoader`、`Qwen3_VQA`、`easy textSwitch`、`Textbox`、`VAELoader`、`VAEDecodeTiled`、`TT_img_enc`、`SaveLatent`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
