---
key: 图片生成/文生图/z image controlnet（cnet）【支持切换】_2001231394615554050.json
name: z image controlnet（cnet）【支持切换】_2001231394615554050
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z image controlnet（cnet）【支持切换】_2001231394615554050.json
hash: efee73e17b551ed1
coverage: 0.685714
learned_at: 2026-10-19 21:47:22
nodes: [PreviewImage, AIO_Preprocessor, AIO_Preprocessor, ModelSamplingAuraFlow, VAEDecode, CLIPLoader, EmptyLatentImage, QwenImageDiffsynthControlnet, AIO_Preprocessor, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, CLIPTextEncode, AIO_Preprocessor, JWInteger, JWInteger, KSampler, DF_Text_Box, Image Switch (JPS), DF_Float, LoadImage, AIO_Preprocessor, MarkdownNote, SaveImage, VAELoader, UNETLoader, ConditioningZeroOut, ModelPatchLoader, MarkdownNote, MarkdownNote, MarkdownNote, JWInteger, MarkdownNote]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 934918328292713, "steps": 10, "width": 768}
---

# 图片生成/文生图/z image controlnet（cnet）【支持切换】_2001231394615554050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z image controlnet（cnet）【支持切换】_2001231394615554050.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（35 个）：
- `PreviewImage`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `QwenImageDiffsynthControlnet`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `JWInteger`
- `JWInteger`
- `KSampler` ★核心
- `DF_Text_Box`
- `Image Switch (JPS)`
- `DF_Float`
- `LoadImage`
- `AIO_Preprocessor`
- `MarkdownNote`
- `SaveImage`
- `VAELoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `ModelPatchLoader`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `JWInteger`
- `MarkdownNote`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `934918328292713`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（24/35）

**有卡**：`AIO_Preprocessor`、`ModelSamplingAuraFlow`、`VAEDecode`、`CLIPLoader`、`EmptyLatentImage`、`QwenImageDiffsynthControlnet`、`CLIPTextEncode`、`JWInteger`、`KSampler`、`DF_Text_Box`、`Image Switch (JPS)`、`DF_Float`、`LoadImage`、`SaveImage`、`VAELoader`、`UNETLoader`、`ConditioningZeroOut`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
