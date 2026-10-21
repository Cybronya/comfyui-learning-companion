---
key: 图片生成/文生图/Anima+Aesthetic+1.1｜图生图+CN+修脸+修手_2078701753071136769.json
name: Anima+Aesthetic+1.1｜图生图+CN+修脸+修手_2078701753071136769
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜图生图+CN+修脸+修手_2078701753071136769.json
hash: 2181a61af238ddb1
coverage: 0.75
learned_at: 2026-10-20 00:18:47
nodes: [Float, PreviewImage, PreviewImage, PreviewImage, UltralyticsDetectorProvider, UltralyticsDetectorProvider, UltralyticsDetectorProvider, SAMLoader, FaceDetailer, UNETLoader, PreviewImage, FaceDetailer, Seed (rgthree), AIO_Preprocessor, PreviewImage, NAGuidance, LoadImage, ImageScale, ClownsharKSampler_Beta, LoadImage, LoraLoaderModelOnly, XB_UNetNameBroadcaster, UNETLoader, CLIPTextEncode, CLIPTextEncode, AnimaLLLiteApply, VAEEncode, VAELoader, RH_LLMAPI_Pro_Node, image_scale_pixel_v2, WD14Tagger|pysssss, CLIPLoader, PreviewImage, PreviewImage, VAEDecode, SaveImage, PreviewImage, PreviewImage, PreviewImage, UltralyticsDetectorProvider, UltralyticsDetectorProvider, UltralyticsDetectorProvider, SAMLoader, FaceDetailer, PreviewImage, FaceDetailer, Seed (rgthree), PreviewImage, PreviewImage, VAEDecode, SaveImage, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3, "denoise": 0.8400000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 30}
---

# 图片生成/文生图/Anima+Aesthetic+1.1｜图生图+CN+修脸+修手_2078701753071136769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima+Aesthetic+1.1｜图生图+CN+修脸+修手_2078701753071136769.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `Float`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `FaceDetailer`
- `UNETLoader` ★核心
- `PreviewImage`
- `FaceDetailer`
- `Seed (rgthree)`
- `AIO_Preprocessor`
- `PreviewImage`
- `NAGuidance`
- `LoadImage`
- `ImageScale`
- `ClownsharKSampler_Beta` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `XB_UNetNameBroadcaster`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AnimaLLLiteApply`
- `VAEEncode` ★核心
- `VAELoader`
- `RH_LLMAPI_Pro_Node`
- `image_scale_pixel_v2`
- `WD14Tagger|pysssss`
- `CLIPLoader`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `FaceDetailer`
- `PreviewImage`
- `FaceDetailer`
- `Seed (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `0`
- `steps` = `30`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8400000000000002`

## 知识

覆盖率 **75%**（39/52）

**有卡**：`Float`、`UltralyticsDetectorProvider`、`SAMLoader`、`FaceDetailer`、`UNETLoader`、`Seed (rgthree)`、`AIO_Preprocessor`、`NAGuidance`、`LoadImage`、`ImageScale`、`ClownsharKSampler_Beta`、`LoraLoaderModelOnly`、`XB_UNetNameBroadcaster`、`CLIPTextEncode`、`AnimaLLLiteApply`、`VAEEncode`、`VAELoader`、`RH_LLMAPI_Pro_Node`、`image_scale_pixel_v2`、`WD14Tagger|pysssss`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
