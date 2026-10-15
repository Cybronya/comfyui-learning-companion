---
key: 视频生成/文生视频/HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177.json
name: HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177.json
hash: 2f824663a8c35469
coverage: 0.872727
learned_at: 2026-10-15 22:44:27
nodes: [DualCLIPLoader, VAELoader, EasyCache, Note, Note, MarkdownNote, KSamplerSelect, JWInteger, JWInteger, EmptyHunyuanVideo15Latent, LoraLoaderModelOnly, SamplerCustomAdvanced, UNETLoader, CFGGuider, ModelSamplingSD3, BasicScheduler, RandomNoise, DualCLIPLoader, VAELoader, EasyCache, CLIPTextEncode, Note, Note, MarkdownNote, KSamplerSelect, JWInteger, JWInteger, EmptyHunyuanVideo15Latent, SamplerCustomAdvanced, UNETLoader, RandomNoise, LoraLoaderModelOnly, ModelSamplingSD3, CreateVideo, VAEDecodeTiled, VAEDecode, VAEDecodeTiled, VAEDecode, ImageConcanate, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, AILab_QwenVL, easy showAnything, VHS_VideoCombine, CFGGuider, BasicScheduler, VHS_VideoCombine, VHS_VideoCombine, AddLabel, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, AddLabel, CR Prompt Text, Seed (rgthree)]
patterns: []
missing: []
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

覆盖率 **87%**（48/55）

**有卡**：`DualCLIPLoader`、`VAELoader`、`EasyCache`、`KSamplerSelect`、`JWInteger`、`EmptyHunyuanVideo15Latent`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`UNETLoader`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`RandomNoise`、`CLIPTextEncode`、`CreateVideo`、`VAEDecodeTiled`、`VAEDecode`、`ImageConcanate`、`AILab_QwenVL`、`VHS_VideoCombine`、`AddLabel`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
