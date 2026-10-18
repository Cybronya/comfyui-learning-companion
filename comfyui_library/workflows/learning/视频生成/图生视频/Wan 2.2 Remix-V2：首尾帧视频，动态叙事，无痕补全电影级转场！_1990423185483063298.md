---
key: 视频生成/图生视频/Wan 2.2 Remix-V2：首尾帧视频，动态叙事，无痕补全电影级转场！_1990423185483063298.json
name: Wan 2.2 Remix-V2：首尾帧视频，动态叙事，无痕补全电影级转场！_1990423185483063298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.2 Remix-V2：首尾帧视频，动态叙事，无痕补全电影级转场！_1990423185483063298.json
hash: 20c271f6119ba3e3
coverage: 0.803279
learned_at: 2026-10-15 22:33:10
nodes: [Note, Note, VAELoader, PreviewImage, Note, Note, Note, Seed (rgthree), Note, Note, easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, SaveImage, RIFE VFI, MathExpression|pysssss, ImageScaleBy, VHS_VideoCombine, VHS_VideoCombine, Text Concatenate, Wan22PromptSelector, JWInteger, ModelSamplingSD3, ModelSamplingSD3, PrimitiveStringMultiline, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, RH_LLMAPI_NODE, ImpactSwitch, CLIPTextEncode, CLIPTextEncode, ShowText, MathExpression|pysssss, JWInteger, MathExpression|pysssss, easy showAnything, Label (rgthree), WanFirstLastFrameToVideo, CLIPVisionLoader, CLIPVisionEncode, JWInteger, Note, CLIPVisionEncode, RH_LLMAPI_NODE, JWInteger, ImageResizeKJv2, ImageResizeKJv2, PathchSageAttentionKJ, wanBlockSwap, PathchSageAttentionKJ, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, UNETLoader, UNETLoader, LoadImage, LoadImage, JWInteger, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan 2.2 Remix-V2：首尾帧视频，动态叙事，无痕补全电影级转场！_1990423185483063298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990423185483063298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `Note`
- `Note`
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
- `MathExpression|pysssss`
- `JWInteger`
- `MathExpression|pysssss`
- `easy showAnything`
- `Label (rgthree)`
- `WanFirstLastFrameToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `JWInteger`
- `Note`
- `CLIPVisionEncode`
- `RH_LLMAPI_NODE`
- `JWInteger`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `CLIPLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（49/61）

**有卡**：`VAELoader`、`Seed (rgthree)`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`ImageScaleBy`、`SaveImage`、`RIFE VFI`、`MathExpression|pysssss`、`VHS_VideoCombine`、`Text Concatenate`、`Wan22PromptSelector`、`JWInteger`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`ShowText`、`Label (rgthree)`、`WanFirstLastFrameToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJv2`、`PathchSageAttentionKJ`、`wanBlockSwap`、`ModelPatchTorchSettings`、`UNETLoader`、`LoadImage`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
