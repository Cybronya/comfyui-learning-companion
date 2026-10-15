---
key: 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874.json
name: Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874.json
hash: 98000717c4e7aa95
coverage: 0.803922
learned_at: 2026-10-15 22:47:01
nodes: [VAELoader, Note, ModelSamplingSD3, Note, ModelSamplingSD3, JWInteger, JWInteger, MathExpression|pysssss, RH_LLMAPI_NODE, ImpactSwitch, RH_LLMAPI_NODE, Text Concatenate, UNETLoader, UNETLoader, MathExpression|pysssss, VHS_VideoCombine, VHS_VideoCombine, wanBlockSwap, Note, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPLoader, Note, CLIPTextEncode, LogicGateNegateValue, LogicGateNegateValue, ImageScaleBy, easy showAnything, easy cleanGpuUsed, ImageScaleBy, JWInteger, JWInteger, RIFE VFI, VAEDecode, Pick From Batch (mtb), CLIPTextEncode, WanImageToVideo, Seed (rgthree), KSamplerAdvanced, easy cleanGpuUsed, PrimitiveStringMultiline, KSamplerAdvanced, PreviewImage, SaveImage, Wan22PromptSelector, easy showAnything, JWInteger, Note]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `VAELoader`
- `Note`
- `ModelSamplingSD3`
- `Note`
- `ModelSamplingSD3`
- `JWInteger`
- `JWInteger`
- `MathExpression|pysssss`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `Note`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `Note`
- `CLIPTextEncode` ★核心
- `LogicGateNegateValue`
- `LogicGateNegateValue`
- `ImageScaleBy`
- `easy showAnything`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `JWInteger`
- `JWInteger`
- `RIFE VFI`
- `VAEDecode` ★核心
- `Pick From Batch (mtb)`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `SaveImage`
- `Wan22PromptSelector`
- `easy showAnything`
- `JWInteger`
- `Note`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（41/51）

**有卡**：`VAELoader`、`ModelSamplingSD3`、`JWInteger`、`MathExpression|pysssss`、`RH_LLMAPI_NODE`、`Text Concatenate`、`UNETLoader`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`CLIPTextEncode`、`LogicGateNegateValue`、`ImageScaleBy`、`easy cleanGpuUsed`、`RIFE VFI`、`VAEDecode`、`Pick From Batch (mtb)`、`WanImageToVideo`、`Seed (rgthree)`、`KSamplerAdvanced`、`SaveImage`、`Wan22PromptSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、Wan22PromptSelector
