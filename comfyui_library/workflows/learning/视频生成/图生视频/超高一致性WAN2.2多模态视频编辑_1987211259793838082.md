---
key: 视频生成/图生视频/超高一致性WAN2.2多模态视频编辑_1987211259793838082.json
name: 超高一致性WAN2.2多模态视频编辑_1987211259793838082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/超高一致性WAN2.2多模态视频编辑_1987211259793838082.json
hash: 879fc59441cd6211
coverage: 0.773333
learned_at: 2026-10-15 22:32:58
nodes: [JWInteger, JWInteger, LoadImage, SaveImage, SaveImage, UNETLoader, CLIPTextEncode, ModelSamplingSD3, VAEDecode, easy cleanGpuUsed, Pick From Batch (mtb), CLIPVisionEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, RH_LLMAPI_NODE, easy showAnything, easy cleanGpuUsed, Pick From Batch (mtb), RH_LLMAPI_NODE, GetImageRangeFromBatch, CLIPVisionLoader, CLIPLoader, Seed (rgthree), CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, easy cleanGpuUsed, GetImageSize+, SaveImage, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionEncode, ModelSamplingSD3, CLIPTextEncode, ModelSamplingSD3, WanImageToVideo, VAEDecode, KSamplerAdvanced, GetNode, SetNode, SetNode, ModelSamplingSD3, UNETLoader, SetNode, SetNode, SetNode, Seed (rgthree), ImageScaleBy, WanImageToVideo, ImageResizeKJv2, KSamplerAdvanced, KSamplerAdvanced, easy cleanGpuUsed, VHS_VideoCombine, easy imageListToImageBatch, SetNode, PreviewImage, VAELoader, Pick From Batch (mtb), easy imageListToImageBatch, PreviewImage, Pick From Batch (mtb), SetNode, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleBy, JWInteger, VHS_VideoCombine, TT_img_enc_v2, TT_img_enc, MathExpression_UTK, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/超高一致性WAN2.2多模态视频编辑_1987211259793838082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987211259793838082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `RH_LLMAPI_NODE`
- `GetImageRangeFromBatch`
- `CLIPVisionLoader`
- `CLIPLoader`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `GetImageSize+`
- `SaveImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `Seed (rgthree)`
- `ImageScaleBy`
- `WanImageToVideo`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `easy imageListToImageBatch`
- `SetNode`
- `PreviewImage`
- `VAELoader`
- `Pick From Batch (mtb)`
- `easy imageListToImageBatch`
- `PreviewImage`
- `Pick From Batch (mtb)`
- `SetNode`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleBy`
- `JWInteger`
- `VHS_VideoCombine`
- `TT_img_enc_v2`
- `TT_img_enc`
- `MathExpression_UTK`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（58/75）

**有卡**：`JWInteger`、`LoadImage`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecode`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_LLMAPI_NODE`、`GetImageRangeFromBatch`、`CLIPVisionLoader`、`CLIPLoader`、`Seed (rgthree)`、`ImageResizeKJv2`、`KSamplerAdvanced`、`GetImageSize+`、`WanImageToVideo`、`ImageScaleBy`、`VHS_VideoCombine`、`easy imageListToImageBatch`、`VAELoader`、`TT_img_enc_v2`、`TT_img_enc`、`MathExpression_UTK`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
