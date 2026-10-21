---
key: 图片生成/图生图/Qwen Image 2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2102833574943744001.json
name: Qwen Image 2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2102833574943744001
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2102833574943744001.json
hash: 5474cca6fbeabe2b
coverage: 0.852941
learned_at: 2026-10-21 00:42:35
nodes: [VAEDecode, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy showAnything, VAELoader, UNETLoader, PrimitiveBoolean, CLIPLoader, BatchImagesNode, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, TextGenerateLTX2Prompt, SaveImage, ResolutionSelector, Fast Groups Muter (rgthree), ImageMergeNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, TextEncodeQwenImage21, LoraLoaderModelOnly, Fast Groups Muter (rgthree), LoadImage, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2102833574943744001.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2102833574943744001.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `VAELoader`
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `CLIPLoader`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `SaveImage`
- `ResolutionSelector`
- `Fast Groups Muter (rgthree)`
- `ImageMergeNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Muter (rgthree)`
- `LoadImage`
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

覆盖率 **85%**（58/68）

**有卡**：`VAEDecode`、`CLIPLoader`、`LoadImage`、`VAELoader`、`UNETLoader`、`PrimitiveBoolean`、`BatchImagesNode`、`TextGenerateLTX2Prompt`、`SaveImage`、`ResolutionSelector`、`ImageMergeNode`、`KSampler`、`QwenImage21Cache`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
