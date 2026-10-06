---
key: 图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json
name: 全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json
hash: 07b41ddeb662fb71
coverage: 0.52439
learned_at: 2026-10-07 02:41:09
nodes: [CLIPLoader, GetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, QwenImage21Cache, Seed (rgthree), EmptyLatentImage, GetNode, SetNode, VAELoader, UNETLoader, SetNode, GetNode, QwenPERewriteT8, ShowText|pysssss, GetNode, GetNode, SetNode, SaveImageAdvanced, VAEDecode, SaveImage, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, SetNode, SetNode, SetNode, SetNode, LoadImage, ComfySwitchNode, ResolutionSelector, SetNode, Text Multiline, Image Comparer (rgthree), LoadImage, LoadImage, XinbaoImageStandardizer, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Text Multiline, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `QwenImage21Cache`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `GetNode`
- `SetNode`
- `VAELoader`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `QwenPERewriteT8`
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `SetNode`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `ComfySwitchNode`
- `ResolutionSelector`
- `SetNode`
- `Text Multiline`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `XinbaoImageStandardizer`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **52%**（43/82）

**有卡**：`CLIPLoader`、`LoadImage`、`QwenImage21Cache`、`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`QwenPERewriteT8`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`KSampler`、`TextEncodeQwenImage21`、`ResolutionSelector`、`XinbaoImageStandardizer`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`Text Multiline`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
