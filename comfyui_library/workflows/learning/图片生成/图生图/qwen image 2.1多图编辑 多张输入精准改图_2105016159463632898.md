---
key: 图片生成/图生图/qwen image 2.1多图编辑 多张输入精准改图_2105016159463632898.json
name: qwen image 2.1多图编辑 多张输入精准改图_2105016159463632898
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1多图编辑 多张输入精准改图_2105016159463632898.json
hash: c962d4ea263fae80
coverage: 0.877193
learned_at: 2026-10-21 00:46:01
nodes: [SaveImage, SaveImage, UNETLoader, LoadImage, ImpactInt, easy imageScaleDownToSize, GetImageSize, EmptyLatentImage, CLIPLoader, VAELoader, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, ImageConcatMulti, ImageConcatMulti, KSampler, QwenPERewriteT8, ShowText|pysssss, VAEDecode, XinbaoImageStandardizer, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen image 2.1多图编辑 多张输入精准改图_2105016159463632898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1多图编辑 多张输入精准改图_2105016159463632898.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `ImpactInt`
- `easy imageScaleDownToSize`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAELoader`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `KSampler` ★核心
- `QwenPERewriteT8`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `XinbaoImageStandardizer`
- `Image Comparer (rgthree)`
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

覆盖率 **88%**（50/57）

**有卡**：`SaveImage`、`UNETLoader`、`LoadImage`、`ImpactInt`、`easy imageScaleDownToSize`、`GetImageSize`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`CR Text`、`ImageConcatMulti`、`KSampler`、`QwenPERewriteT8`、`VAEDecode`、`XinbaoImageStandardizer`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
