---
key: 图片生成/图生图/纯种WAN2.2洗图(秒杀Krea)_1938145100054577154.json
name: 纯种WAN2.2洗图(秒杀Krea)_1938145100054577154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/纯种WAN2.2洗图(秒杀Krea)_1938145100054577154.json
hash: b8e2c9c47d30873c
coverage: 0.913043
learned_at: 2026-10-23 13:21:13
nodes: [UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, VAELoader, RandomNoise, SplitSigmas, SamplerCustomAdvanced, DisableNoise, Image Comparer (rgthree), RH_Captioner, CLIPLoader, VAEDecode, SaveImage, LoadImage, SamplerCustomAdvanced, WanVideoNAG, KSamplerSelect, VAEEncode, CLIPTextEncode, PrimitiveFloat, BasicScheduler, CFGGuider, ModelSamplingSD3]
patterns: []
missing: []
---

# 图片生成/图生图/纯种WAN2.2洗图(秒杀Krea)_1938145100054577154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/纯种WAN2.2洗图(秒杀Krea)_1938145100054577154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `RandomNoise`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `Image Comparer (rgthree)`
- `RH_Captioner`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `WanVideoNAG`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `BasicScheduler`
- `CFGGuider`
- `ModelSamplingSD3`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAELoader`、`RandomNoise`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`RH_Captioner`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`WanVideoNAG`、`KSamplerSelect`、`VAEEncode`、`BasicScheduler`、`CFGGuider`、`ModelSamplingSD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider
