---
key: 提示词反推_joy caption3_joy caption-beta-one_1940313410569682946.json
name: 提示词反推_joy caption3_joy caption-beta-one_1940313410569682946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/提示词反推_joy caption3_joy caption-beta-one_1940313410569682946.json
hash: 8d9445ba7279ab9a
coverage: 0.733333
learned_at: 2026-10-10 20:59:45
nodes: [LoadImage, LayerUtility: JoyCaptionBeta1, ShowText|pysssss, LayerUtility: LoadJoyCaptionBeta1Model, UNETLoader, EmptyLatentImage, DualCLIPLoader, KSampler, CLIPTextEncode, FluxGuidance, CLIPTextEncode, VAELoader, VAEDecode, SaveImage, Fast Groups Muter (rgthree)]
patterns: [text_to_image]
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model]
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 216727540294355, "steps": 20, "width": 512}
discoveries: [次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识]
---

# 提示词反推_joy caption3_joy caption-beta-one_1940313410569682946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/提示词反推_joy caption3_joy caption-beta-one_1940313410569682946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `LoadImage`
- `LayerUtility: JoyCaptionBeta1`
- `ShowText|pysssss`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `DualCLIPLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Muter (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `216727540294355`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`LoadImage`、`UNETLoader`、`EmptyLatentImage`、`DualCLIPLoader`、`KSampler`、`CLIPTextEncode`、`FluxGuidance`、`VAELoader`、`VAEDecode`、`SaveImage`

**缺卡**（2）：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance

## 学习发现

- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
