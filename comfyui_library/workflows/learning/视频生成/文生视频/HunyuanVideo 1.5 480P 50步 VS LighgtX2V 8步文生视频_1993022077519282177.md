---
key: 视频生成/文生视频/HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177.json
name: HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177.json
hash: 2f824663a8c35469
coverage: 0.8
learned_at: 2026-10-11 02:57:35
nodes: [DualCLIPLoader, VAELoader, EasyCache, Note, Note, MarkdownNote, KSamplerSelect, JWInteger, JWInteger, EmptyHunyuanVideo15Latent, LoraLoaderModelOnly, SamplerCustomAdvanced, UNETLoader, CFGGuider, ModelSamplingSD3, BasicScheduler, RandomNoise, DualCLIPLoader, VAELoader, EasyCache, CLIPTextEncode, Note, Note, MarkdownNote, KSamplerSelect, JWInteger, JWInteger, EmptyHunyuanVideo15Latent, SamplerCustomAdvanced, UNETLoader, RandomNoise, LoraLoaderModelOnly, ModelSamplingSD3, CreateVideo, VAEDecodeTiled, VAEDecode, VAEDecodeTiled, VAEDecode, ImageConcanate, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, AILab_QwenVL, easy showAnything, VHS_VideoCombine, CFGGuider, BasicScheduler, VHS_VideoCombine, VHS_VideoCombine, AddLabel, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, AddLabel, CR Prompt Text, Seed (rgthree)]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CR Prompt Text, Seed (rgthree)]
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `DualCLIPLoader`
- `VAELoader`
- `EasyCache`
- `Note`
- `Note`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `JWInteger`
- `JWInteger`
- `EmptyHunyuanVideo15Latent`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `BasicScheduler`
- `RandomNoise`
- `DualCLIPLoader`
- `VAELoader`
- `EasyCache`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `JWInteger`
- `JWInteger`
- `EmptyHunyuanVideo15Latent`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AILab_QwenVL`
- `easy showAnything`
- `VHS_VideoCombine`
- `CFGGuider`
- `BasicScheduler`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `CR Prompt Text`
- `Seed (rgthree)`

## 知识

覆盖率 **80%**（44/55）

**有卡**：`DualCLIPLoader`、`VAELoader`、`EasyCache`、`KSamplerSelect`、`JWInteger`、`EmptyHunyuanVideo15Latent`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`UNETLoader`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`RandomNoise`、`CLIPTextEncode`、`CreateVideo`、`VAEDecodeTiled`、`VAEDecode`、`ImageConcanate`、`AILab_QwenVL`、`VHS_VideoCombine`、`AddLabel`

**缺卡**（4）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
