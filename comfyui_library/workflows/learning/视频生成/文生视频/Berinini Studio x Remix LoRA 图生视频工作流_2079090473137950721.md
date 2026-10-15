---
key: 视频生成/文生视频/Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721.json
name: Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721.json
hash: 129382f4494150fd
coverage: 0.553571
learned_at: 2026-10-15 22:44:03
nodes: [CLIPLoader, VAELoader, LoadImage, BasicScheduler, SplitSigmas, KSamplerSelect, LoadImage, SetNode, VHS_LoadVideo, SetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, GetNode, SamplerCustom, GetNode, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Seed (rgthree), ModelSamplingSD3, SetNode, SetNode, SetNode, SetNode, SimpleMath+, UNETLoader, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, Int, LoadImage, SamplerCustom, RH_LLMAPI_Pro_Node, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), PreviewAny, Label (rgthree), GetNode, UNETLoader, BerniniStudio, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
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

覆盖率 **55%**（31/56）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`BasicScheduler`、`SplitSigmas`、`KSamplerSelect`、`VHS_LoadVideo`、`VAEDecode`、`ModelSamplingSD3`、`SamplerCustom`、`Label (rgthree)`、`Seed (rgthree)`、`SimpleMath+`、`UNETLoader`、`VHS_VideoCombine`、`Int`、`RH_LLMAPI_Pro_Node`、`INTConstant`、`BerniniStudio`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
