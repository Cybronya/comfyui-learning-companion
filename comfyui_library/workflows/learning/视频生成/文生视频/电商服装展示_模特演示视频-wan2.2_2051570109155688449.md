---
key: 视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json
name: 电商服装展示_模特演示视频-wan2.2_2051570109155688449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json
hash: a28bda994ae787d6
coverage: 0.84375
learned_at: 2026-10-11 19:49:50
nodes: [VAELoader, DownloadAndLoadGIMMVFIModel, CLIPLoader, PrimitiveInt, UNETLoader, UNETLoader, Int, Int, Int, Int, SimpleMath+, PathchSageAttentionKJ, LoraLoaderModelOnly, PainterVRAM, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, PathchSageAttentionKJ, CLIPTextEncode, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, GIMMVFI_interpolate, ImageConcatMulti, CLIPTextEncode, INTConstant, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, MathExpression|pysssss, LoadImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `VAELoader`
- `DownloadAndLoadGIMMVFIModel`
- `CLIPLoader`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Int`
- `Int`
- `Int`
- `Int`
- `SimpleMath+`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PainterVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GIMMVFI_interpolate`
- `ImageConcatMulti`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`VAELoader`、`DownloadAndLoadGIMMVFIModel`、`CLIPLoader`、`UNETLoader`、`Int`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`PainterVRAM`、`ModelSamplingSD3`、`CLIPTextEncode`、`WanImageToVideo`、`KSamplerAdvanced`、`VAEDecode`、`GIMMVFI_interpolate`、`ImageConcatMulti`、`INTConstant`、`VHS_VideoCombine`、`LoadImage`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
