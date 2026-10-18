---
key: 视频生成/图生视频/wan2.2图生视频稳定快捷版_1963149133328658434.json
name: wan2.2图生视频稳定快捷版_1963149133328658434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频稳定快捷版_1963149133328658434.json
hash: ebe471d2443b4964
coverage: 0.896552
learned_at: 2026-10-15 22:31:32
nodes: [VAEDecode, CLIPTextEncode, PathchSageAttentionKJ, CLIPTextEncode, WanImageToVideo, Bjornulf_ShowInt, ShowText|pysssss, CreateVideo, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, KSamplerAdvanced, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, ModelSamplingSD3, CFGZeroStar, PreviewImage, VAELoader, CLIPLoader, UNETLoader, UNETLoader, INTConstant, INTConstant, PrimitiveFloat, SaveVideo, RH_LLMAPI_NODE, KSamplerAdvanced, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频稳定快捷版_1963149133328658434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963149133328658434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `Bjornulf_ShowInt`
- `ShowText|pysssss`
- `CreateVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `CFGZeroStar`
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `SaveVideo`
- `RH_LLMAPI_NODE`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`WanImageToVideo`、`Bjornulf_ShowInt`、`CreateVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`KSamplerAdvanced`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`CFGZeroStar`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`SaveVideo`、`RH_LLMAPI_NODE`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
