---
key: 视频生成/文生视频/wan2.2官方优化版250928（添加最新4步加速lora）_1973561137847472129.json
name: wan2.2官方优化版250928（添加最新4步加速lora）_1973561137847472129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2官方优化版250928（添加最新4步加速lora）_1973561137847472129.json
hash: 8e23d525e1ca6025
coverage: 0.8
learned_at: 2026-10-10 23:09:47
nodes: [UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, VAELoader, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, GIMMVFI_interpolate, ImageSharpen, easy cleanGpuUsed, TorchCompileModel, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, CLIPLoader, TorchCompileModel, PathchSageAttentionKJ, Note, INTConstant, INTConstant, JWInteger, Text Multiline, JWInteger, JWInteger, ImageFromBatch+, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, Note, Note, LoraLoaderModelOnly, VHS_VideoCombine, Note, Note]
patterns: []
missing: [ImageFromBatch+, Text Multiline, easy cleanGpuUsed]
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2官方优化版250928（添加最新4步加速lora）_1973561137847472129.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2官方优化版250928（添加最新4步加速lora）_1973561137847472129.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `ImageSharpen`
- `easy cleanGpuUsed`
- `TorchCompileModel`
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `Note`
- `INTConstant`
- `INTConstant`
- `JWInteger`
- `Text Multiline`
- `JWInteger`
- `JWInteger`
- `ImageFromBatch+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `Note`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`DownloadAndLoadGIMMVFIModel`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`ImageSharpen`、`TorchCompileModel`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`INTConstant`、`JWInteger`、`KSamplerAdvanced`

**缺卡**（3）：`ImageFromBatch+`、`Text Multiline`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
