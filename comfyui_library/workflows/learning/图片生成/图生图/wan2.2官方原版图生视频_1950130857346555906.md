---
key: 图片生成/图生图/wan2.2官方原版图生视频_1950130857346555906.json
name: wan2.2官方原版图生视频_1950130857346555906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2官方原版图生视频_1950130857346555906.json
hash: 6d786e0e4d3656ee
coverage: 0.741935
learned_at: 2026-10-23 11:46:07
nodes: [KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, UNETLoader, CLIPLoader, UNETLoader, CLIPTextEncode, PathchSageAttentionKJ, CFGZeroStar, VAEDecode, CreateVideo, WanImageToVideo, SaveVideo, easy showAnything, JjkText, easy showAnything, RH_Captioner, easy showAnything, ShowText|pysssss, JjkText, TextCombinerTwo, JjkText, easy anythingIndexSwitch, RH_Translator, LoadImage, TextCombinerTwo, RH_Prompter]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/wan2.2官方原版图生视频_1950130857346555906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2官方原版图生视频_1950130857346555906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（31 个）：
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `VAEDecode` ★核心
- `CreateVideo`
- `WanImageToVideo`
- `SaveVideo`
- `easy showAnything`
- `JjkText`
- `easy showAnything`
- `RH_Captioner`
- `easy showAnything`
- `ShowText|pysssss`
- `JjkText`
- `TextCombinerTwo`
- `JjkText`
- `easy anythingIndexSwitch`
- `RH_Translator`
- `LoadImage`
- `TextCombinerTwo`
- `RH_Prompter`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（23/31）

**有卡**：`KSamplerAdvanced`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`CFGZeroStar`、`VAEDecode`、`CreateVideo`、`WanImageToVideo`、`SaveVideo`、`RH_Captioner`、`TextCombinerTwo`、`easy anythingIndexSwitch`、`RH_Translator`、`LoadImage`、`RH_Prompter`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
