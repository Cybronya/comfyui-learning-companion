---
key: 视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧_1989386607084138498.json
name: Smooth Mix Wan 2.2：首尾帧_1989386607084138498.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1989386607084138498.json
hash: df2acf1bd4e3fb33
coverage: 0.8
learned_at: 2026-10-15 22:33:06
nodes: [Note, Note, CLIPLoader, VAELoader, PreviewImage, Note, Note, Note, Seed (rgthree), Note, Note, easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, SaveImage, RIFE VFI, MathExpression|pysssss, ImageScaleBy, VHS_VideoCombine, Text Concatenate, Wan22PromptSelector, JWInteger, ModelSamplingSD3, ModelSamplingSD3, PrimitiveStringMultiline, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, RH_LLMAPI_NODE, ImpactSwitch, CLIPTextEncode, CLIPTextEncode, ShowText, UNETLoader, UNETLoader, MathExpression|pysssss, JWInteger, MathExpression|pysssss, easy showAnything, WanFirstLastFrameToVideo, CLIPVisionLoader, CLIPVisionEncode, JWInteger, Note, CLIPVisionEncode, RH_LLMAPI_NODE, ImageResizeKJv2, ImageResizeKJv2, PathchSageAttentionKJ, wanBlockSwap, PathchSageAttentionKJ, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, VHS_VideoCombine, LoadImage, JWInteger, LoadImage, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧_1989386607084138498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989386607084138498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
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
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `SaveImage`
- `RIFE VFI`
- `MathExpression|pysssss`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `Text Concatenate`
- `Wan22PromptSelector`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `JWInteger`
- `MathExpression|pysssss`
- `easy showAnything`
- `WanFirstLastFrameToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `JWInteger`
- `Note`
- `CLIPVisionEncode`
- `RH_LLMAPI_NODE`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `LoadImage`
- `JWInteger`
- `LoadImage`
- `JWInteger`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（48/60）

**有卡**：`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`ImageScaleBy`、`SaveImage`、`RIFE VFI`、`MathExpression|pysssss`、`VHS_VideoCombine`、`Text Concatenate`、`Wan22PromptSelector`、`JWInteger`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`ShowText`、`UNETLoader`、`WanFirstLastFrameToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJv2`、`PathchSageAttentionKJ`、`wanBlockSwap`、`ModelPatchTorchSettings`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
