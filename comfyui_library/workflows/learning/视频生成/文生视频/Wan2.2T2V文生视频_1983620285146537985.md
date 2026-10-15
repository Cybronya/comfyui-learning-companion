---
key: 视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json
name: Wan2.2T2V文生视频_1983620285146537985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json
hash: b952d3c607628c02
coverage: 0.962963
learned_at: 2026-10-15 22:47:13
nodes: [PrimitiveInt, INTConstant, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, DownloadAndLoadGIMMVFIModel, VAEDecode, VAELoader, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, CLIPTextEncode, CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, SimpleMath+, CLIPTextEncode, CLIPTextEncode, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（27 个）：
- `PrimitiveInt`
- `INTConstant`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `DownloadAndLoadGIMMVFIModel`
- `VAEDecode` ★核心
- `VAELoader`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`INTConstant`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`ModelSamplingSD3`、`DownloadAndLoadGIMMVFIModel`、`VAEDecode`、`VAELoader`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`CLIPLoader`、`KSamplerAdvanced`、`VHS_VideoCombine`、`SimpleMath+`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
