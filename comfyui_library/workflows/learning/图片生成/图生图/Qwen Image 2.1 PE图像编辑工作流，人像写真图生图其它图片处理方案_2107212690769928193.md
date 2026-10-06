---
key: 图片生成/图生图/Qwen Image 2.1 PE图像编辑工作流，人像写真图生图其它图片处理方案_2107212690769928193.json
name: Qwen Image 2.1 PE图像编辑工作流，人像写真图生图其它图片处理方案_2107212690769928193
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE图像编辑工作流，人像写真图生图其它图片处理方案_2107212690769928193.json
hash: ec4e2e547fcdf58d
coverage: 0.857143
learned_at: 2026-10-07 02:41:22
nodes: [VAELoader, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, LoadImage, UNETLoader, easy showAnything, CLIPLoader, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, QwenImage21Cache, KSampler, easy cleanGpuUsed, SaveImage, VAEDecode, TextEncodeQwenImage21, ComfySwitchNode, ResolutionSelector, EmptyLatentImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy cleanGpuUsed, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 PE图像编辑工作流，人像写真图生图其它图片处理方案_2107212690769928193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE图像编辑工作流，人像写真图生图其它图片处理方案_2107212690769928193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `VAELoader`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenPERewriteT8`
- `LoadImage`
- `UNETLoader` ★核心
- `easy showAnything`
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `LoadImage`
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

覆盖率 **86%**（48/56）

**有卡**：`VAELoader`、`LoadImage`、`QwenPERewriteT8`、`UNETLoader`、`CLIPLoader`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`QwenImage21Cache`、`KSampler`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
