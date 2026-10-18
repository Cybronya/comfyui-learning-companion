---
key: 视频生成/图生视频/wan2.1-FLF2v首尾帧视频（提示词扩写）_1915886168360026113.json
name: wan2.1-FLF2v首尾帧视频（提示词扩写）_1915886168360026113.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1-FLF2v首尾帧视频（提示词扩写）_1915886168360026113.json
hash: 9eba8cfc6e9c5b87
coverage: 0.591837
learned_at: 2026-10-15 22:29:38
nodes: [CLIPVisionLoader, GetNode, CLIPVisionEncode, CLIPVisionEncode, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, UNETLoader, ShowText|pysssss, GetNode, GetNode, Int, Int, WanFirstLastFrameToVideo, KSampler, Int, VAEDecode, VHS_VideoCombine, LoadImage, ImageResize+, ImageResize+, SetNode, SetNode, GetNode, VHS_VideoCombine, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, GetNode, GetNode, CLIPLoader, Anything Everywhere, VAELoader, Anything Everywhere, Note, Anything Everywhere, LoadImage, workflow>1, GetNode, RH_Prompter, RH_Translator, SetNode, AddLabel, AddLabel]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 765984275425297, "steps": 20}
---

# 视频生成/图生视频/wan2.1-FLF2v首尾帧视频（提示词扩写）_1915886168360026113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1915886168360026113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `CLIPVisionLoader`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `Int`
- `Int`
- `WanFirstLastFrameToVideo`
- `KSampler` ★核心
- `Int`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResize+`
- `ImageResize+`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `Anything Everywhere`
- `VAELoader`
- `Anything Everywhere`
- `Note`
- `Anything Everywhere`
- `LoadImage`
- `workflow>1`
- `GetNode`
- `RH_Prompter`
- `RH_Translator`
- `SetNode`
- `AddLabel`
- `AddLabel`

## 关键参数

- `seed` = `765984275425297`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（29/49）

**有卡**：`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`UNETLoader`、`Int`、`WanFirstLastFrameToVideo`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ImageResize+`、`EmptyImage`、`GetImageSizeAndCount`、`ImageConcatMulti`、`CLIPLoader`、`VAELoader`、`workflow>1`、`RH_Prompter`、`RH_Translator`、`AddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
