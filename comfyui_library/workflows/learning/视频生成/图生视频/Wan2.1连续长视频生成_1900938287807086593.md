---
key: 视频生成/图生视频/Wan2.1连续长视频生成_1900938287807086593.json
name: Wan2.1连续长视频生成_1900938287807086593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1900938287807086593.json
hash: 72cd272936468bb1
coverage: 0.55102
learned_at: 2026-10-15 22:29:23
nodes: [WanVideoTeaCacheKJ, SetNode, SetNode, GetNode, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, KSampler, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, CLIPVisionEncode, KSampler, VAEDecode, SetNode, PreviewImage, ShowText|pysssss, PreviewImage, VHS_VideoCombine, GetNode, VHS_VideoCombine, GetNode, LTXVPromptEnhancerLoader, LTXVPromptEnhancer, ShowText|pysssss, VAEDecode, SetNode, GetNode, GetImageSizeAndCount, MathExpression|pysssss, ImageFromBatch, LTXVPromptEnhancer, SetNode, UnetLoaderGGUF, CLIPLoader, VAELoader, CLIPVisionLoader, WanImageToVideo, WanImageToVideo, LoadImage, ImageScale]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 64687711273995, "steps": 20}
---

# 视频生成/图生视频/Wan2.1连续长视频生成_1900938287807086593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1900938287807086593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `WanVideoTeaCacheKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPVisionEncode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `PreviewImage`
- `ShowText|pysssss`
- `PreviewImage`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `LTXVPromptEnhancerLoader`
- `LTXVPromptEnhancer`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `LTXVPromptEnhancer`
- `SetNode`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `WanImageToVideo`
- `WanImageToVideo`
- `LoadImage`
- `ImageScale`

## 关键参数

- `seed` = `64687711273995`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **55%**（27/49）

**有卡**：`WanVideoTeaCacheKJ`、`CLIPVisionEncode`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`LTXVPromptEnhancerLoader`、`LTXVPromptEnhancer`、`GetImageSizeAndCount`、`MathExpression|pysssss`、`ImageFromBatch`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`WanImageToVideo`、`LoadImage`、`ImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode、CLIPVisionLoader
