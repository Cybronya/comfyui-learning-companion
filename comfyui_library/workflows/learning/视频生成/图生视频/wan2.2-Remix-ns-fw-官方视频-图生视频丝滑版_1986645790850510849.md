---
key: 视频生成/图生视频/wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849.json
name: wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849.json
hash: 72940ab158a8ed85
coverage: 0.469697
learned_at: 2026-10-13 00:04:36
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, SetNode, PathchSageAttentionKJ, GetNode, SetNode, PathchSageAttentionKJ, GetImageSizeAndCount, PreviewImage, ImageFromBatch, VAEDecodeTiled, ImpactFloat, PreviewImage, INTConstant, Reroute, WanVideoVACEStartToEndFrame, SetNode, easy seed, CLIPLoader, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAELoader, WanImageToVideo, GetNode, ShowText|pysssss, GetImageSizeAndCount, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, easy int, GetImageSizeAndCount, easy int, ImageFromBatch+, StringFunction|pysssss, StringFunction|pysssss, GetNode, GetNode, easy showAnything, VHS_VideoCombine, UNETLoader, UNETLoader, easy anythingIndexSwitch, easy int, WanMoeKSampler, Qwen3_VQA, CLIPVisionLoader, GetImageSizeAndCount, CLIPVisionEncode, easy positive, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, SaveImage, SaveLatent, GetImageSizeAndCount, GetNode, LoadImage, easy positive, VHS_VideoCombine]
patterns: []
missing: [ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, StringFunction|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, easy int, easy int, easy positive, easy positive, easy imageSize, easy seed]
parameters: {"cfg": 20, "denoise": "euler", "sampler_name": 1.5, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/图生视频/wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageFromBatch`
- `VAEDecodeTiled` ★核心
- `ImpactFloat`
- `PreviewImage`
- `INTConstant`
- `Reroute`
- `WanVideoVACEStartToEndFrame`
- `SetNode`
- `easy seed`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `WanImageToVideo`
- `GetNode`
- `ShowText|pysssss`
- `GetImageSizeAndCount`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `easy int`
- `GetImageSizeAndCount`
- `easy int`
- `ImageFromBatch+`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy anythingIndexSwitch`
- `easy int`
- `WanMoeKSampler` ★核心
- `Qwen3_VQA`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `CLIPVisionEncode`
- `easy positive`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `SaveImage`
- `SaveLatent`
- `GetImageSizeAndCount`
- `GetNode`
- `LoadImage`
- `easy positive`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1.5`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **47%**（31/66）

**有卡**：`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`ImageFromBatch`、`VAEDecodeTiled`、`ImpactFloat`、`INTConstant`、`WanVideoVACEStartToEndFrame`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`WanImageToVideo`、`VHS_VideoCombine`、`UNETLoader`、`WanMoeKSampler`、`Qwen3_VQA`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SaveImage`、`SaveLatent`、`LoadImage`

**缺卡**（12）：`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`StringFunction|pysssss`、`StringFunction|pysssss`、`easy anythingIndexSwitch`、`easy int`、`easy int`、`easy int`、`easy positive`、`easy positive`、`easy imageSize`、`easy seed`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、SaveLatent、VAEDecodeTiled

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
