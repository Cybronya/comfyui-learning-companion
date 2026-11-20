---
key: 平台全量/Flux Face Swap + Huge Animal!_1881255330872008706.json
name: Flux Face Swap + Huge Animal!_1881255330872008706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Face Swap + Huge Animal!_1881255330872008706.json
hash: 108b0becaed55b13
coverage: 0.8
learned_at: 2026-11-14 00:27:35
nodes: [VAEDecode, UNETLoader, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, PreviewImage, CLIPTextEncode, ReActorFaceSwap, LoadImage, CLIPTextEncode, DF_Text, Text Find and Replace, SaveImage, CLIPTextEncode, Note, Note, Note, DualCLIPLoader, SamplerCustomAdvanced, easy cleanGpuUsed, VAELoader, EmptyLatentImage, DF_Text, ShowText|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 768}
---

# 平台全量/Flux Face Swap + Huge Animal!_1881255330872008706.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Face Swap + Huge Animal!_1881255330872008706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ReActorFaceSwap`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `DF_Text`
- `Text Find and Replace`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `DualCLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `DF_Text`
- `ShowText|pysssss`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`VAEDecode`、`UNETLoader`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`CLIPTextEncode`、`ReActorFaceSwap`、`LoadImage`、`DF_Text`、`Text Find and Replace`、`SaveImage`、`DualCLIPLoader`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`VAELoader`、`EmptyLatentImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
