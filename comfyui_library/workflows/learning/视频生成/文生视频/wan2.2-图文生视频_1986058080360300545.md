---
key: 视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json
name: wan2.2-图文生视频_1986058080360300545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json
hash: 7d7424df44ae609e
coverage: 0.826087
learned_at: 2026-10-11 02:45:03
nodes: [UNETLoader, UNETLoader, CLIPLoader, WanImageToVideo, CLIPTextEncode, JWInteger, JWInteger, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, MathExpression|pysssss, CLIPVisionEncode, CLIPVisionLoader, Seed (rgthree), KSamplerAdvanced, CR Prompt Text, VAEDecode, VHS_VideoCombine, LoadImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, CR Prompt Text, Seed (rgthree)]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `CR Prompt Text`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`UNETLoader`、`CLIPLoader`、`WanImageToVideo`、`CLIPTextEncode`、`JWInteger`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAELoader`、`ImageResizeKJv2`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
