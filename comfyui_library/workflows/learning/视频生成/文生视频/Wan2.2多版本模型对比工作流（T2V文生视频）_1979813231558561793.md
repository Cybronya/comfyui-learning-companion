---
key: 视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json
name: Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json
hash: 89b2cee755353852
coverage: 0.957143
learned_at: 2026-10-15 22:47:15
nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, EmptyHunyuanLatentVideo, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Text Concatenate, CLIPLoader, VAELoader, PrimitiveInt, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Note, LoraLoaderModelOnly, SimpleMath+, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, Note, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, LoraLoaderModelOnly, UNETLoader, UNETLoader, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（70 个）：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Note`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `INTConstant`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（67/70）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`Text Concatenate`、`CLIPLoader`、`VAELoader`、`Text Multiline`、`SimpleMath+`、`UNETLoader`、`INTConstant`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
