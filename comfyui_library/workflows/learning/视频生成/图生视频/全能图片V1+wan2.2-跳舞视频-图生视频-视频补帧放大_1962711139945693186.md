---
key: 视频生成/图生视频/全能图片V1+wan2.2-跳舞视频-图生视频-视频补帧放大_1962711139945693186.json
name: 全能图片V1+wan2.2-跳舞视频-图生视频-视频补帧放大_1962711139945693186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962711139945693186.json
hash: 8d4782e4412693be
coverage: 0.844444
learned_at: 2026-10-15 22:31:31
nodes: [CLIPLoader, VAELoader, CLIPVisionLoader, WanFirstLastFrameToVideo, UNETLoader, UNETLoader, ImageStitch, CLIPTextEncode, RH_Captioner, RH_Translator, easy showAnything, PrimitiveBoolean, easy ifElse, LoraLoaderModelOnly, CLIPVisionEncode, CLIPVisionEncode, LayerUtility: ImageMaskScaleAs, KSamplerAdvanced, KSamplerAdvanced, RIFE VFI, PreviewImage, CR Upscale Image, VAEDecode, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, PreviewImage, SimpleMath+, DF_Integer, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, MarkdownNote, RH_Translator, LoadImage, PreviewImage, easy showAnything, Textbox, RH_Nano_Banana_Image2Image, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/全能图片V1+wan2.2-跳舞视频-图生视频-视频补帧放大_1962711139945693186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962711139945693186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `RH_Translator`
- `easy showAnything`
- `PrimitiveBoolean`
- `easy ifElse`
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
- `SimpleMath+`
- `DF_Integer`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `RH_Translator`
- `LoadImage`
- `PreviewImage`
- `easy showAnything`
- `Textbox`
- `RH_Nano_Banana_Image2Image`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`UNETLoader`、`ImageStitch`、`CLIPTextEncode`、`RH_Captioner`、`RH_Translator`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`LayerUtility: ImageMaskScaleAs`、`KSamplerAdvanced`、`RIFE VFI`、`CR Upscale Image`、`VAEDecode`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`SimpleMath+`、`DF_Integer`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Textbox`、`RH_Nano_Banana_Image2Image`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
