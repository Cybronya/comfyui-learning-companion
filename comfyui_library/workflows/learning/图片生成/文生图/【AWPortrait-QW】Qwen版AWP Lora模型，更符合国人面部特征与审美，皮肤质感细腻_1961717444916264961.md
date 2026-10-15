---
key: 图片生成/文生图/【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961.json
name: 【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961.json
hash: 4f7670e869eafad8
coverage: 0.708333
learned_at: 2026-10-15 22:28:02
nodes: [KSampler, CLIPLoader, VAELoader, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, ShowText|pysssss, SaveImage, UNETLoader, LoadImage, ModelSamplingAuraFlow, VAEDecode, easy showAnything, LoraLoaderModelOnly, PreviewImage, CLIPTextEncode, CR SDXL Aspect Ratio, Text Concatenate, CLIPTextEncode, PrimitiveString, Reroute, GetImageSize, Note, PrimitiveString, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 269396040660126, "steps": 30}
---

# 图片生成/文生图/【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【AWPortrait-QW】Qwen版AWP Lora模型，更符合国人面部特征与审美，皮肤质感细腻_1961717444916264961.json`

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

覆盖率 **71%**（17/24）

**有卡**：`KSampler`、`CLIPLoader`、`VAELoader`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`SaveImage`、`UNETLoader`、`LoadImage`、`ModelSamplingAuraFlow`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`、`Text Concatenate`、`GetImageSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
