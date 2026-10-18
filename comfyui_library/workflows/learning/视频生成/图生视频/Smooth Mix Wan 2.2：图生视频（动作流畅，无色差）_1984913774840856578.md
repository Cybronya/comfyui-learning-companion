---
key: 视频生成/图生视频/Smooth Mix Wan 2.2：图生视频（动作流畅，无色差）_1984913774840856578.json
name: Smooth Mix Wan 2.2：图生视频（动作流畅，无色差）_1984913774840856578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Smooth Mix Wan 2.2：图生视频（动作流畅，无色差）_1984913774840856578.json
hash: 17669af8b9dd6a17
coverage: 0.762712
learned_at: 2026-10-15 22:32:50
nodes: [Note, Note, CLIPLoader, VAELoader, PreviewImage, Note, Note, Note, Seed (rgthree), Note, Note, Note, easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, SaveImage, RIFE VFI, MathExpression|pysssss, ImageScaleBy, VHS_VideoCombine, VHS_VideoCombine, CLIPVisionLoader, Text Concatenate, JWInteger, ModelSamplingSD3, ModelSamplingSD3, Note, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, RH_LLMAPI_NODE, WanImageToVideo, ImpactSwitch, CLIPTextEncode, CLIPTextEncode, ShowText, UNETLoader, UNETLoader, JWInteger, MathExpression|pysssss, JWInteger, MathExpression|pysssss, easy showAnything, RH_LLMAPI_NODE, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, wanBlockSwap, wanBlockSwap, LoadImage, Wan22PromptSelector, Label (rgthree), PrimitiveStringMultiline, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Smooth Mix Wan 2.2：图生视频（动作流畅，无色差）_1984913774840856578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984913774840856578.json`

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
- `ImageScaleBy`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `Text Concatenate`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
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
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `JWInteger`
- `MathExpression|pysssss`
- `JWInteger`
- `MathExpression|pysssss`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `wanBlockSwap`
- `LoadImage`
- `Wan22PromptSelector`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `MarkdownNote`
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

**有卡**：`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`ImageScaleBy`、`SaveImage`、`RIFE VFI`、`MathExpression|pysssss`、`VHS_VideoCombine`、`CLIPVisionLoader`、`Text Concatenate`、`JWInteger`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`KSamplerAdvanced`、`VAEDecode`、`RH_LLMAPI_NODE`、`WanImageToVideo`、`CLIPTextEncode`、`ShowText`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`wanBlockSwap`、`LoadImage`、`Wan22PromptSelector`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
