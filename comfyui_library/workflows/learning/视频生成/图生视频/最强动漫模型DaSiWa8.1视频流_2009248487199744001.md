---
key: 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流_2009248487199744001.json
name: 最强动漫模型DaSiWa8.1视频流_2009248487199744001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2009248487199744001.json
hash: 88145a43ac394f7d
coverage: 0.391892
learned_at: 2026-10-15 22:34:11
nodes: [Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, INTConstant, INTConstant, Reroute, Reroute, Reroute, Reroute, Int, Note, PreviewImage, Reroute, CLIPTextEncode, Reroute, ModelSamplingSD3, TextInput_, Reroute, Note, Int, GetImagesFromBatchIndexed, KSamplerAdvanced, KSamplerAdvanced, Reroute, CLIPTextEncode, Fast Groups Bypasser (rgthree), Note, Note, PainterI2V, RIFE VFI, Qwen3_VQA, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, JoinStrings, ShowText|pysssss, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPLoader, VHS_VideoCombine, LoadImage, easy showAnything, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流_2009248487199744001.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009248487199744001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `Note`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Note`
- `PreviewImage`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `ModelSamplingSD3`
- `TextInput_`
- `Reroute`
- `Note`
- `Int`
- `GetImagesFromBatchIndexed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `PainterI2V`
- `RIFE VFI`
- `Qwen3_VQA`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `JoinStrings`
- `ShowText|pysssss`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `easy showAnything`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **39%**（29/74）

**有卡**：`ModelPatchTorchSettings`、`VAELoader`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`VAEDecode`、`INTConstant`、`Int`、`CLIPTextEncode`、`TextInput_`、`GetImagesFromBatchIndexed`、`KSamplerAdvanced`、`PainterI2V`、`RIFE VFI`、`Qwen3_VQA`、`LayerUtility: ImageScaleByAspectRatio V2`、`JoinStrings`、`PathchSageAttentionKJ`、`CLIPLoader`、`VHS_VideoCombine`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、GetImagesFromBatchIndexed
