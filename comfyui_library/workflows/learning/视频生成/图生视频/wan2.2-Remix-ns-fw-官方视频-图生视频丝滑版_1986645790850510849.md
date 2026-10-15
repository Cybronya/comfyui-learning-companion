---
key: 视频生成/图生视频/wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849.json
name: wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849.json
hash: 72940ab158a8ed85
coverage: 0.651515
learned_at: 2026-10-15 22:42:59
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, SetNode, PathchSageAttentionKJ, GetNode, SetNode, PathchSageAttentionKJ, GetImageSizeAndCount, PreviewImage, ImageFromBatch, VAEDecodeTiled, ImpactFloat, PreviewImage, INTConstant, Reroute, WanVideoVACEStartToEndFrame, SetNode, easy seed, CLIPLoader, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAELoader, WanImageToVideo, GetNode, ShowText|pysssss, GetImageSizeAndCount, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, easy int, GetImageSizeAndCount, easy int, ImageFromBatch+, StringFunction|pysssss, StringFunction|pysssss, GetNode, GetNode, easy showAnything, VHS_VideoCombine, UNETLoader, UNETLoader, easy anythingIndexSwitch, easy int, WanMoeKSampler, Qwen3_VQA, CLIPVisionLoader, GetImageSizeAndCount, CLIPVisionEncode, easy positive, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, SaveImage, SaveLatent, GetImageSizeAndCount, GetNode, LoadImage, easy positive, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "euler", "sampler_name": 1.5, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
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

覆盖率 **65%**（43/66）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`ImageFromBatch`、`VAEDecodeTiled`、`ImpactFloat`、`INTConstant`、`WanVideoVACEStartToEndFrame`、`easy seed`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`ImageFromBatch+`、`StringFunction|pysssss`、`VHS_VideoCombine`、`UNETLoader`、`easy anythingIndexSwitch`、`WanMoeKSampler`、`Qwen3_VQA`、`CLIPVisionLoader`、`CLIPVisionEncode`、`easy positive`、`SaveImage`、`SaveLatent`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、easy seed、SaveLatent
