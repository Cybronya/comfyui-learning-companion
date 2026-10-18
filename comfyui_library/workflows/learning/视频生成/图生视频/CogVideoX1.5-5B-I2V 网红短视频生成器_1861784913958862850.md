---
key: 视频生成/图生视频/CogVideoX1.5-5B-I2V 网红短视频生成器_1861784913958862850.json
name: CogVideoX1.5-5B-I2V 网红短视频生成器_1861784913958862850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/CogVideoX1.5-5B-I2V 网红短视频生成器_1861784913958862850.json
hash: 04c0d12df7d4ec07
coverage: 0.820513
learned_at: 2026-10-15 22:29:14
nodes: [PrimitiveNode, easy cleanGpuUsed, PrimitiveNode, FluxGuidance, ModelSamplingFlux, BasicGuider, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, RandomNoise, CLIPLoader, CogVideoTextEncode, CogVideoImageEncode, ImageResizeKJ, CogVideoSampler, CogVideoDecode, VAEDecode, EmptySD3LatentImage, CogVideoTextEncode, CLIPTextEncode, VAELoader, Note, Fast Groups Muter (rgthree), SaveImage, Reroute, RIFE VFI, VHS_VideoCombine, UNETLoader, Joy_caption_load, Joy_caption, easy cleanGpuUsed, ShowText|pysssss, LoraLoaderModelOnly, ShowText|pysssss, RH_Captioner, LoadImage, DualCLIPLoader, DownloadAndLoadCogVideoModel, VideoCombine_Adv]
patterns: []
missing: []
---

# 视频生成/图生视频/CogVideoX1.5-5B-I2V 网红短视频生成器_1861784913958862850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1861784913958862850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `PrimitiveNode`
- `easy cleanGpuUsed`
- `PrimitiveNode`
- `FluxGuidance`
- `ModelSamplingFlux`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `CLIPLoader`
- `CogVideoTextEncode`
- `CogVideoImageEncode`
- `ImageResizeKJ`
- `CogVideoSampler` ★核心
- `CogVideoDecode`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `CogVideoTextEncode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `Fast Groups Muter (rgthree)`
- `SaveImage`
- `Reroute`
- `RIFE VFI`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `Joy_caption_load`
- `Joy_caption`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `RH_Captioner`
- `LoadImage`
- `DualCLIPLoader`
- `DownloadAndLoadCogVideoModel`
- `VideoCombine_Adv`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`easy cleanGpuUsed`、`FluxGuidance`、`ModelSamplingFlux`、`BasicGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`CLIPLoader`、`CogVideoTextEncode`、`CogVideoImageEncode`、`ImageResizeKJ`、`CogVideoSampler`、`CogVideoDecode`、`VAEDecode`、`EmptySD3LatentImage`、`CLIPTextEncode`、`VAELoader`、`SaveImage`、`RIFE VFI`、`VHS_VideoCombine`、`UNETLoader`、`Joy_caption_load`、`Joy_caption`、`LoraLoaderModelOnly`、`RH_Captioner`、`LoadImage`、`DualCLIPLoader`、`DownloadAndLoadCogVideoModel`、`VideoCombine_Adv`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance
