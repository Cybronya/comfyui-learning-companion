---
key: 视频生成/文生视频/【大炮视频】wan2.1_10个运镜lora 简单方便，让你图生视频充满灵性~_1931150479697620994.json
name: 【大炮视频】wan2.1_10个运镜lora 简单方便，让你图生视频充满灵性~_1931150479697620994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1931150479697620994.json
hash: 900729f81553e562
coverage: 0.8
learned_at: 2026-10-15 22:43:26
nodes: [CLIPVisionLoader, VAELoader, ModelSamplingSD3, CLIPVisionEncode, easy showAnything, SimpleMath+, Note, Note Plus (mtb), Note, CR String To Combo, SplitStringByDelimiter, LoraLoaderModelOnly, JoinStrings, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAEDecode, KSampler, MarkdownNote, WanImageToVideo, ImageResizeKJ, RH_Captioner, RH_LLMAPI_NODE, ShowText|pysssss, Note Plus (mtb), ImpactInt, UNETLoader, ImpactInt, ImpactStringSelector, ShowText|pysssss, ShowText|pysssss, LoadImage, ImpactInt, ImpactInt, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 512966991795667, "steps": 20}
---

# 视频生成/文生视频/【大炮视频】wan2.1_10个运镜lora 简单方便，让你图生视频充满灵性~_1931150479697620994.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1931150479697620994.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `CLIPVisionLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `easy showAnything`
- `SimpleMath+`
- `Note`
- `Note Plus (mtb)`
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
- `Note Plus (mtb)`
- `ImpactInt`
- `UNETLoader` ★核心
- `ImpactInt`
- `ImpactStringSelector`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `512966991795667`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`CLIPVisionLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPVisionEncode`、`SimpleMath+`、`Note Plus (mtb)`、`CR String To Combo`、`SplitStringByDelimiter`、`LoraLoaderModelOnly`、`JoinStrings`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`KSampler`、`WanImageToVideo`、`ImageResizeKJ`、`RH_Captioner`、`RH_LLMAPI_NODE`、`ImpactInt`、`UNETLoader`、`ImpactStringSelector`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
