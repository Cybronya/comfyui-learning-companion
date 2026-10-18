---
key: 视频生成/图生视频/【图生视频】Smooth Mix Wan 2.2_1979752163389902850.json
name: 【图生视频】Smooth Mix Wan 2.2_1979752163389902850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【图生视频】Smooth Mix Wan 2.2_1979752163389902850.json
hash: 854caf871062ec4c
coverage: 0.762712
learned_at: 2026-10-15 22:32:25
nodes: [Note, Note, CLIPLoader, VAELoader, PreviewImage, Note, Note, Note, Seed (rgthree), Note, Note, Note, easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, SaveImage, RIFE VFI, MathExpression|pysssss, Label (rgthree), ImageScaleBy, VHS_VideoCombine, VHS_VideoCombine, CLIPVisionLoader, Text Concatenate, Wan22PromptSelector, JWInteger, ModelSamplingSD3, ModelSamplingSD3, Note, PrimitiveStringMultiline, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, RH_LLMAPI_NODE, WanImageToVideo, ImpactSwitch, CLIPTextEncode, CLIPTextEncode, ShowText, PathchSageAttentionKJ, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, wanBlockSwap, UNETLoader, UNETLoader, JWInteger, MathExpression|pysssss, JWInteger, MathExpression|pysssss, easy showAnything, RH_LLMAPI_NODE, Label (rgthree), PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/【图生视频】Smooth Mix Wan 2.2_1979752163389902850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979752163389902850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `Note`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `Seed (rgthree)`
- `Note`
- `Note`
- `Note`
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `SaveImage`
- `RIFE VFI`
- `MathExpression|pysssss`
- `Label (rgthree)`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `Text Concatenate`
- `Wan22PromptSelector`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `PrimitiveStringMultiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `RH_LLMAPI_NODE`
- `WanImageToVideo`
- `ImpactSwitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `JWInteger`
- `MathExpression|pysssss`
- `JWInteger`
- `MathExpression|pysssss`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `Label (rgthree)`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（45/59）

**有卡**：`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`ImageScaleBy`、`SaveImage`、`RIFE VFI`、`MathExpression|pysssss`、`Label (rgthree)`、`VHS_VideoCombine`、`CLIPVisionLoader`、`Text Concatenate`、`Wan22PromptSelector`、`JWInteger`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`KSamplerAdvanced`、`VAEDecode`、`RH_LLMAPI_NODE`、`WanImageToVideo`、`CLIPTextEncode`、`ShowText`、`PathchSageAttentionKJ`、`wanBlockSwap`、`ModelPatchTorchSettings`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
