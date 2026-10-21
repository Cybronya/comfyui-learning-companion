---
key: 图片生成/文生图/图片生成_Z-Image-Turbo_Detail-Daemon_增加细节_去除竖纹_2013923317299810306.json
name: 图片生成_Z-Image-Turbo_Detail-Daemon_增加细节_去除竖纹_2013923317299810306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图片生成_Z-Image-Turbo_Detail-Daemon_增加细节_去除竖纹_2013923317299810306.json
hash: e362fd17aea40ed3
coverage: 0.75
learned_at: 2026-10-19 22:15:55
nodes: [SetNode, SetNode, GetNode, easy int, easy int, GetNode, CLIPTextEncode, ConditioningZeroOut, SamplerCustomAdvanced, CFGGuider, BasicScheduler, EmptyLatentImage, KSamplerSelect, SamplerCustomAdvanced, Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, GetNode, VRAMReserver, SetNode, SeedVR2LoadVAEModel, CLIPLoader, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, VAEDecode, VAEDecode, Reroute, AILab_ImagePreview, SaveImage, UNETLoader, LoraLoaderModelOnly, VAELoader, DetailDaemonSamplerNode, DetailDaemonGraphSigmasNode, Seed (rgthree), RandomNoise]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 图片生成/文生图/图片生成_Z-Image-Turbo_Detail-Daemon_增加细节_去除竖纹_2013923317299810306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图片生成_Z-Image-Turbo_Detail-Daemon_增加细节_去除竖纹_2013923317299810306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `easy int`
- `easy int`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `BasicScheduler`
- `EmptyLatentImage` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `GetNode`
- `VRAMReserver`
- `SetNode`
- `SeedVR2LoadVAEModel`
- `CLIPLoader`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `AILab_ImagePreview`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `DetailDaemonSamplerNode` ★核心
- `DetailDaemonGraphSigmasNode`
- `Seed (rgthree)`
- `RandomNoise`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`easy int`、`CLIPTextEncode`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`CFGGuider`、`BasicScheduler`、`EmptyLatentImage`、`KSamplerSelect`、`SaveImage`、`VRAMReserver`、`SeedVR2LoadVAEModel`、`CLIPLoader`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`VAEDecode`、`AILab_ImagePreview`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`DetailDaemonSamplerNode`、`DetailDaemonGraphSigmasNode`、`Seed (rgthree)`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
