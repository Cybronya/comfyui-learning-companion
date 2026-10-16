---
key: 视频生成/图生视频/视频-图生视频加强动态-wan2.2-smoothMix-PainterI2V-官方_1988562888287805442.json
name: 视频-图生视频加强动态-wan2.2-smoothMix-PainterI2V-官方_1988562888287805442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988562888287805442.json
hash: 0edf8cf57ccbb5ab
coverage: 0.641791
learned_at: 2026-10-15 22:33:03
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, SetNode, GetNode, GetNode, SetNode, PathchSageAttentionKJ, PreviewImage, ImageFromBatch, VAEDecodeTiled, GetImageSizeAndCount, PreviewImage, INTConstant, VHS_VideoCombine, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, SetNode, easy seed, CLIPLoader, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAELoader, GetImageSizeAndCount, WanMoeKSampler, GetNode, ShowText|pysssss, GetImageSizeAndCount, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetImageSizeAndCount, GetImageSizeAndCount, ImageFromBatch+, StringFunction|pysssss, StringFunction|pysssss, GetNode, GetNode, easy positive, PainterI2V, VHS_VideoCombine, LoadImage, easy anythingIndexSwitch, easy showAnything, MemoryCleaner, easy cleanGpuUsed, PathchSageAttentionKJ, UNETLoader, UNETLoader, Reroute, ModelBlockSwap, ModelBlockSwap, easy int, ImpactFloat, easy int, PrimitiveFloat, GetImageSizeAndCount, SetNode, MathExpression|pysssss, SetNode, easy positive, Qwen3_VQA]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1.5, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/视频-图生视频加强动态-wan2.2-smoothMix-PainterI2V-官方_1988562888287805442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988562888287805442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `ImageFromBatch`
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `PreviewImage`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
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
- `GetImageSizeAndCount`
- `WanMoeKSampler` ★核心
- `GetNode`
- `ShowText|pysssss`
- `GetImageSizeAndCount`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `GetNode`
- `GetNode`
- `easy positive`
- `PainterI2V`
- `VHS_VideoCombine`
- `LoadImage`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `MemoryCleaner`
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `ModelBlockSwap`
- `ModelBlockSwap`
- `easy int`
- `ImpactFloat`
- `easy int`
- `PrimitiveFloat`
- `GetImageSizeAndCount`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `easy positive`
- `Qwen3_VQA`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1.5`
- `scheduler` = `1`
- `denoise` = `sa_solver`

## 知识

覆盖率 **64%**（43/67）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`ImageFromBatch`、`VAEDecodeTiled`、`INTConstant`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`、`easy seed`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`WanMoeKSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`StringFunction|pysssss`、`easy positive`、`PainterI2V`、`LoadImage`、`easy anythingIndexSwitch`、`MemoryCleaner`、`easy cleanGpuUsed`、`UNETLoader`、`ModelBlockSwap`、`easy int`、`ImpactFloat`、`MathExpression|pysssss`、`Qwen3_VQA`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、easy seed、VAEDecodeTiled
