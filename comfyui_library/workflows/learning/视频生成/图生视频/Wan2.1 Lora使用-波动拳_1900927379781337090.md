---
key: 视频生成/图生视频/Wan2.1 Lora使用-波动拳_1900927379781337090.json
name: Wan2.1 Lora使用-波动拳_1900927379781337090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 Lora使用-波动拳_1900927379781337090.json
hash: 585ce6710dabaf11
coverage: 0.59375
learned_at: 2026-10-15 22:29:23
nodes: [SetNode, SetNode, GetNode, CLIPVisionEncode, CLIPTextEncode, GetNode, GetNode, GetNode, SetNode, SetNode, PreviewImage, GetNode, VHS_VideoCombine, LTXVPromptEnhancerLoader, VAEDecode, SetNode, WanImageToVideo, ImageScale, KSampler, SetNode, WanVideoTeaCacheKJ, VAELoader, CLIPVisionLoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoadImage, LTXVPromptEnhancer, ShowText|pysssss, CLIPTextEncode, CR Text Concatenate, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1002619976763373, "steps": 20}
---

# 视频生成/图生视频/Wan2.1 Lora使用-波动拳_1900927379781337090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1900927379781337090.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `VHS_VideoCombine`
- `LTXVPromptEnhancerLoader`
- `VAEDecode` ★核心
- `SetNode`
- `WanImageToVideo`
- `ImageScale`
- `KSampler` ★核心
- `SetNode`
- `WanVideoTeaCacheKJ`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LTXVPromptEnhancer`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `CR Text`

## 关键参数

- `seed` = `1002619976763373`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（19/32）

**有卡**：`CLIPVisionEncode`、`CLIPTextEncode`、`VHS_VideoCombine`、`LTXVPromptEnhancerLoader`、`VAEDecode`、`WanImageToVideo`、`ImageScale`、`KSampler`、`WanVideoTeaCacheKJ`、`VAELoader`、`CLIPVisionLoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`LTXVPromptEnhancer`、`CR Text Concatenate`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
