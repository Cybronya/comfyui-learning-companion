---
key: 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874.json
name: Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874.json
hash: 98000717c4e7aa95
coverage: 0.647059
learned_at: 2026-10-11 03:07:12
nodes: [VAELoader, Note, ModelSamplingSD3, Note, ModelSamplingSD3, JWInteger, JWInteger, MathExpression|pysssss, RH_LLMAPI_NODE, ImpactSwitch, RH_LLMAPI_NODE, Text Concatenate, UNETLoader, UNETLoader, MathExpression|pysssss, VHS_VideoCombine, VHS_VideoCombine, wanBlockSwap, Note, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPLoader, Note, CLIPTextEncode, LogicGateNegateValue, LogicGateNegateValue, ImageScaleBy, easy showAnything, easy cleanGpuUsed, ImageScaleBy, JWInteger, JWInteger, RIFE VFI, VAEDecode, Pick From Batch (mtb), CLIPTextEncode, WanImageToVideo, Seed (rgthree), KSamplerAdvanced, easy cleanGpuUsed, PrimitiveStringMultiline, KSamplerAdvanced, PreviewImage, SaveImage, Wan22PromptSelector, easy showAnything, JWInteger, Note]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, Pick From Batch (mtb), RIFE VFI, Text Concatenate, easy cleanGpuUsed, easy cleanGpuUsed, Seed (rgthree)]
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **65%**（33/51）

**有卡**：`VAELoader`、`ModelSamplingSD3`、`JWInteger`、`RH_LLMAPI_NODE`、`UNETLoader`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`CLIPTextEncode`、`LogicGateNegateValue`、`ImageScaleBy`、`VAEDecode`、`WanImageToVideo`、`KSamplerAdvanced`、`SaveImage`、`Wan22PromptSelector`

**缺卡**（8）：`MathExpression|pysssss`、`MathExpression|pysssss`、`Pick From Batch (mtb)`、`RIFE VFI`、`Text Concatenate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Wan22PromptSelector、SaveImage

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
