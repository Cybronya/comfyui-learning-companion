---
key: 视频生成/文生视频/wan2.2-14B-rapid 文生视频-最新加速模型_1998656401134247938.json
name: wan2.2-14B-rapid 文生视频-最新加速模型_1998656401134247938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-14B-rapid 文生视频-最新加速模型_1998656401134247938.json
hash: f7e032441d587aa0
coverage: 0.607143
learned_at: 2026-10-11 02:57:39
nodes: [CLIPTextEncode, easy cleanGpuUsed, easy showAnything, RH_Prompter, CLIPTextEncode, easy imageSize, TextBox, Wan_video_prompt_generator, easy showAnything, UNETLoader, ModelSamplingSD3, CLIPLoader, VAEDecode, LayerUtility: PurgeVRAM, VAELoader, EmptyImage, Int, SimpleMath+, SimpleMath+, Int, SimpleMath+, EmptyHunyuanLatentVideo, SimpleMath+, SimpleMath+, CR Text Replace, TextBox, KSampler, VHS_VideoCombine]
patterns: []
missing: [CR Text Replace, LayerUtility: PurgeVRAM, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy imageSize]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 239534204625140, "steps": 4}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2-14B-rapid 文生视频-最新加速模型_1998656401134247938.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-14B-rapid 文生视频-最新加速模型_1998656401134247938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy showAnything`
- `RH_Prompter`
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `TextBox`
- `Wan_video_prompt_generator`
- `easy showAnything`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAELoader`
- `EmptyImage`
- `Int`
- `SimpleMath+`
- `SimpleMath+`
- `Int`
- `SimpleMath+`
- `EmptyHunyuanLatentVideo`
- `SimpleMath+`
- `SimpleMath+`
- `CR Text Replace`
- `TextBox`
- `KSampler` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `239534204625140`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **61%**（17/28）

**有卡**：`CLIPTextEncode`、`RH_Prompter`、`TextBox`、`Wan_video_prompt_generator`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`EmptyImage`、`Int`、`EmptyHunyuanLatentVideo`、`KSampler`、`VHS_VideoCombine`

**缺卡**（9）：`CR Text Replace`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、RH_Prompter

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
