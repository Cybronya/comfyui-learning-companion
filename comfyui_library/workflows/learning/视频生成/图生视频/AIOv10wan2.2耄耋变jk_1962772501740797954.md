---
key: 视频生成/图生视频/AIOv10wan2.2耄耋变jk_1962772501740797954.json
name: AIOv10wan2.2耄耋变jk_1962772501740797954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962772501740797954.json
hash: 00bfcddc59baee55
coverage: 0.666667
learned_at: 2026-10-15 22:31:32
nodes: [GetNode, GetNode, Int, Int, SetNode, Int, SetNode, SetNode, Int, SetNode, GetNode, GetNode, Int, SetNode, Int, SetNode, Int, SetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, workflow>加速节点, Note, Note, Seed Everywhere, workflow>Clip Text, GetNode, CheckpointLoaderSimple, VAEDecode, Fast Groups Bypasser (rgthree), KSamplerAdvanced, DF_Integer, SimpleMath+, GetNode, Note, workflow>加速节点, VHS_VideoCombine, VAEDecode, Note, CLIPVisionEncode, SimpleMath+, CLIPVisionLoader, Fast Groups Bypasser (rgthree), KSamplerAdvanced, WanImageToVideo, VAEDecodeTiled, SaveLatent, VHS_SplitImages, Seed Everywhere, StringLength, PreviewImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SaveTextFile, easy imageToBase64, easy loadImageBase64, VHS_SplitImages, VHS_VideoCombine, PrimitiveString, Note, JjkText, JoinStrings, ShowText, ShowText, KSamplerAdvanced, KSamplerAdvanced, SaveImage, workflow>Clip Text, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "wan2.2-t2v-rapid-aio-v10.safetensors", "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/AIOv10wan2.2耄耋变jk_1962772501740797954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962772501740797954.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `GetNode`
- `GetNode`
- `Int`
- `Int`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `Int`
- `SetNode`
- `GetNode`
- `GetNode`
- `Int`
- `SetNode`
- `Int`
- `SetNode`
- `Int`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `workflow>加速节点`
- `Note`
- `Note`
- `Seed Everywhere`
- `workflow>Clip Text`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `DF_Integer`
- `SimpleMath+`
- `GetNode`
- `Note`
- `workflow>加速节点`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Note`
- `CLIPVisionEncode`
- `SimpleMath+`
- `CLIPVisionLoader`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `VAEDecodeTiled` ★核心
- `SaveLatent`
- `VHS_SplitImages`
- `Seed Everywhere`
- `StringLength`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveTextFile`
- `easy imageToBase64`
- `easy loadImageBase64`
- `VHS_SplitImages`
- `VHS_VideoCombine`
- `PrimitiveString`
- `Note`
- `JjkText`
- `JoinStrings`
- `ShowText`
- `ShowText`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `workflow>Clip Text`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-v10.safetensors`
- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **67%**（48/72）

**有卡**：`Int`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`workflow>加速节点`、`Seed Everywhere`、`workflow>Clip Text`、`CheckpointLoaderSimple`、`VAEDecode`、`KSamplerAdvanced`、`DF_Integer`、`SimpleMath+`、`VHS_VideoCombine`、`CLIPVisionEncode`、`CLIPVisionLoader`、`WanImageToVideo`、`VAEDecodeTiled`、`SaveLatent`、`VHS_SplitImages`、`StringLength`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveTextFile`、`easy imageToBase64`、`easy loadImageBase64`、`JoinStrings`、`ShowText`、`SaveImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、LoadImage、KSamplerAdvanced、Seed Everywhere、SaveLatent、VAEDecodeTiled
