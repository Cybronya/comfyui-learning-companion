---
key: 视频生成/文生视频/Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721.json
name: Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721.json
hash: 129382f4494150fd
coverage: 0.446429
learned_at: 2026-10-11 20:38:32
nodes: [CLIPLoader, VAELoader, LoadImage, BasicScheduler, SplitSigmas, KSamplerSelect, LoadImage, SetNode, VHS_LoadVideo, SetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, GetNode, SamplerCustom, GetNode, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Seed (rgthree), ModelSamplingSD3, SetNode, SetNode, SetNode, SetNode, SimpleMath+, UNETLoader, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, Int, LoadImage, SamplerCustom, RH_LLMAPI_Pro_Node, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), PreviewAny, Label (rgthree), GetNode, UNETLoader, BerniniStudio, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SimpleMath+, Seed (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721.json`

## 结构

**生成流程**：Model → Sampling → Decode → Other

**节点**（56 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `BasicScheduler`
- `SplitSigmas`
- `KSamplerSelect` ★核心
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Seed (rgthree)`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `LoadImage`
- `SamplerCustom` ★核心
- `RH_LLMAPI_Pro_Node`
- `INTConstant`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `Label (rgthree)`
- `GetNode`
- `UNETLoader` ★核心
- `BerniniStudio`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 知识

覆盖率 **45%**（25/56）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`BasicScheduler`、`SplitSigmas`、`KSamplerSelect`、`VHS_LoadVideo`、`VAEDecode`、`ModelSamplingSD3`、`SamplerCustom`、`UNETLoader`、`VHS_VideoCombine`、`Int`、`RH_LLMAPI_Pro_Node`、`INTConstant`、`BerniniStudio`、`LoraLoaderModelOnly`

**缺卡**（6）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`SimpleMath+`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
