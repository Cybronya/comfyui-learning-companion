---
key: 图片生成/文生图/AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738.json
name: AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738.json
hash: 9a2597262197d7e5
coverage: 0.763158
learned_at: 2026-10-10 21:26:03
nodes: [UNETLoader, UNETLoader, CLIPLoader, SeedVR2BlockSwap, VAELoader, PresetTextSelector, PathchSageAttentionKJ, CLIPTextEncode, CFGZeroStar, LoraLoaderModelOnly, PathchSageAttentionKJ, CFGZeroStar, EmptyHunyuanLatentVideo, PrimitiveNode, CLIPTextEncode, Int, Int, ModelSamplingSD3, ModelSamplingSD3, CFGNorm, CFGNorm, LoraLoaderModelOnly, Image Comparer (rgthree), SeedVR2GGUF, KSampler, KSampler, ShowText|pysssss, CR Text, SaveImage, VAEDecode, LayerUtility: PurgeVRAM V2, PreviewImage, PreviewImage, easy promptConcat, easy anythingIndexSwitch, RHHiddenNodes, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [CR Text, LayerUtility: PurgeVRAM V2, easy anythingIndexSwitch, easy promptConcat]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "heun", "scheduler": "beta", "seed": 136838535921461, "steps": 10}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI短剧定妆照万相2.2文生图+自动扩词+多风格参考_1957310097770868738.json`

## 结构

**节点**（38 个）：
- `UNETLoader`
- `UNETLoader`
- `CLIPLoader`
- `SeedVR2BlockSwap`
- `VAELoader`
- `PresetTextSelector`
- `PathchSageAttentionKJ`
- `CLIPTextEncode`
- `CFGZeroStar`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `EmptyHunyuanLatentVideo`
- `PrimitiveNode`
- `CLIPTextEncode`
- `Int`
- `Int`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CFGNorm`
- `CFGNorm`
- `LoraLoaderModelOnly`
- `Image Comparer (rgthree)`
- `SeedVR2GGUF`
- `KSampler`
- `KSampler`
- `ShowText|pysssss`
- `CR Text`
- `SaveImage`
- `VAEDecode`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `PreviewImage`
- `easy promptConcat`
- `easy anythingIndexSwitch`
- `RHHiddenNodes`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `seed` = `136838535921461`
- `steps` = `10`

## 知识

覆盖率 **76%**（29/38）

**有卡**：`UNETLoader`、`CLIPLoader`、`SeedVR2BlockSwap`、`VAELoader`、`PresetTextSelector`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`CFGZeroStar`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`PrimitiveNode`、`Int`、`ModelSamplingSD3`、`CFGNorm`、`Image Comparer (rgthree)`、`SeedVR2GGUF`、`KSampler`、`ShowText|pysssss`、`CR Text`、`SaveImage`

**缺卡**（4）：`CR Text`、`LayerUtility: PurgeVRAM V2`、`easy anythingIndexSwitch`、`easy promptConcat`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
