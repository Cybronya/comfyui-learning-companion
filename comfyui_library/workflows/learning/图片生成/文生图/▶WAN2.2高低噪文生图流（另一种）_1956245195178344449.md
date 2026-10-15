---
key: 图片生成/文生图/▶WAN2.2高低噪文生图流（另一种）_1956245195178344449.json
name: ▶WAN2.2高低噪文生图流（另一种）_1956245195178344449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/▶WAN2.2高低噪文生图流（另一种）_1956245195178344449.json
hash: 4b4778ebd6d18625
coverage: 0.8
learned_at: 2026-10-10 20:59:28
nodes: [VAELoader, PreviewImage, CLIPLoader, CLIPTextEncode, UNETLoader, UNETLoader, LayerUtility: PurgeVRAM, Note, EmptyHunyuanLatentVideo, CLIPTextEncode, KSampler, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, SaveImage, KSampler]
patterns: []
missing: [LayerUtility: PurgeVRAM]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 0, "steps": 6}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/▶WAN2.2高低噪文生图流（另一种）_1956245195178344449.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/▶WAN2.2高低噪文生图流（另一种）_1956245195178344449.json`

## 结构

**节点**（20 个）：
- `VAELoader`
- `PreviewImage`
- `CLIPLoader`
- `CLIPTextEncode`
- `UNETLoader`
- `UNETLoader`
- `LayerUtility: PurgeVRAM`
- `Note`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode`
- `KSampler`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `VAEDecode`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `VAEDecode`
- `SaveImage`
- `KSampler`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.30000000000000004`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `seed` = `0`
- `steps` = `6`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`VAELoader`、`PreviewImage`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`Note`、`EmptyHunyuanLatentVideo`、`KSampler`、`Fast Groups Bypasser (rgthree)`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAEDecode`

**缺卡**（1）：`LayerUtility: PurgeVRAM`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
