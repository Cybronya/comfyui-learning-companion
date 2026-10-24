---
name: unknown_workflow_video_lora_sampler_230
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.946556
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, GetImageRangeFromBatch, ImageResizeKJv2, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int, easy mathInt]
problems: []
missing: []
members: [视频生成/文生视频/SCAIL-2 Dual Character Motion Drive_2072998835728982016.json, 视频生成/文生视频/SCAIL-2 Dual Character Swap_2072998837813551104.json, 视频生成/文生视频/SCAIL-2 Dual-Reference Long Video Edit_2072998856960548864.json, 视频生成/文生视频/SCAIL-2 Single Character Long Video Drive_2072998857560334336.json, 视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998838488834048.json, 视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998839138951168.json, 视频生成/文生视频/SCAIL-2 Single-Reference Long Video Edit_2072998856218157056.json, 视频生成/文生视频/SCAIL-2 Triple Character Motion Drive_2072998837192794112.json, 视频生成/文生视频/SCAIL-2 双人生物长视频驱动_2064973862177173505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_230

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/SCAIL-2 Dual Character Motion Drive_2072998835728982016.json、视频生成/文生视频/SCAIL-2 Dual Character Swap_2072998837813551104.json、视频生成/文生视频/SCAIL-2 Dual-Reference Long Video Edit_2072998856960548864.json、视频生成/文生视频/SCAIL-2 Single Character Long Video Drive_2072998857560334336.json、视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998838488834048.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 4/9 个有
- `ImageCompositeMasked` —— 4/9 个有
- `SAM3_TrackToMask` —— 4/9 个有
- `CLIPLoaderGGUF` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
