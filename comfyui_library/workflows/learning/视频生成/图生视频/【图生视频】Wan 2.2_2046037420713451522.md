---
key: 视频生成/图生视频/【图生视频】Wan 2.2_2046037420713451522.json
name: 【图生视频】Wan 2.2_2046037420713451522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046037420713451522.json
hash: a671a23930fdbb2a
coverage: 0.77193
learned_at: 2026-10-15 22:36:54
nodes: [easy cleanGpuUsed, ImageScaleBy, RIFE VFI, MathExpression|pysssss, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, MathExpression|pysssss, JWInteger, LoadImage, PreviewImage, Note, wanBlockSwap, Note, UNETLoader, ModelSamplingSD3, UNETLoader, wanBlockSwap, ModelSamplingSD3, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPLoader, VAELoader, CLIPVisionEncode, CLIPVisionLoader, easy cleanGpuUsed, VAEDecode, Pick From Batch (mtb), VHS_VideoCombine, CLIPTextEncode, ShowText, RH_LLMAPI_NODE, Note, SaveImage, Note, Note, ImageScaleBy, Note, MathExpression|pysssss, CLIPTextEncode, WanImageToVideo, Seed (rgthree), JWInteger, RH_LLMAPI_NODE, Text Concatenate, Wan22PromptSelector, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, ImpactSwitch, Note, Note, PreviewImage, JWInteger, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/【图生视频】Wan 2.2_2046037420713451522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046037420713451522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `RIFE VFI`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MathExpression|pysssss`
- `JWInteger`
- `LoadImage`
- `PreviewImage`
- `Note`
- `wanBlockSwap`
- `Note`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Pick From Batch (mtb)`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ShowText`
- `RH_LLMAPI_NODE`
- `Note`
- `SaveImage`
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `Seed (rgthree)`
- `JWInteger`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `Wan22PromptSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `ImpactSwitch`
- `Note`
- `Note`
- `PreviewImage`
- `JWInteger`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（44/57）

**有卡**：`easy cleanGpuUsed`、`ImageScaleBy`、`RIFE VFI`、`MathExpression|pysssss`、`VHS_VideoCombine`、`KSamplerAdvanced`、`JWInteger`、`LoadImage`、`wanBlockSwap`、`UNETLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAEDecode`、`Pick From Batch (mtb)`、`CLIPTextEncode`、`ShowText`、`RH_LLMAPI_NODE`、`SaveImage`、`WanImageToVideo`、`Seed (rgthree)`、`Text Concatenate`、`Wan22PromptSelector`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
