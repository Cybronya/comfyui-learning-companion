---
key: 视频生成/文生视频/wan2.2-图生视频-20秒长视频_1985192415910838274.json
name: wan2.2-图生视频-20秒长视频_1985192415910838274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-图生视频-20秒长视频_1985192415910838274.json
hash: a01c017526a5f489
coverage: 0.735294
learned_at: 2026-10-11 02:45:03
nodes: [UNETLoader, KSamplerAdvanced, KSamplerAdvanced, Seed (rgthree), Seed (rgthree), KSamplerAdvanced, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, ImageResizeKJv2, VAEDecode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, VAEDecode, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionLoader, WanImageToVideo, CLIPVisionEncode, WanImageToVideo, ImageFromBatch+, CLIPVisionEncode, CLIPVisionLoader, ImageFromBatch+, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, CLIPLoader, easy batchAnything, VHS_VideoCombine, VAEDecode, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, KSamplerAdvanced, VAELoader, KSamplerAdvanced, VAEDecode, easy batchAnything, VHS_VideoCombine, KSamplerAdvanced, easy batchAnything, CLIPVisionLoader, ImageResizeKJv2, Seed (rgthree), Seed (rgthree), WanImageToVideo, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, CR Text, CR Text, CR Text, CR Text, JWInteger, JWInteger, LoadImage]
patterns: []
missing: [CR Text, CR Text, CR Text, CR Text, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy batchAnything, easy batchAnything, easy batchAnything, Seed (rgthree), Seed (rgthree), Seed (rgthree), Seed (rgthree)]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan2.2-图生视频-20秒长视频_1985192415910838274.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-图生视频-20秒长视频_1985192415910838274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（68 个）：
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `WanImageToVideo`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `ImageFromBatch+`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageFromBatch+`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy batchAnything`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy batchAnything`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `easy batchAnything`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `WanImageToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（50/68）

**有卡**：`UNETLoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`ImageResizeKJv2`、`VAEDecode`、`WanImageToVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VHS_VideoCombine`、`VAELoader`、`JWInteger`、`LoadImage`

**缺卡**（18）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy batchAnything`、`easy batchAnything`、`easy batchAnything`、`Seed (rgthree)`、`Seed (rgthree)`、`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
