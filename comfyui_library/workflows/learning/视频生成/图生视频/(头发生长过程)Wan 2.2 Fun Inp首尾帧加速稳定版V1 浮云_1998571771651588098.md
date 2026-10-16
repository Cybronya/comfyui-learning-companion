---
key: 视频生成/图生视频/(头发生长过程)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1998571771651588098.json
name: (头发生长过程)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1998571771651588098.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998571771651588098.json
hash: 532e077220c4ae50
coverage: 0.895522
learned_at: 2026-10-15 22:33:32
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoadImage, LoadImage, WanFunInpaintToVideo, VAEDecode, CreateVideo, SaveVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, UNETLoader, WanFunInpaintToVideo, Note, MarkdownNote, CreateVideo, SaveVideo, CLIPTextEncode, CLIPTextEncode, MarkdownNote, Note, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, WanFunInpaintToVideo, Note, MarkdownNote, Note, CLIPTextEncode, VAEDecode, PDIMAGE_LongerSize, ImageConcanate, LoraLoaderModelOnly, VHS_VideoCombine, CR Prompt Text, ImageConcanate, JWInteger, LoraLoaderModelOnly, JWInteger, VHS_VideoCombine, CreateVideo, KSamplerAdvanced, LoadImage, LoadImage, KSamplerAdvanced, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/(头发生长过程)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1998571771651588098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998571771651588098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `WanFunInpaintToVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `WanFunInpaintToVideo`
- `Note`
- `MarkdownNote`
- `CreateVideo`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `WanFunInpaintToVideo`
- `Note`
- `MarkdownNote`
- `Note`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `CR Prompt Text`
- `ImageConcanate`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `VHS_VideoCombine`
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `JWInteger`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（60/67）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`WanFunInpaintToVideo`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`、`PDIMAGE_LongerSize`、`ImageConcanate`、`VHS_VideoCombine`、`CR Prompt Text`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
