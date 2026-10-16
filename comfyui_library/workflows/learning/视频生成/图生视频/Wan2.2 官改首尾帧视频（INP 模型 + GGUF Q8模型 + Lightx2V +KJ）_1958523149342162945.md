---
key: 视频生成/图生视频/Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json
name: Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958523149342162945.json
hash: 1a62f8c7c1873cd4
coverage: 0.844444
learned_at: 2026-10-15 22:31:22
nodes: [LoadImage, Note, RIFE VFI, Int, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, LoadImage, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, WanFirstLastFrameToVideo, LayerUtility: ImageMaskScaleAs, MarkdownNote, VAEDecode, MarkdownNote, MarkdownNote, JWFloat, JWInteger, JWInteger, KSamplerAdvanced, KSamplerAdvanced, JWFloat, CLIPLoader, VAELoader, PrimitiveInt, UnetLoaderGGUF, UnetLoaderGGUF, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, JWInteger, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, UNETLoader, UNETLoader, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 0, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958523149342162945.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（45 个）：
- `LoadImage`
- `Note`
- `RIFE VFI`
- `Int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanFirstLastFrameToVideo`
- `LayerUtility: ImageMaskScaleAs`
- `MarkdownNote`
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `JWFloat`
- `JWInteger`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWFloat`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `0`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`LoadImage`、`RIFE VFI`、`Int`、`UNETLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`easy cleanGpuUsed`、`WanFirstLastFrameToVideo`、`LayerUtility: ImageMaskScaleAs`、`VAEDecode`、`JWFloat`、`JWInteger`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
