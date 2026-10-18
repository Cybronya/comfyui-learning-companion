---
key: 视频生成/图生视频/wan2.2-GGUF+SmoothMix图生视频工作流_2006660938727952385.json
name: wan2.2-GGUF+SmoothMix图生视频工作流_2006660938727952385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-GGUF+SmoothMix图生视频工作流_2006660938727952385.json
hash: f39985f2a360aa1c
coverage: 0.928571
learned_at: 2026-10-15 22:34:02
nodes: [VHS_VideoCombine, CLIPTextEncode, KSamplerAdvanced, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, easy cleanGpuUsed, CLIPVisionEncode, CLIPVisionLoader, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, UNETLoader, UNETLoader, CLIPTextEncode, easy showAnything, mxSlider2D, ImageScaleBy, WanImageToVideo, KSamplerAdvanced, Seed (rgthree), VHS_VideoCombine, PreviewImage, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, CR Text List To String, ImageResizeKJv2, easy cleanGpuUsed, VAEDecode, Pick From Batch (mtb), easy cleanGpuUsed, RIFE VFI, ColorMatch, ImageScaleBy, SaveImage, Qwen3_VQA, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-GGUF+SmoothMix图生视频工作流_2006660938727952385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006660938727952385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `mxSlider2D`
- `ImageScaleBy`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `PreviewImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CR Text List To String`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `ColorMatch`
- `ImageScaleBy`
- `SaveImage`
- `Qwen3_VQA`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（39/42）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`UnetLoaderGGUF`、`UNETLoader`、`mxSlider2D`、`ImageScaleBy`、`WanImageToVideo`、`Seed (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`CR Text List To String`、`ImageResizeKJv2`、`VAEDecode`、`Pick From Batch (mtb)`、`RIFE VFI`、`ColorMatch`、`SaveImage`、`Qwen3_VQA`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
