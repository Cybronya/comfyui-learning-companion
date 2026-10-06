---
key: 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937.json
name: Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937.json
hash: b62b8a5a3d137d13
coverage: 0.723404
learned_at: 2026-10-06 21:47:27
nodes: [VAELoader, CR Prompt Text, QwenPERewriteT8, QwenImage21Cache, KSampler, VAEDecode, easy cleanGpuUsed, ComfySwitchNode, EmptyLatentImage, ResolutionSelector, easy showAnything, UNETLoader, CLIPLoader, TextEncodeQwenImage21, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, QwenImage21SageAttentionT8, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenPERewriteT8, easy cleanGpuUsed, CR Prompt Text, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（47 个）：
- `VAELoader`
- `CR Prompt Text`
- `QwenPERewriteT8`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `QwenImage21SageAttentionT8`
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

覆盖率 **72%**（34/47）

**有卡**：`VAELoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（7）：`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`QwenPERewriteT8`、`easy cleanGpuUsed`、`CR Prompt Text`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
