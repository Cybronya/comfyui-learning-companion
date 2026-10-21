---
key: 图片生成/图生图/Qwen Image 2.1换装编辑后人物一致性无偏差服装光影匹配原图加LoRA工作流_2107917971644571650.json
name: Qwen Image 2.1换装编辑后人物一致性无偏差服装光影匹配原图加LoRA工作流_2107917971644571650
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1换装编辑后人物一致性无偏差服装光影匹配原图加LoRA工作流_2107917971644571650.json
hash: 437f5fa6db314ecf
coverage: 0.766667
learned_at: 2026-10-21 00:42:40
nodes: [ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, ComfySwitchNode, RegexMatch, TextGenerate, RegexReplace, JjkText, PrimitiveBoolean, JjkText, JjkText, TextGenerate, ComfySwitchNode, JjkText, JjkText, RegexMatch, TextGenerate, JjkText, LoadImage, VAEDecode, KSampler, SplitImageWithAlpha, VAELoader, CLIPLoader, LoadImage, StringFormat, JjkShowText, TextEncodeQwenImage21, QwenImage21Cache, Image Comparer (rgthree), SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1换装编辑后人物一致性无偏差服装光影匹配原图加LoRA工作流_2107917971644571650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1换装编辑后人物一致性无偏差服装光影匹配原图加LoRA工作流_2107917971644571650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `RegexMatch`
- `TextGenerate`
- `RegexReplace`
- `JjkText`
- `PrimitiveBoolean`
- `JjkText`
- `JjkText`
- `TextGenerate`
- `ComfySwitchNode`
- `JjkText`
- `JjkText`
- `RegexMatch`
- `TextGenerate`
- `JjkText`
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SplitImageWithAlpha`
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `StringFormat`
- `JjkShowText`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `Image Comparer (rgthree)`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **77%**（46/60）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`RegexMatch`、`TextGenerate`、`RegexReplace`、`PrimitiveBoolean`、`LoadImage`、`VAEDecode`、`KSampler`、`SplitImageWithAlpha`、`VAELoader`、`CLIPLoader`、`StringFormat`、`JjkShowText`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`SaveImage`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
