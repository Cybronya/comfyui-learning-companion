---
key: 视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json
name: 加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json
hash: acc3cdee7b1666cb
coverage: 0.833333
learned_at: 2026-10-11 02:45:04
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, LoraLoaderModelOnly, CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, Text Multiline, VHS_VideoCombine, SimpleMath+, PrimitiveInt, INTConstant, EmptyHunyuanLatentVideo, LayerUtility: PurgeVRAM V2, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, CLIPTextEncode]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, SimpleMath+, Text Multiline]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
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

覆盖率 **83%**（20/24）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerAdvanced`、`VHS_VideoCombine`、`INTConstant`、`EmptyHunyuanLatentVideo`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`

**缺卡**（3）：`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
