---
key: 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2104081684923772930.json
name: （稳定加速版）Qwen Image 2.1 PE 文生图_2104081684923772930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2104081684923772930.json
hash: d9f78412cc52d6c2
coverage: 0.785714
learned_at: 2026-10-07 02:03:36
nodes: [Note, CLIPLoader, VAELoader, QwenImage21Cache, Note, CR Prompt Text, easy showAnything, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, QwenPERewriteT8, easy cleanGpuUsed, SaveImage, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, UNETLoader, QwenImage21SpectrumT8, KSampler, KSamplerSelect, ManualSigmas, VHS_VideoCombine, LTXVConcatAVLatent, VAEDecode, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEEncode, VAEDecode]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 708219274555562, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2104081684923772930.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2104081684923772930.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `Note`
- `CR Prompt Text`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `QwenPERewriteT8`
- `easy cleanGpuUsed`
- `SaveImage`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `KSampler` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEEncode` ★核心
- `VAEDecode` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `708219274555562`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`QwenPERewriteT8`、`SaveImage`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`UNETLoader`、`QwenImage21SpectrumT8`、`KSampler`、`KSamplerSelect`、`ManualSigmas`、`VHS_VideoCombine`、`LTXVConcatAVLatent`、`VAEDecode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEEncode`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
