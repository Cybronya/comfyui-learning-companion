---
key: 平台全量/Wan2.2 Vace作迁移视频生视频加速版V1（深度_骨骼控制实验版）V2_1950024347340685314.json
name: Wan2.2 Vace作迁移视频生视频加速版V1（深度_骨骼控制实验版）V2_1950024347340685314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Vace作迁移视频生视频加速版V1（深度_骨骼控制实验版）V2_1950024347340685314.json
hash: e4a1fdd9dac25edb
coverage: 0.788462
learned_at: 2026-11-14 01:05:36
nodes: [CLIPLoader, CLIPTextEncode, PathchSageAttentionKJ, UnetLoaderGGUF, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, TrimVideoLatent, VAELoader, UnetLoaderGGUF, WanVideoVAELoader, ImageMirror, DepthAnything_V2, OpenposePreprocessor, ImageFromBatch+, JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, DownloadAndLoadDepthAnythingV2Model, VHS_MergeImages, VHS_VideoCombine, ImpactSwitch, ImpactSwitch, VHS_LoadVideo, Note, Note, DF_Integer, Note, PrimitiveNode, JWInteger, Note, Note, Note, JWInteger, PreviewImage, ImageRepeat, PreviewImage, ImageConcatMulti, VHS_VideoCombine, WanVaceToVideo, ImageFromBatch+, VHS_VideoCombine, LoadImage, CLIPTextEncode, CR Prompt Text, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 平台全量/Wan2.2 Vace作迁移视频生视频加速版V1（深度_骨骼控制实验版）V2_1950024347340685314.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Vace作迁移视频生视频加速版V1（深度_骨骼控制实验版）V2_1950024347340685314.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `WanVideoVAELoader`
- `ImageMirror`
- `DepthAnything_V2`
- `OpenposePreprocessor`
- `ImageFromBatch+`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `DownloadAndLoadDepthAnythingV2Model`
- `VHS_MergeImages`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `ImpactSwitch`
- `VHS_LoadVideo`
- `Note`
- `Note`
- `DF_Integer`
- `Note`
- `PrimitiveNode`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `PreviewImage`
- `ImageRepeat`
- `PreviewImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`TrimVideoLatent`、`VAELoader`、`WanVideoVAELoader`、`ImageMirror`、`DepthAnything_V2`、`OpenposePreprocessor`、`ImageFromBatch+`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`DownloadAndLoadDepthAnythingV2Model`、`VHS_MergeImages`、`VHS_LoadVideo`、`DF_Integer`、`ImageRepeat`、`ImageConcatMulti`、`WanVaceToVideo`、`LoadImage`、`CR Prompt Text`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DepthAnything_V2
