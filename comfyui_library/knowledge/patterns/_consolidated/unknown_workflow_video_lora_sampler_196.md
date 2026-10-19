---
name: unknown_workflow_video_lora_sampler_196
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.3893
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, GetImageRangeFromBatch, GetNode, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2065365595184521217.json, 视频生成/图生视频/2065680641039093761.json, 视频生成/图生视频/2064969130989670401.json, 视频生成/图生视频/2066352425379909633.json, 视频生成/图生视频/2064637391054397441.json, 视频生成/图生视频/2064981162845622273.json, 视频生成/图生视频/2064994418565931010.json, 视频生成/图生视频/2064998971084468225.json, 视频生成/图生视频/2066063514803986434.json, 视频生成/图生视频/2065765401602125825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_196

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2065365595184521217.json、视频生成/图生视频/2065680641039093761.json、视频生成/图生视频/2064969130989670401.json、视频生成/图生视频/2066352425379909633.json、视频生成/图生视频/2064637391054397441.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：39%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 9/10 个有
- `GetImageSize` —— 6/10 个有
- `ImageFromBatch` —— 6/10 个有
- `PrimitiveBoolean` —— 4/10 个有
- `WanChunkFeedForward` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `INTConstant` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `VHS_VideoInfoLoaded` —— 2/10 个有
- `ApplySageAttention` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `Pick From Batch (mtb)` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `RH_RhartImageG2ImageToImage` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `UNETLoader` —— 1/10 个有
- `easy forLoopEnd` —— 1/10 个有
- `easy forLoopStart` —— 1/10 个有
- `easy imageRemBg` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
