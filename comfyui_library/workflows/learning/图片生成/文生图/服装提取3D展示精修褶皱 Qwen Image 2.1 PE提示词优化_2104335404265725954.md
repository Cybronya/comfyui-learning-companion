---
key: 服装提取3D展示精修褶皱 Qwen Image 2.1 PE提示词优化_2104335404265725954.json
name: 服装提取3D展示精修褶皱 Qwen Image 2.1 PE提示词优化_2104335404265725954
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/服装提取3D展示精修褶皱 Qwen Image 2.1 PE提示词优化_2104335404265725954.json
hash: a70366ff302e0742
coverage: 0.859649
learned_at: 2026-10-10 20:59:50
nodes: [LoadImage, VAELoader, VAEDecode, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, easy seed, Text Multiline, ResolutionSelector, CLIPLoader, EmptyLatentImage, QwenPERewriteT8, Display Any (rgthree), UNETLoader, QwenImage21SageAttentionT8, TextEncodeQwenImage21, SaveImage, ImageStitch, SaveImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Display Any (rgthree), Text Multiline, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 服装提取3D展示精修褶皱 Qwen Image 2.1 PE提示词优化_2104335404265725954.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/服装提取3D展示精修褶皱 Qwen Image 2.1 PE提示词优化_2104335404265725954.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `LoadImage`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `easy seed`
- `Text Multiline`
- `ResolutionSelector`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `QwenPERewriteT8`
- `Display Any (rgthree)`
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `TextEncodeQwenImage21`
- `SaveImage`
- `ImageStitch`
- `SaveImage`
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

覆盖率 **86%**（49/57）

**有卡**：`LoadImage`、`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`ResolutionSelector`、`CLIPLoader`、`EmptyLatentImage`、`QwenPERewriteT8`、`UNETLoader`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`SaveImage`、`ImageStitch`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（3）：`Display Any (rgthree)`、`Text Multiline`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
