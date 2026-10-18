---
key: 视频生成/图生视频/wan2.2高低频首尾帧生视频低配电脑可下载本地部署_2076552090461229058.json
name: wan2.2高低频首尾帧生视频低配电脑可下载本地部署_2076552090461229058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2高低频首尾帧生视频低配电脑可下载本地部署_2076552090461229058.json
hash: a49a87c43546eef0
coverage: 0.947368
learned_at: 2026-10-15 22:41:31
nodes: [UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, VAELoader, CLIPLoader, KSamplerAdvanced, VAEDecode, CreateVideo, SaveVideo, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, WanFirstLastFrameToVideo, LoadImage, LoadImage, 孤海注释]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2高低频首尾帧生视频低配电脑可下载本地部署_2076552090461229058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076552090461229058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `LoadImage`
- `LoadImage`
- `孤海注释`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
