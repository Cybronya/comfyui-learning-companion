---
key: 视频生成/图生视频/全能图片V1+wan2.2-变老特效-图生视频-视频补帧放大_1962663438763864066.json
name: 全能图片V1+wan2.2-变老特效-图生视频-视频补帧放大_1962663438763864066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962663438763864066.json
hash: cd9d18b4fadc74ba
coverage: 0.840909
learned_at: 2026-10-15 22:31:31
nodes: [CLIPLoader, VAELoader, CLIPVisionLoader, WanFirstLastFrameToVideo, UNETLoader, UNETLoader, ImageStitch, CLIPTextEncode, LoadImage, PreviewImage, RH_Captioner, easy showAnything, RH_Translator, easy showAnything, PrimitiveBoolean, easy ifElse, Textbox, LoraLoaderModelOnly, CLIPVisionEncode, CLIPVisionEncode, LayerUtility: ImageMaskScaleAs, KSamplerAdvanced, KSamplerAdvanced, RIFE VFI, PreviewImage, CR Upscale Image, VAEDecode, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, PreviewImage, RH_Nano_Banana_Image2Image, RH_Translator, SimpleMath+, DF_Integer, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/全能图片V1+wan2.2-变老特效-图生视频-视频补帧放大_1962663438763864066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962663438763864066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PreviewImage`
- `RH_Captioner`
- `easy showAnything`
- `RH_Translator`
- `easy showAnything`
- `PrimitiveBoolean`
- `easy ifElse`
- `Textbox`
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LayerUtility: ImageMaskScaleAs`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
- `PreviewImage`
- `CR Upscale Image`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `RH_Translator`
- `SimpleMath+`
- `DF_Integer`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`UNETLoader`、`ImageStitch`、`CLIPTextEncode`、`LoadImage`、`RH_Captioner`、`RH_Translator`、`PrimitiveBoolean`、`Textbox`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`LayerUtility: ImageMaskScaleAs`、`KSamplerAdvanced`、`RIFE VFI`、`CR Upscale Image`、`VAEDecode`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`RH_Nano_Banana_Image2Image`、`SimpleMath+`、`DF_Integer`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
