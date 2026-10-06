---
key: 图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json
name: QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json
hash: 6c44be4e173d328b
coverage: 0.833333
learned_at: 2026-10-07 02:28:10
nodes: [KSampler, QwenImage21Cache, EmptyLatentImage, TextEncodeQwenImage21, TextGenerate, ComfySwitchNode, PreviewAny, CLIPLoader, PrimitiveStringMultiline, CR Prompt Text, UNETLoader, UNETLoader, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, CLIPLoader, CLIPLoader, VAELoader, ResolutionSelector, PrimitiveBoolean, PrimitiveInt, VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（66 个）：
- `KSampler` ★核心
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextGenerate`
- `ComfySwitchNode`
- `PreviewAny`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（55/66）

**有卡**：`KSampler`、`QwenImage21Cache`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextGenerate`、`CLIPLoader`、`UNETLoader`、`PrimitiveBoolean`、`VAELoader`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
