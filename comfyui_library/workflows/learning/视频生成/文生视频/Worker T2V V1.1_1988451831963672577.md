---
key: 视频生成/文生视频/Worker T2V V1.1_1988451831963672577.json
name: Worker T2V V1.1_1988451831963672577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Worker T2V V1.1_1988451831963672577.json
hash: 246699cbb71142c2
coverage: 0.971429
learned_at: 2026-10-15 22:47:17
nodes: [CR Text, RH_LLMAPI_NODE, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, JWInteger, JWInteger, easy showAnything, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, INTConstant, INTConstant, CLIPTextEncode, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, INTConstant, EmptyHunyuanLatentVideo, MathExpression|pysssss, CR Text, JWInteger, ImageFromBatch+, LayerUtility: PurgeVRAM V2, FlashVSRNode, RIFE VFI, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Worker T2V V1.1_1988451831963672577.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Worker T2V V1.1_1988451831963672577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `CR Text`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `EmptyHunyuanLatentVideo`
- `MathExpression|pysssss`
- `CR Text`
- `JWInteger`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM V2`
- `FlashVSRNode`
- `RIFE VFI`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`CR Text`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`JWInteger`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`INTConstant`、`KSamplerAdvanced`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`MathExpression|pysssss`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM V2`、`FlashVSRNode`、`RIFE VFI`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
