---
key: 视频生成/图生视频/WAN2.2-FUN-CN【线稿深度姿势可选】_1957010325603061761.json
name: WAN2.2-FUN-CN【线稿深度姿势可选】_1957010325603061761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957010325603061761.json
hash: 157aacd06dfffcb9
coverage: 0.875
learned_at: 2026-10-15 22:31:15
nodes: [ModelSamplingSD3, VAEDecode, CLIPLoader, VAELoader, LoadImage, MarkdownNote, UNETLoader, CLIPTextEncode, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJ, ImageResizeKJv2, MathExpression|pysssss, LoadVideoDepthAnythingModel, CreateVideo, SaveVideo, Wan22FunControlToVideo, VideoDepthAnythingProcess, ControlNextGetPoses, Canny, VHS_LoadVideo, ImageResizeKJv2, PreviewImage, PreviewImage, easy anythingIndexSwitch, PreviewImage, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2-FUN-CN【线稿深度姿势可选】_1957010325603061761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957010325603061761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `LoadVideoDepthAnythingModel`
- `CreateVideo`
- `SaveVideo`
- `Wan22FunControlToVideo`
- `VideoDepthAnythingProcess`
- `ControlNextGetPoses`
- `Canny`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `easy anythingIndexSwitch`
- `PreviewImage`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`ModelSamplingSD3`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`LoadImage`、`UNETLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`ImageResizeKJ`、`ImageResizeKJv2`、`MathExpression|pysssss`、`LoadVideoDepthAnythingModel`、`CreateVideo`、`SaveVideo`、`Wan22FunControlToVideo`、`VideoDepthAnythingProcess`、`ControlNextGetPoses`、`Canny`、`VHS_LoadVideo`、`easy anythingIndexSwitch`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LoadVideoDepthAnythingModel
