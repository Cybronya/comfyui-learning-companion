---
key: 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_1979696533400621058.json
name: Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_1979696533400621058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_1979696533400621058.json
hash: 81776864c4ff185c
coverage: 0.578947
learned_at: 2026-10-10 23:05:42
nodes: [Note, Note, CLIPLoader, VAELoader, CLIPTextEncode, PreviewImage, Note, Note, WanImageToVideo, ModelSamplingSD3, Note, ModelSamplingSD3, Seed (rgthree), Note, Note, Note, VAEDecode, easy cleanGpuUsed, Pick From Batch (mtb), easy cleanGpuUsed, ImageScaleBy, SaveImage, RIFE VFI, JWInteger, JWInteger, CLIPTextEncode, MathExpression|pysssss, RH_LLMAPI_NODE, ImpactSwitch, Label (rgthree), Label (rgthree), RH_LLMAPI_NODE, Text Concatenate, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, ImageScaleBy, MathExpression|pysssss, JWInteger, LogicGateNegateValue, LogicGateNegateValue, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, Wan22PromptSelector, PrimitiveStringMultiline, JWInteger, JWInteger, Note, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, wanBlockSwap]
patterns: []
missing: [Label (rgthree), Label (rgthree), MathExpression|pysssss, MathExpression|pysssss, Pick From Batch (mtb), RIFE VFI, Text Concatenate, easy cleanGpuUsed, easy cleanGpuUsed, Seed (rgthree)]
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_1979696533400621058.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_1979696533400621058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
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
- `Label (rgthree)`
- `Label (rgthree)`
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
- `VHS_VideoCombine`
- `easy showAnything`
- `Wan22PromptSelector`
- `PrimitiveStringMultiline`
- `JWInteger`
- `JWInteger`
- `Note`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `wanBlockSwap`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **58%**（33/57）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`VAEDecode`、`ImageScaleBy`、`SaveImage`、`JWInteger`、`RH_LLMAPI_NODE`、`KSamplerAdvanced`、`UNETLoader`、`LogicGateNegateValue`、`VHS_VideoCombine`、`Wan22PromptSelector`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`

**缺卡**（10）：`Label (rgthree)`、`Label (rgthree)`、`MathExpression|pysssss`、`MathExpression|pysssss`、`Pick From Batch (mtb)`、`RIFE VFI`、`Text Concatenate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Wan22PromptSelector、SaveImage

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
