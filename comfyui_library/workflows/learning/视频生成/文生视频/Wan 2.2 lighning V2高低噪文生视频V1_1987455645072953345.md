---
key: 视频生成/文生视频/Wan 2.2 lighning V2高低噪文生视频V1_1987455645072953345.json
name: Wan 2.2 lighning V2高低噪文生视频V1_1987455645072953345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2 lighning V2高低噪文生视频V1_1987455645072953345.json
hash: 0871bd37ed5dae65
coverage: 0.888889
learned_at: 2026-10-11 02:57:38
nodes: [PathchSageAttentionKJ, CLIPTextEncode, PathchSageAttentionKJ, TorchCompileModel, TorchCompileModel, ModelSamplingSD3, EmptyHunyuanLatentVideo, easy cleanGpuUsed, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, ImageSharpen, DownloadAndLoadGIMMVFIModel, ImageFromBatch+, LayerUtility: PurgeVRAM, CLIPTextEncode, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, GIMMVFI_interpolate, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, Text Multiline, VHS_VideoCombine, CLIPLoader, UNETLoader, INTConstant, LoraLoaderModelOnly, JWInteger, JWInteger]
patterns: []
missing: [ImageFromBatch+, LayerUtility: PurgeVRAM, Text Multiline, easy cleanGpuUsed]
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan 2.2 lighning V2高低噪文生视频V1_1987455645072953345.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2 lighning V2高低噪文生视频V1_1987455645072953345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `TorchCompileModel`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `ImageSharpen`
- `DownloadAndLoadGIMMVFIModel`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GIMMVFI_interpolate`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `Text Multiline`
- `VHS_VideoCombine`
- `CLIPLoader`
- `UNETLoader` ★核心
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`TorchCompileModel`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`VAEDecode`、`UNETLoader`、`INTConstant`、`ImageSharpen`、`DownloadAndLoadGIMMVFIModel`、`KSamplerAdvanced`、`GIMMVFI_interpolate`、`VAELoader`、`JWInteger`、`VHS_VideoCombine`、`CLIPLoader`

**缺卡**（4）：`ImageFromBatch+`、`LayerUtility: PurgeVRAM`、`Text Multiline`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
