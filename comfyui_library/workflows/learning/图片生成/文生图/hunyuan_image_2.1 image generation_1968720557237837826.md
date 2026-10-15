---
key: 图片生成/文生图/hunyuan_image_2.1 image generation_1968720557237837826.json
name: hunyuan_image_2.1 image generation_1968720557237837826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/hunyuan_image_2.1 image generation_1968720557237837826.json
hash: c4e11a0e569fd4f1
coverage: 0.580645
learned_at: 2026-10-10 20:59:21
nodes: [VAELoader, DualCLIPLoader, CLIPTextEncode, Note, UNETLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, HunyuanRefinerLatent, SaveImage, UNETLoader, KSampler, LayerUtility: PurgeVRAM V2, VAEDecode, CLIPTextEncode, EmptyHunyuanImageLatent, KSampler, LayerUtility: PurgeVRAM V2, VAEDecode, SaveImage, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree)]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 770039891896361, "steps": 4}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/hunyuan_image_2.1 image generation_1968720557237837826.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/hunyuan_image_2.1 image generation_1968720557237837826.json`

## 结构

**节点**（31 个）：
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode`
- `Note`
- `UNETLoader`
- `VAELoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEEncode`
- `HunyuanRefinerLatent`
- `SaveImage`
- `UNETLoader`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode`
- `CLIPTextEncode`
- `EmptyHunyuanImageLatent`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode`
- `SaveImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `770039891896361`
- `steps` = `4`

## 知识

覆盖率 **58%**（18/31）

**有卡**：`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`Note`、`UNETLoader`、`VAEEncode`、`HunyuanRefinerLatent`、`SaveImage`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`EmptyHunyuanImageLatent`

**缺卡**（12）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
