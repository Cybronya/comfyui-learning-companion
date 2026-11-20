---
key: 平台全量/wan2.1百分百成功的万能修复工作流_低像素修复_面部_手部_任意错误修复_1921116357608292353.json
name: wan2.1百分百成功的万能修复工作流_低像素修复_面部_手部_任意错误修复_1921116357608292353
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1百分百成功的万能修复工作流_低像素修复_面部_手部_任意错误修复_1921116357608292353.json
hash: f2d0be70861fa2ea
coverage: 0.55
learned_at: 2026-11-14 01:19:14
nodes: [VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScale, ImageToMask, LayerMask: MaskPreview, PreviewImage, Image Comparer (rgthree), Anything Everywhere3, VAEDecode, ImageCrop, GetNode, GetNode, GetNode, GetNode, GetNode, ImageScale, SetNode, PreviewImage, ImageScale, SetNode, GrowMaskWithBlur, ImageCompositeMasked, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoNAG, ModelSamplingSD3, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, InpaintModelConditioning, GetNode, GetNode, WanVideoNAG, ModelSamplingSD3, VAEDecode, PreviewImage, GetNode, SaveImage, VAEEncode, GetNode, easy float, RH_Translator, Mask Crop Region, SetNode, SetNode, MaskToImage, KSampler, CLIPTextEncode, CLIPTextEncode, SetNode, LoadImage, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.030000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 449927002644516, "steps": 10}
---

# 平台全量/wan2.1百分百成功的万能修复工作流_低像素修复_面部_手部_任意错误修复_1921116357608292353.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1百分百成功的万能修复工作流_低像素修复_面部_手部_任意错误修复_1921116357608292353.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScale`
- `ImageToMask`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `ImageCrop`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `SetNode`
- `PreviewImage`
- `ImageScale`
- `SetNode`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `GetNode`
- `GetNode`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `PreviewImage`
- `GetNode`
- `SaveImage`
- `VAEEncode` ★核心
- `GetNode`
- `easy float`
- `RH_Translator`
- `Mask Crop Region`
- `SetNode`
- `SetNode`
- `MaskToImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `449927002644516`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.030000000000000006`

## 知识

覆盖率 **55%**（33/60）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageScale`、`ImageToMask`、`LayerMask: MaskPreview`、`VAEDecode`、`ImageCrop`、`GrowMaskWithBlur`、`ImageCompositeMasked`、`WanVideoNAG`、`ModelSamplingSD3`、`CLIPTextEncode`、`InpaintModelConditioning`、`SaveImage`、`VAEEncode`、`easy float`、`RH_Translator`、`Mask Crop Region`、`MaskToImage`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
