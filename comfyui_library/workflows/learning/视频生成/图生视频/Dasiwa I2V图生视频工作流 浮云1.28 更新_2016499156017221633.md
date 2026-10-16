---
key: 视频生成/图生视频/Dasiwa I2V图生视频工作流 浮云1.28 更新_2016499156017221633.json
name: Dasiwa I2V图生视频工作流 浮云1.28 更新_2016499156017221633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2016499156017221633.json
hash: 0c7b6874ca30cd74
coverage: 0.769231
learned_at: 2026-10-15 22:34:43
nodes: [Note, Note, ImageScaleBy, Note, SaveImage, ColorMatch, ImageScaleBy, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Note, CLIPTextEncode, PreviewImage, Pick From Batch (mtb), PainterI2V, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, UNETLoader, WanImageToVideo, VAEDecode, ImageResizeKJv2, JWInteger, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, JWInteger, VHS_VideoCombine, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Dasiwa I2V图生视频工作流 浮云1.28 更新_2016499156017221633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016499156017221633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `CLIPVisionEncode`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Note`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Pick From Batch (mtb)`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `JWInteger`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `JWInteger`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`ImageScaleBy`、`SaveImage`、`ColorMatch`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`PainterI2V`、`PathchSageAttentionKJ`、`UNETLoader`、`WanImageToVideo`、`VAEDecode`、`ImageResizeKJv2`、`JWInteger`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
