---
key: 图片生成/文生图/一句话图像编辑Flux kontext黑森林RunningHub专用节点工作流文生图图生图_2088432747160367105.json
name: 一句话图像编辑Flux kontext黑森林RunningHub专用节点工作流文生图图生图_2088432747160367105
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一句话图像编辑Flux kontext黑森林RunningHub专用节点工作流文生图图生图_2088432747160367105.json
hash: 28fb825d9d4e6898
coverage: 0.780488
learned_at: 2026-10-20 01:00:11
nodes: [SetNode, GetNode, SaveImage, LoadImage, Bjornulf_ShowStringText, RH_Translator, ShowText|pysssss, Bjornulf_ShowStringText, SetNode, GetNode, RH_ComfyFluxKontext, Comfly_Flux_Kontext, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/一句话图像编辑Flux kontext黑森林RunningHub专用节点工作流文生图图生图_2088432747160367105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一句话图像编辑Flux kontext黑森林RunningHub专用节点工作流文生图图生图_2088432747160367105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（41 个）：
- `SetNode`
- `GetNode`
- `SaveImage`
- `LoadImage`
- `Bjornulf_ShowStringText`
- `RH_Translator`
- `ShowText|pysssss`
- `Bjornulf_ShowStringText`
- `SetNode`
- `GetNode`
- `RH_ComfyFluxKontext`
- `Comfly_Flux_Kontext`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **78%**（32/41）

**有卡**：`SaveImage`、`LoadImage`、`Bjornulf_ShowStringText`、`RH_Translator`、`RH_ComfyFluxKontext`、`Comfly_Flux_Kontext`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
