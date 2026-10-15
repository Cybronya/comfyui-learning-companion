---
key: 视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json
name: Wan2.2建筑生长文生视频_1989132418231701506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json
hash: 8c4701a8cbb43974
coverage: 0.958333
learned_at: 2026-10-15 22:47:15
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, SimpleMath+, PrimitiveInt, LayerUtility: PurgeVRAM V2, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, CLIPTextEncode, Text Multiline, INTConstant, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（24 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `SimpleMath+`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM V2`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `INTConstant`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerAdvanced`、`VHS_VideoCombine`、`SimpleMath+`、`LayerUtility: PurgeVRAM V2`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`Text Multiline`、`INTConstant`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
