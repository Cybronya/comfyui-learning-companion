---
key: 图片生成/文生图/Wan2.2反推文生图_1973082031938736129.json
name: Wan2.2反推文生图_1973082031938736129.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2反推文生图_1973082031938736129.json
hash: aba5a1d41eabd1c7
coverage: 0.821429
learned_at: 2026-10-09 19:50:52
nodes: [RandomNoise, SplitSigmas, DisableNoise, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, WanVideoNAG, CFGGuider, SamplerCustomAdvanced, UNETLoader, VAELoader, ShowText|pysssss, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, CLIPLoader, Image Comparer (rgthree), easy cleanGpuUsed, easy cleanGpuUsed, SeedVR2, PreviewImage, SaveImage, VAEDecode, LoraLoaderModelOnly, BasicScheduler, LoadImage, RH_Captioner]
patterns: []
missing: [easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "height": 1152, "width": 768}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2反推文生图_1973082031938736129.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1973082031938736129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `RandomNoise`
- `SplitSigmas`
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `WanVideoNAG`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SeedVR2`
- `PreviewImage`
- `SaveImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `LoadImage`
- `RH_Captioner`

## 关键参数

- `width` = `768`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`RandomNoise`、`SplitSigmas`、`DisableNoise`、`SamplerCustomAdvanced`、`ModelSamplingSD3`、`KSamplerSelect`、`WanVideoNAG`、`CFGGuider`、`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CLIPLoader`、`SeedVR2`、`SaveImage`、`VAEDecode`、`BasicScheduler`、`LoadImage`、`RH_Captioner`

**缺卡**（2）：`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
