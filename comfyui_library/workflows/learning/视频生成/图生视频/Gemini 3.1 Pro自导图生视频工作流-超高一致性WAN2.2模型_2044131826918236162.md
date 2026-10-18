---
key: 视频生成/图生视频/Gemini 3.1 Pro自导图生视频工作流-超高一致性WAN2.2模型_2044131826918236162.json
name: Gemini 3.1 Pro自导图生视频工作流-超高一致性WAN2.2模型_2044131826918236162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Gemini 3.1 Pro自导图生视频工作流-超高一致性WAN2.2模型_2044131826918236162.json
hash: 540248a3d77ae4af
coverage: 0.542857
learned_at: 2026-10-15 22:36:36
nodes: [GetNode, GetNode, GetNode, TT_img_enc, TT_img_enc_v2, easy cleanGpuUsed, SetNode, GetNode, ModelSamplingSD3, ModelSamplingSD3, GetNode, GetNode, CLIPVisionEncode, GetNode, CLIPTextEncode, Pick From Batch (mtb), easy imageListToImageBatch, GetNode, PreviewImage, GetNode, ImageListToImageBatch, Pick From Batch (mtb), SetNode, SetNode, PreviewImage, UNETLoader, SetNode, UNETLoader, SetNode, CLIPVisionLoader, SetNode, SetNode, CLIPLoader, SetNode, VAELoader, ModelSamplingSD3, CLIPVisionEncode, CLIPTextEncode, ImageResizeKJv2, Seed (rgthree), ImageScaleBy, easy cleanGpuUsed, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, easy cleanGpuUsed, ImageScaleBy, SetNode, Seed (rgthree), ModelSamplingSD3, GetNode, KSamplerAdvanced, WanImageToVideo, GetNode, SetNode, CLIPTextEncode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, WanImageToVideo, GetNode, VAEDecode, easy cleanGpuUsed, ImageResizeKJv2, GetNode, SetNode, CLIPTextEncode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, KSamplerAdvanced, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, GetNode, easy showAnything, LoadImage, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, JWInteger, JWInteger, SaveImage, SaveImage, PrimitiveNode, RH_LLMAPI_Pro_Node, PrimitiveNode, RH_LLMAPI_Pro_Node, SetNode, LoadImage, GetNode, MathExpression_UTK, GetImageRangeFromBatch, GetImageSize+, GetNode, PreviewImage, Text, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Gemini 3.1 Pro自导图生视频工作流-超高一致性WAN2.2模型_2044131826918236162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044131826918236162.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `TT_img_enc`
- `TT_img_enc_v2`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Pick From Batch (mtb)`
- `easy imageListToImageBatch`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `ImageListToImageBatch`
- `Pick From Batch (mtb)`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `UNETLoader` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `Seed (rgthree)`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `SetNode`
- `Seed (rgthree)`
- `ModelSamplingSD3`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `WanImageToVideo`
- `GetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `easy showAnything`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `SaveImage`
- `SaveImage`
- `PrimitiveNode`
- `RH_LLMAPI_Pro_Node`
- `PrimitiveNode`
- `RH_LLMAPI_Pro_Node`
- `SetNode`
- `LoadImage`
- `GetNode`
- `MathExpression_UTK`
- `GetImageRangeFromBatch`
- `GetImageSize+`
- `GetNode`
- `PreviewImage`
- `Text`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **54%**（57/105）

**有卡**：`TT_img_enc`、`TT_img_enc_v2`、`easy cleanGpuUsed`、`ModelSamplingSD3`、`CLIPVisionEncode`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`easy imageListToImageBatch`、`ImageListToImageBatch`、`UNETLoader`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`ImageResizeKJv2`、`Seed (rgthree)`、`ImageScaleBy`、`VAEDecode`、`KSamplerAdvanced`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VHS_VideoCombine`、`JWInteger`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`MathExpression_UTK`、`GetImageRangeFromBatch`、`GetImageSize+`、`Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
