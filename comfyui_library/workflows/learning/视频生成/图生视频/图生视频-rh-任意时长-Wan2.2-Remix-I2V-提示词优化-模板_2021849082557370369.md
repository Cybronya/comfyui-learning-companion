---
key: 视频生成/图生视频/图生视频-rh-任意时长-Wan2.2-Remix-I2V-提示词优化-模板_2021849082557370369.json
name: 图生视频-rh-任意时长-Wan2.2-Remix-I2V-提示词优化-模板_2021849082557370369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2021849082557370369.json
hash: d4197a8e8f2d1281
coverage: 0.717391
learned_at: 2026-10-15 22:35:09
nodes: [KSamplerAdvanced, wanBlockSwap, ModelSamplingSD3, INTConstant, wanBlockSwap, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, VAELoader, Seed (rgthree), ImageResize+, UNETLoader, CLIPLoader, easy cleanGpuUsed, SetNode, INTConstant, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, SetNode, INTConstant, SetNode, SetNode, VAEDecode, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, INTConstant, UNETLoader, GetNode, INTConstant, ImageLoader, Qwen3_VQA, easy showAnything, CR Text Concatenate, PreviewAny, MathExpression|pysssss, ttN concat, Text Multiline (Code Compatible), IntToText, INTConstant, Note]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频-rh-任意时长-Wan2.2-Remix-I2V-提示词优化-模板_2021849082557370369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021849082557370369.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（46 个）：
- `KSamplerAdvanced` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `INTConstant`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `Seed (rgthree)`
- `ImageResize+`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy cleanGpuUsed`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RIFE VFI`
- `VHS_VideoCombine`
- `INTConstant`
- `UNETLoader` ★核心
- `GetNode`
- `INTConstant`
- `ImageLoader`
- `Qwen3_VQA`
- `easy showAnything`
- `CR Text Concatenate`
- `PreviewAny`
- `MathExpression|pysssss`
- `ttN concat`
- `Text Multiline (Code Compatible)`
- `IntToText`
- `INTConstant`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **72%**（33/46）

**有卡**：`KSamplerAdvanced`、`wanBlockSwap`、`ModelSamplingSD3`、`INTConstant`、`WanImageToVideo`、`VAELoader`、`Seed (rgthree)`、`ImageResize+`、`UNETLoader`、`CLIPLoader`、`easy cleanGpuUsed`、`CLIPTextEncode`、`VAEDecode`、`RIFE VFI`、`VHS_VideoCombine`、`ImageLoader`、`Qwen3_VQA`、`CR Text Concatenate`、`MathExpression|pysssss`、`ttN concat`、`Text Multiline (Code Compatible)`、`IntToText`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、ImageResize+
