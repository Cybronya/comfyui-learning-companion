---
key: 平台全量/QwenEdit2511MultiangleLightning交互式灯光调节(感谢AIWood大佬)_2011339156768690177.json
name: QwenEdit2511MultiangleLightning交互式灯光调节(感谢AIWood大佬)_2011339156768690177
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/QwenEdit2511MultiangleLightning交互式灯光调节(感谢AIWood大佬)_2011339156768690177.json
hash: 9282c06951f46e8e
coverage: 0.555556
learned_at: 2026-11-14 00:53:08
nodes: [TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Note, EmptySD3LatentImage, TextEncodeQwenImageEditPlus, VAELoader, KSampler, ModelSamplingAuraFlow, CFGNorm, VAEDecode, PrimitiveInt, PrimitiveInt, CLIPLoader, PrimitiveInt, PrimitiveFloat, NumberClamp, NumberClamp, PrimitiveInt, NumberClamp, PrimitiveInt, PrimitiveInt, NumberClamp, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, NumberClamp, NumberClamp, PrimitiveFloat, PrimitiveInt, Light-Tool: RGB2Hex, SimpleMathSlider+, LoadImage, QwenMultiangleLightningNode, UNETLoader, VAEEncode, ImageScaleToTotalPixels, SaveImage, easy showAnything, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveInt]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1002, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/QwenEdit2511MultiangleLightning交互式灯光调节(感谢AIWood大佬)_2011339156768690177.json

> 来源文件 `comfyui_library/workflows/平台全量/QwenEdit2511MultiangleLightning交互式灯光调节(感谢AIWood大佬)_2011339156768690177.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Note`
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPLoader`
- `PrimitiveInt`
- `PrimitiveFloat`
- `NumberClamp`
- `NumberClamp`
- `PrimitiveInt`
- `NumberClamp`
- `PrimitiveInt`
- `PrimitiveInt`
- `NumberClamp`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `NumberClamp`
- `NumberClamp`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Light-Tool: RGB2Hex`
- `SimpleMathSlider+`
- `LoadImage`
- `QwenMultiangleLightningNode`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `SaveImage`
- `easy showAnything`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1002`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **56%**（25/45）

**有卡**：`TextEncodeQwenImageEditPlus`、`FluxKontextMultiReferenceLatentMethod`、`EmptySD3LatentImage`、`VAELoader`、`KSampler`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`CLIPLoader`、`NumberClamp`、`Light-Tool: RGB2Hex`、`SimpleMathSlider+`、`LoadImage`、`QwenMultiangleLightningNode`、`UNETLoader`、`VAEEncode`、`ImageScaleToTotalPixels`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、LoadImage、CFGNorm、FluxKontextMultiReferenceLatentMethod

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
