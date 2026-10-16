---
key: 视频生成/图生视频/全能图片V1+wan2.2-变胖特效-图生视频-视频补帧放大_1962700232851079170.json
name: 全能图片V1+wan2.2-变胖特效-图生视频-视频补帧放大_1962700232851079170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962700232851079170.json
hash: fe8aa1d57e6350d3
coverage: 0.840909
learned_at: 2026-10-15 22:31:31
nodes: [CLIPLoader, VAELoader, CLIPVisionLoader, WanFirstLastFrameToVideo, UNETLoader, UNETLoader, CLIPTextEncode, RH_Translator, easy showAnything, easy ifElse, LoraLoaderModelOnly, CLIPVisionEncode, CLIPVisionEncode, KSamplerAdvanced, KSamplerAdvanced, RIFE VFI, CR Upscale Image, VAEDecode, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, PreviewImage, SimpleMath+, DF_Integer, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, RH_Nano_Banana_Image2Image, RH_Translator, LayerUtility: ImageMaskScaleAs, ImageStitch, RH_Captioner, easy showAnything, PreviewImage, LoadImage, PreviewImage, PrimitiveBoolean, Textbox, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/全能图片V1+wan2.2-变胖特效-图生视频-视频补帧放大_1962700232851079170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962700232851079170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `easy showAnything`
- `easy ifElse`
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
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
- `SimpleMath+`
- `DF_Integer`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `RH_Nano_Banana_Image2Image`
- `RH_Translator`
- `LayerUtility: ImageMaskScaleAs`
- `ImageStitch`
- `RH_Captioner`
- `easy showAnything`
- `PreviewImage`
- `LoadImage`
- `PreviewImage`
- `PrimitiveBoolean`
- `Textbox`
- `VHS_VideoCombine`
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

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`UNETLoader`、`CLIPTextEncode`、`RH_Translator`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`KSamplerAdvanced`、`RIFE VFI`、`CR Upscale Image`、`VAEDecode`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`SimpleMath+`、`DF_Integer`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Nano_Banana_Image2Image`、`LayerUtility: ImageMaskScaleAs`、`ImageStitch`、`RH_Captioner`、`LoadImage`、`PrimitiveBoolean`、`Textbox`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
