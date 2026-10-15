---
key: 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json
name: Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json
hash: 325180442f88b0a9
coverage: 0.9375
learned_at: 2026-10-15 22:44:02
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, CLIPTextEncode, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, VHS_VideoCombine, UNETLoader, CLIPLoader, VAELoader, WanImageToVideo, LoraLoaderModelOnly, UNETLoader, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`WanImageToVideo`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
