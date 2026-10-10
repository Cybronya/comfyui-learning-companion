---
key: 图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2056630627348336641.json
name: ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2056630627348336641
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2056630627348336641.json
hash: 4b9cde85f70e5e4b
coverage: 0.515152
learned_at: 2026-10-10 20:48:11
nodes: [SetNode, SetNode, SetNode, easy promptLine, GetNode, GetNode, ModelSamplingAuraFlow, CFGNorm, PlaySound|pysssss, PlaySound|pysssss, INTConstant, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, GetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, JjkText, SaveImage, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, UNETLoader, KSampler, VAEDecode, LayerUtility: PurgeVRAM, SetNode, PlaySound|pysssss, JjkText, LoadImage]
patterns: [image_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, easy promptLine]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 195576003938438, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2056630627348336641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2056630627348336641.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `easy promptLine`
- `GetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `INTConstant`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `JjkText`
- `SaveImage`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `PlaySound|pysssss`
- `JjkText`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `195576003938438`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（17/33）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`INTConstant`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`SaveImage`、`FluxKontextMultiReferenceLatentMethod`、`UNETLoader`、`KSampler`、`VAEDecode`、`LoadImage`

**缺卡**（6）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`PlaySound|pysssss`、`PlaySound|pysssss`、`PlaySound|pysssss`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
