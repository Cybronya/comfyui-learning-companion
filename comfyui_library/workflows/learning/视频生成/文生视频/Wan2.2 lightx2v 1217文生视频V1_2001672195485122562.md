---
key: 视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json
name: Wan2.2 lightx2v 1217文生视频V1_2001672195485122562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json
hash: 7a44531dfc3218d2
coverage: 0.848485
learned_at: 2026-10-11 02:57:38
nodes: [TT_img_enc, SaveImage, VAEDecode, CLIPTextEncode, LayerUtility: PurgeVRAM, VAELoader, KSamplerAdvanced, KSamplerAdvanced, INTConstant, JWInteger, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, INTConstant, VHS_VideoCombine, ImageFromBatch+, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, easy seed, VHS_VideoCombine, CLIPLoader, UNETLoader, JWInteger, JWInteger, CR Prompt Text, UNETLoader, LoraLoaderModelOnly, easy showAnything]
patterns: []
missing: [ImageFromBatch+, LayerUtility: PurgeVRAM, CR Prompt Text, easy seed]
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `TT_img_enc`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `JWInteger`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `easy seed`
- `VHS_VideoCombine`
- `CLIPLoader`
- `UNETLoader` ★核心
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`TT_img_enc`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`KSamplerAdvanced`、`INTConstant`、`JWInteger`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`CLIPLoader`、`UNETLoader`

**缺卡**（4）：`ImageFromBatch+`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
