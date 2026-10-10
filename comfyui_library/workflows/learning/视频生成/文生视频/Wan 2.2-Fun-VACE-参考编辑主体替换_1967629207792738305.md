---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE-参考编辑主体替换_1967629207792738305.json
name: Wan 2.2-Fun-VACE-参考编辑主体替换_1967629207792738305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-参考编辑主体替换_1967629207792738305.json
hash: a2bf3c5dc1ecc5a0
coverage: 0.942857
learned_at: 2026-10-10 23:06:08
nodes: [TrimVideoLatent, VAEDecode, CLIPTextEncode, VHS_VideoCombine, WanVaceToVideo, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, InvertMask, MaskToImage, GetImageSize+, VHS_DuplicateMasks, GrowMaskWithBlur, SolidMask, VHS_VideoCombine, PreviewImage, INTConstant, InspyrenetRembg, ImageCompositeMasked, ImageResizeKJv2, KSamplerAdvanced, VAELoader, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_LoadVideo, CLIPTextEncode, LoadImage, Miaoshouai_Tagger]
patterns: []
missing: [GetImageSize+]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "sa_solver_pece", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan 2.2-Fun-VACE-参考编辑主体替换_1967629207792738305.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-参考编辑主体替换_1967629207792738305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `InvertMask`
- `MaskToImage`
- `GetImageSize+`
- `VHS_DuplicateMasks`
- `GrowMaskWithBlur`
- `SolidMask`
- `VHS_VideoCombine`
- `PreviewImage`
- `INTConstant`
- `InspyrenetRembg`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Miaoshouai_Tagger`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `sa_solver_pece`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanVaceToVideo`、`ModelSamplingSD3`、`CLIPLoader`、`InvertMask`、`MaskToImage`、`VHS_DuplicateMasks`、`GrowMaskWithBlur`、`SolidMask`、`INTConstant`、`InspyrenetRembg`、`ImageCompositeMasked`、`ImageResizeKJv2`、`KSamplerAdvanced`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VHS_LoadVideo`、`LoadImage`、`Miaoshouai_Tagger`

**缺卡**（1）：`GetImageSize+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
