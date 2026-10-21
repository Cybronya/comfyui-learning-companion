---
name: unknown_workflow_video_lora_sampler_510
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.41325
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetImageRangeFromBatch, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/Scail2动作迁移_for循环（一键模仿）_2089320207121731586.json, 视频生成/图生视频/Scail2多参工作流_2090458654913941506.json, 视频生成/图生视频/Scail2多参工作流_2093511775273705474.json, 视频生成/图生视频/2065014891525795842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_510

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Scail2动作迁移_for循环（一键模仿）_2089320207121731586.json、视频生成/图生视频/Scail2多参工作流_2090458654913941506.json、视频生成/图生视频/Scail2多参工作流_2093511775273705474.json、视频生成/图生视频/2065014891525795842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：41%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `SingleBooleanTrigger` —— 3/4 个有
- `ComfySwitchNode` —— 2/4 个有
- `Float` —— 2/4 个有
- `ImageBatchMultiple+` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `Int` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
