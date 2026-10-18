---
key: 视频生成/图生视频/自己用：wan2.1_10个运镜lora_1940692152370311170.json
name: 自己用：wan2.1_10个运镜lora_1940692152370311170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/自己用：wan2.1_10个运镜lora_1940692152370311170.json
hash: 781e0b9c4bf4084e
coverage: 0.8125
learned_at: 2026-10-15 22:30:34
nodes: [CLIPVisionLoader, VAELoader, ModelSamplingSD3, CLIPVisionEncode, easy showAnything, SimpleMath+, Note, CR String To Combo, SplitStringByDelimiter, LoraLoaderModelOnly, JoinStrings, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAEDecode, KSampler, MarkdownNote, WanImageToVideo, ImageResizeKJ, RH_Captioner, RH_LLMAPI_NODE, ShowText|pysssss, ImpactInt, UNETLoader, ImpactStringSelector, ShowText|pysssss, ShowText|pysssss, ImpactInt, VHS_VideoCombine, ImpactInt, LoadImage, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 782778016020910, "steps": 20}
---

# 视频生成/图生视频/自己用：wan2.1_10个运镜lora_1940692152370311170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1940692152370311170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `CLIPVisionLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `easy showAnything`
- `SimpleMath+`
- `Note`
- `CR String To Combo`
- `SplitStringByDelimiter`
- `LoraLoaderModelOnly` ★核心
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `WanImageToVideo`
- `ImageResizeKJ`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `ImpactInt`
- `UNETLoader` ★核心
- `ImpactStringSelector`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ImpactInt`
- `VHS_VideoCombine`
- `ImpactInt`
- `LoadImage`
- `ImpactInt`

## 关键参数

- `seed` = `782778016020910`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`CLIPVisionLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPVisionEncode`、`SimpleMath+`、`CR String To Combo`、`SplitStringByDelimiter`、`LoraLoaderModelOnly`、`JoinStrings`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`KSampler`、`WanImageToVideo`、`ImageResizeKJ`、`RH_Captioner`、`RH_LLMAPI_NODE`、`ImpactInt`、`UNETLoader`、`ImpactStringSelector`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
