---
name: unknown_workflow_video_lora_sampler_990
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4895
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetImageRangeFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/让照片里的人跳任何舞｜SCAIL2骨骼驱动人物替换_2064706601667358721.json, 视频生成/图生视频/超越的闭源角色完美迁移-姿态-表情-声音_2065765401602125825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_990

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/让照片里的人跳任何舞｜SCAIL2骨骼驱动人物替换_2064706601667358721.json、视频生成/图生视频/超越的闭源角色完美迁移-姿态-表情-声音_2065765401602125825.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
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

**可变部分**（部分 workflow 才有）：
- `ApplySageAttention` —— 1/2 个有
- `ColorTransfer` —— 1/2 个有
- `DiffusionModelLoaderKJ` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `Pick From Batch (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
