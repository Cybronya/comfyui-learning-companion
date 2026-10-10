---
key: F.1 在线生图-反推_1873979338214559746.json
name: F.1 在线生图-反推_1873979338214559746
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 在线生图-反推_1873979338214559746.json
hash: cab59736617e0d3d
coverage: 0.8
learned_at: 2026-10-10 20:58:30
nodes: [SaveImage, SaveImage, SaveImage, EmptyLatentImage, Anything Everywhere3, UNETLoader, LoraLoaderModelOnly, SaveImage, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, ShowText|pysssss, LoadImage, CLIPTextEncode, KSampler, ConditioningZeroOut, VAEDecode, KSampler, ConditioningZeroOut, KSampler, ConditioningZeroOut, KSampler, ConditioningZeroOut, VAEDecode, VAEDecode, VAEDecode, FluxGuidance, VAELoader, Anything Everywhere3, DualCLIPLoader]
patterns: [text_to_image]
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 1079658624448393, "steps": 20, "width": 1024}
discoveries: [次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识]
---

# F.1 在线生图-反推_1873979338214559746.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1 在线生图-反推_1873979338214559746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `ShowText|pysssss`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `VAELoader`
- `Anything Everywhere3`
- `DualCLIPLoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `1079658624448393`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（24/30）

**有卡**：`SaveImage`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`CLIPTextEncode`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`FluxGuidance`、`VAELoader`、`DualCLIPLoader`

**缺卡**（3）：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage

## 学习发现

- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
