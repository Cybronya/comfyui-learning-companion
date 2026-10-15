---
key: 图片生成/文生图/Wan2.1 文生图_1950055564211568642.json
name: Wan2.1 文生图_1950055564211568642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1 文生图_1950055564211568642.json
hash: e7fa7219df2c3cee
coverage: 0.8
learned_at: 2026-10-10 20:59:13
nodes: [LoraLoaderModelOnly, VAELoader, EmptyHunyuanLatentVideo, KSampler, CLIPTextEncode, LoraLoaderModelOnly, LayerUtility: JoyCaptionBeta1, LoadImage, LayerUtility: LoadJoyCaptionBeta1Model, ShowText|pysssss, CLIPTextEncode, UNETLoader, CLIPLoader, VAEDecode, SaveImage]
patterns: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 636156977862286, "steps": 8}
discoveries: [次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.1 文生图_1950055564211568642.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.1 文生图_1950055564211568642.json`

## 结构

**节点**（15 个）：
- `LoraLoaderModelOnly`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `LayerUtility: JoyCaptionBeta1`
- `LoadImage`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `ShowText|pysssss`
- `CLIPTextEncode`
- `UNETLoader`
- `CLIPLoader`
- `VAEDecode`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `seed` = `636156977862286`
- `steps` = `8`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`LoraLoaderModelOnly`、`VAELoader`、`EmptyHunyuanLatentVideo`、`KSampler`、`CLIPTextEncode`、`LayerUtility: JoyCaptionBeta1`、`LoadImage`、`LayerUtility: LoadJoyCaptionBeta1Model`、`ShowText|pysssss`、`UNETLoader`

**缺卡**（2）：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
