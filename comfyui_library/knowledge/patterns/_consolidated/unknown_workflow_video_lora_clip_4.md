---
name: unknown_workflow_video_lora_clip_4
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.542214
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DiffusionModelLoaderKJ, GetNode, ImageResizeKJv2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanChunkFeedForward]
problems: []
missing: []
members: [视频生成/图生视频/2065073781403643906.json, 视频生成/图生视频/2068015030934786049.json, 视频生成/图生视频/2067983408994807810.json, 视频生成/图生视频/2065050887139188738.json, 视频生成/图生视频/2067976240774074369.json, 视频生成/图生视频/2068006607816060929.json, 视频生成/图生视频/2069809845880049665.json, 视频生成/图生视频/2068608241436815362.json, 视频生成/图生视频/2068592068020228097.json, 视频生成/图生视频/Scail2人物替换工作流_2102813959735832577.json, 视频生成/图生视频/Scail2人物替换工作流_2106538167158530050.json, 视频生成/图生视频/2068613671097552898.json, 视频生成/图生视频/2064423977212272642.json, 视频生成/图生视频/2068394809362051074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2065073781403643906.json、视频生成/图生视频/2068015030934786049.json、视频生成/图生视频/2067983408994807810.json、视频生成/图生视频/2065050887139188738.json、视频生成/图生视频/2067976240774074369.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SetNode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanChunkFeedForward`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 12/14 个有
- `BatchImagesNode` —— 12/14 个有
- `CheckpointLoaderSimple` —— 11/14 个有
- `KSamplerSelect` —— 11/14 个有
- `SAM3_VideoTrack` —— 11/14 个有
- `SCAIL2ColoredMask` —— 11/14 个有
- `SamplerCustom` —— 11/14 个有
- `WanSCAILToVideo` —— 11/14 个有
- `PreviewImage` —— 10/14 个有
- `VAEDecode` —— 10/14 个有
- `INTConstant` —— 7/14 个有
- `ImageConcatMulti` —— 7/14 个有
- `ColorTransfer` —— 6/14 个有
- `GetImageRangeFromBatch` —— 6/14 个有
- `VideoInfoLoaded` —— 6/14 个有
- `WanContextWindowsManual` —— 4/14 个有
- `RMBG` —— 3/14 个有
- `SaveVideoNode` —— 3/14 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/14 个有
- `GIMMVFI_interpolate` —— 2/14 个有
- `LayerMask: RemBgUltra` —— 2/14 个有
- `SAM3_Detect` —— 2/14 个有
- `VAEDecodeTiled` —— 2/14 个有
- `WanSCAILInfinity` —— 2/14 个有
- `WanSCAILMultirefInfinity` —— 2/14 个有
- `WanVideoMemoryEfficientSageAttentionPatch` —— 2/14 个有
- `easy imageRemBg` —— 2/14 个有
- `CR Text` —— 1/14 个有
- `ComfySwitchNode` —— 1/14 个有
- `EmptyImage` —— 1/14 个有
- `GetImageSizeAndCount` —— 1/14 个有
- `Int` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
