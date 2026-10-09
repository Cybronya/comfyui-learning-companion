---
key: 图片生成/文生图/【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961.json
name: 【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961.json
hash: 4f7670e869eafad8
coverage: 0.541667
learned_at: 2026-10-07 23:46:53
nodes: [KSampler, CLIPLoader, VAELoader, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, ShowText|pysssss, SaveImage, UNETLoader, LoadImage, ModelSamplingAuraFlow, VAEDecode, easy showAnything, LoraLoaderModelOnly, PreviewImage, CLIPTextEncode, CR SDXL Aspect Ratio, Text Concatenate, CLIPTextEncode, PrimitiveString, Reroute, GetImageSize, Note, PrimitiveString, LoadImage]
patterns: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, Text Concatenate, CR SDXL Aspect Ratio]
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 269396040660126, "steps": 30}
discoveries: [次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1961717444916264961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `ShowText|pysssss`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `PrimitiveString`
- `Reroute`
- `GetImageSize`
- `Note`
- `PrimitiveString`
- `LoadImage`

## 关键参数

- `seed` = `269396040660126`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（13/24）

**有卡**：`KSampler`、`CLIPLoader`、`VAELoader`、`SaveImage`、`UNETLoader`、`LoadImage`、`ModelSamplingAuraFlow`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`GetImageSize`

**缺卡**（4）：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`Text Concatenate`、`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 学习发现

- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
