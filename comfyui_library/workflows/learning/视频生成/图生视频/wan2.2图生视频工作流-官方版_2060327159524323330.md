---
key: 视频生成/图生视频/wan2.2图生视频工作流-官方版_2060327159524323330.json
name: wan2.2图生视频工作流-官方版_2060327159524323330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频工作流-官方版_2060327159524323330.json
hash: 4cda5718fd24b876
coverage: 0.552632
learned_at: 2026-10-15 22:38:47
nodes: [ModelSamplingSD3, PrimitiveInt, PrimitiveInt, PrimitiveFloat, KSamplerAdvanced, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ModelSamplingSD3, ComfySwitchNode, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveFloat, PrimitiveStringMultiline, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, ComfySwitchNode, VAEDecode, UNETLoader, UNETLoader, CLIPLoader, ComfyMathExpression, WanImageToVideo, GetImageSize, ResizeImagesByLongerEdge, PrimitiveInt, PrimitiveFloat, PrimitiveBoolean, PrimitiveInt, CreateVideo, SetNode, GetNode, SaveVideo, LoadImage, PrimitiveStringMultiline, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频工作流-官方版_2060327159524323330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060327159524323330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `ModelSamplingSD3`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `KSamplerAdvanced` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ModelSamplingSD3`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ComfyMathExpression`
- `WanImageToVideo`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `CreateVideo`
- `SetNode`
- `GetNode`
- `SaveVideo`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAELoader`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **55%**（21/38）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`ComfyMathExpression`、`WanImageToVideo`、`GetImageSize`、`ResizeImagesByLongerEdge`、`PrimitiveBoolean`、`CreateVideo`、`SaveVideo`、`LoadImage`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
