---
key: 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频（流畅如丝，内置补帧）_1984903672830312450.json
name: Smooth Mix Wan 2.2：文生视频（流畅如丝，内置补帧）_1984903672830312450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan 2.2：文生视频（流畅如丝，内置补帧）_1984903672830312450.json
hash: 57b05ce09ca9b64b
coverage: 0.741379
learned_at: 2026-10-15 22:47:00
nodes: [Note, Note, CLIPLoader, VAELoader, CLIPTextEncode, PreviewImage, Note, Note, WanImageToVideo, ModelSamplingSD3, Note, ModelSamplingSD3, Seed (rgthree), Note, Note, Note, VAEDecode, easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, SaveImage, RIFE VFI, JWInteger, JWInteger, CLIPTextEncode, MathExpression|pysssss, RH_LLMAPI_NODE, ImpactSwitch, RH_LLMAPI_NODE, Text Concatenate, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, ImageScaleBy, MathExpression|pysssss, JWInteger, LogicGateNegateValue, LogicGateNegateValue, easy showAnything, VHS_VideoCombine, JWInteger, Note, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, wanBlockSwap, Wan22PromptSelector, PrimitiveStringMultiline, JWInteger, Label (rgthree), VHS_VideoCombine, easy showAnything, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频（流畅如丝，内置补帧）_1984903672830312450.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan 2.2：文生视频（流畅如丝，内置补帧）_1984903672830312450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `Note`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Note`
- `Note`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `Note`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `Note`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `SaveImage`
- `RIFE VFI`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageScaleBy`
- `MathExpression|pysssss`
- `JWInteger`
- `LogicGateNegateValue`
- `LogicGateNegateValue`
- `easy showAnything`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `Wan22PromptSelector`
- `PrimitiveStringMultiline`
- `JWInteger`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `easy showAnything`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（43/58）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`Seed (rgthree)`、`VAEDecode`、`easy cleanGpuUsed`、`Pick From Batch (mtb)`、`ImageScaleBy`、`SaveImage`、`RIFE VFI`、`JWInteger`、`MathExpression|pysssss`、`RH_LLMAPI_NODE`、`Text Concatenate`、`KSamplerAdvanced`、`UNETLoader`、`LogicGateNegateValue`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Wan22PromptSelector`、`Label (rgthree)`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
