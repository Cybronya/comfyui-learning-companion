---
key: 图片生成/文生图/AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738.json
name: AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738.json
hash: 9a2597262197d7e5
coverage: 0.868421
learned_at: 2026-10-15 22:26:11
nodes: [UNETLoader, UNETLoader, CLIPLoader, SeedVR2BlockSwap, VAELoader, PresetTextSelector, PathchSageAttentionKJ, CLIPTextEncode, CFGZeroStar, LoraLoaderModelOnly, PathchSageAttentionKJ, CFGZeroStar, EmptyHunyuanLatentVideo, PrimitiveNode, CLIPTextEncode, Int, Int, ModelSamplingSD3, ModelSamplingSD3, CFGNorm, CFGNorm, LoraLoaderModelOnly, Image Comparer (rgthree), SeedVR2GGUF, KSampler, KSampler, ShowText|pysssss, CR Text, SaveImage, VAEDecode, LayerUtility: PurgeVRAM V2, PreviewImage, PreviewImage, easy promptConcat, easy anythingIndexSwitch, RHHiddenNodes, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "heun", "scheduler": "beta", "seed": 136838535921461, "steps": 10}
---

# 图片生成/文生图/AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（38 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `SeedVR2BlockSwap`
- `VAELoader`
- `PresetTextSelector`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CFGZeroStar`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `EmptyHunyuanLatentVideo`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CFGNorm`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2GGUF`
- `KSampler` ★核心
- `KSampler` ★核心
- `ShowText|pysssss`
- `CR Text`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `PreviewImage`
- `easy promptConcat`
- `easy anythingIndexSwitch`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `136838535921461`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`UNETLoader`、`CLIPLoader`、`SeedVR2BlockSwap`、`VAELoader`、`PresetTextSelector`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`CFGZeroStar`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`Int`、`ModelSamplingSD3`、`CFGNorm`、`SeedVR2GGUF`、`KSampler`、`CR Text`、`SaveImage`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`easy promptConcat`、`easy anythingIndexSwitch`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGNorm
