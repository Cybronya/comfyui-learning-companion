---
key: 视频生成/图生视频/Wan2.2-InP首尾帧-ComfyUI官方 (v1)_1957255296970317825.json
name: Wan2.2-InP首尾帧-ComfyUI官方 (v1)_1957255296970317825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-InP首尾帧-ComfyUI官方 (v1)_1957255296970317825.json
hash: b73ee8bfc65b7ae3
coverage: 0.837209
learned_at: 2026-10-15 22:31:16
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CLIPLoader, VAELoader, UNETLoader, UNETLoader, WanFunInpaintToVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, WanFunInpaintToVideo, KSamplerAdvanced, PrimitiveInt, PrimitiveInt, MarkdownNote, Note, Note, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, VAEDecode, SaveVideo, CreateVideo, PreViewVideo, VAEDecode, CreateVideo, CLIPTextEncode, SaveVideo, LoadImage, LoadImage, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-InP首尾帧-ComfyUI官方 (v1)_1957255296970317825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957255296970317825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（43 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanFunInpaintToVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFunInpaintToVideo`
- `KSamplerAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `Note`
- `Note`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveVideo`
- `CreateVideo`
- `PreViewVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `Text Multiline`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（36/43）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`WanFunInpaintToVideo`、`LoraLoaderModelOnly`、`LoadImage`、`VAEDecode`、`SaveVideo`、`CreateVideo`、`PreViewVideo`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
