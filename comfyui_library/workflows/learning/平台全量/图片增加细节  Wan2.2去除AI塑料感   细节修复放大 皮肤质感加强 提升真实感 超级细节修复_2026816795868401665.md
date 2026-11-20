---
key: 平台全量/图片增加细节  Wan2.2去除AI塑料感   细节修复放大 皮肤质感加强 提升真实感 超级细节修复_2026816795868401665.json
name: 图片增加细节  Wan2.2去除AI塑料感   细节修复放大 皮肤质感加强 提升真实感 超级细节修复_2026816795868401665
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/图片增加细节  Wan2.2去除AI塑料感   细节修复放大 皮肤质感加强 提升真实感 超级细节修复_2026816795868401665.json
hash: cc0ffbf8e21b8fce
coverage: 0.84
learned_at: 2026-11-14 01:54:45
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere, CLIPTextEncode, VAEEncode, Image Comparer (rgthree), Joy_caption_two, SaveImage, VAEDecode, KSampler, LoadImage, Joy_caption_two_load, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, Anything Everywhere3, VAELoader, CLIPTextEncode, CR Text Concatenate, PreviewAny, ConstrainImage|pysssss, RH_Captioner, TextInput_]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.25, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 791715029150849, "steps": 20}
---

# 平台全量/图片增加细节  Wan2.2去除AI塑料感   细节修复放大 皮肤质感加强 提升真实感 超级细节修复_2026816795868401665.json

> 来源文件 `comfyui_library/workflows/平台全量/图片增加细节  Wan2.2去除AI塑料感   细节修复放大 皮肤质感加强 提升真实感 超级细节修复_2026816795868401665.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `Joy_caption_two`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `Joy_caption_two_load`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `Anything Everywhere3`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `PreviewAny`
- `ConstrainImage|pysssss`
- `RH_Captioner`
- `TextInput_`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `791715029150849`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.25`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEEncode`、`Joy_caption_two`、`SaveImage`、`VAEDecode`、`KSampler`、`LoadImage`、`Joy_caption_two_load`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CR Text Concatenate`、`ConstrainImage|pysssss`、`RH_Captioner`、`TextInput_`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
