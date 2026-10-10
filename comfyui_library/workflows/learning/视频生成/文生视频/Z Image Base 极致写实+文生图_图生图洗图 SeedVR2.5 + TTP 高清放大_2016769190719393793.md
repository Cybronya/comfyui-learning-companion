---
key: 视频生成/文生视频/Z Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016769190719393793.json
name: Z Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016769190719393793
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Z Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016769190719393793.json
hash: b947391234fd6ad0
coverage: 0.660377
learned_at: 2026-10-11 03:07:13
nodes: [Reroute, LayerUtility: ImageReelComposit, ImpactInt, CLIPTextEncode, CLIPTextEncode, VAEDecode, LayerUtility: ImageReel, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, SaveImage, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler, ImageScaleBy, Image Filter Adjustments, Image Comparer (rgthree), KSampler, VAEEncode, CLIPTextEncode, SomethingToString, PlaySound|pysssss, VAEDecode, KSampler, EmptySD3LatentImage, VAELoader, UNETLoader, INTConstant, INTConstant, ModelSamplingAuraFlow, SaveImage, CLIPLoader, SeedVR2VideoUpscaler, Image Filter Adjustments, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, Qwen3_VQA, ShowText|pysssss, PreviewImage, PrimitiveFloat, Note, SaveImage, CR Text, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage]
patterns: [image_to_image]
missing: [CR Text, Image Filter Adjustments, Image Filter Adjustments, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss]
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 978471420599265, "steps": 25}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Image Filter Adjustments` 知识库中没有该节点类型的任何知识, 次要节点 `Image Filter Adjustments` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Z Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016769190719393793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Z Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016769190719393793.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `Reroute`
- `LayerUtility: ImageReelComposit`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `Image Filter Adjustments`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `SomethingToString`
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `VAELoader`
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `CLIPLoader`
- `SeedVR2VideoUpscaler`
- `Image Filter Adjustments`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `PreviewImage`
- `PrimitiveFloat`
- `Note`
- `SaveImage`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `978471420599265`
- `steps` = `25`
- `cfg` = `3`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（35/53）

**有卡**：`ImpactInt`、`CLIPTextEncode`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SaveImage`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`KSampler`、`VAEEncode`、`SomethingToString`、`EmptySD3LatentImage`、`VAELoader`、`UNETLoader`、`INTConstant`、`ModelSamplingAuraFlow`、`CLIPLoader`、`Qwen3_VQA`、`LoadImage`

**缺卡**（7）：`CR Text`、`Image Filter Adjustments`、`Image Filter Adjustments`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageScaleByAspectRatio V2`、`PlaySound|pysssss`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SeedVR2LoadDiTModel

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Filter Adjustments` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Filter Adjustments` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
