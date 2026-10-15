---
key: 视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json
name: 电商服装展示_模特演示视频-wan2.2_2051570109155688449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json
hash: a28bda994ae787d6
coverage: 0.96875
learned_at: 2026-10-15 22:48:55
nodes: [VAELoader, DownloadAndLoadGIMMVFIModel, CLIPLoader, PrimitiveInt, UNETLoader, UNETLoader, Int, Int, Int, Int, SimpleMath+, PathchSageAttentionKJ, LoraLoaderModelOnly, PainterVRAM, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, PathchSageAttentionKJ, CLIPTextEncode, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, GIMMVFI_interpolate, ImageConcatMulti, CLIPTextEncode, INTConstant, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, MathExpression|pysssss, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
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

覆盖率 **97%**（31/32）

**有卡**：`VAELoader`、`DownloadAndLoadGIMMVFIModel`、`CLIPLoader`、`UNETLoader`、`Int`、`SimpleMath+`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`PainterVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`CLIPTextEncode`、`WanImageToVideo`、`KSamplerAdvanced`、`VAEDecode`、`GIMMVFI_interpolate`、`ImageConcatMulti`、`INTConstant`、`VHS_VideoCombine`、`MathExpression|pysssss`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
