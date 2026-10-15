---
key: 视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json
name: 加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json
hash: acc3cdee7b1666cb
coverage: 0.958333
learned_at: 2026-10-15 22:48:06
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, LoraLoaderModelOnly, CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, Text Multiline, VHS_VideoCombine, SimpleMath+, PrimitiveInt, INTConstant, EmptyHunyuanLatentVideo, LayerUtility: PurgeVRAM V2, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（24 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `VHS_VideoCombine`
- `SimpleMath+`
- `PrimitiveInt`
- `INTConstant`
- `EmptyHunyuanLatentVideo`
- `LayerUtility: PurgeVRAM V2`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerAdvanced`、`Text Multiline`、`VHS_VideoCombine`、`SimpleMath+`、`INTConstant`、`EmptyHunyuanLatentVideo`、`LayerUtility: PurgeVRAM V2`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
