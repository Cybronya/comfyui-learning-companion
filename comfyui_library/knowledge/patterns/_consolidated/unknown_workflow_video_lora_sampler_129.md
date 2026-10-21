---
name: unknown_workflow_video_lora_sampler_129
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.631615
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1996042760450981890.json, 视频生成/图生视频/2069666439010807809.json, 视频生成/图生视频/1996065856805355521.json, 视频生成/图生视频/2051153118703955970.json, 视频生成/图生视频/2049307460728524802.json, 视频生成/图生视频/2049678404324208642.json, 视频生成/图生视频/1995844904171495425.json, 视频生成/图生视频/2061068385760399361.json, 视频生成/图生视频/2062090699058798593.json, 视频生成/图生视频/2068716358623391746.json, 视频生成/图生视频/2009099537780056065.json, 视频生成/图生视频/1999779350897717249.json, 视频生成/图生视频/1995725668220538882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_129

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1996042760450981890.json、视频生成/图生视频/2069666439010807809.json、视频生成/图生视频/1996065856805355521.json、视频生成/图生视频/2051153118703955970.json、视频生成/图生视频/2049307460728524802.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoScheduler` —— 12/13 个有
- `Int` —— 11/13 个有
- `WanVideoBlockSwap` —— 11/13 个有
- `WanVideoSetLoRAs` —— 11/13 个有
- `DrawViTPose` —— 9/13 个有
- `PoseAndFaceDetection` —— 9/13 个有
- `WanVideoSetBlockSwap` —— 9/13 个有
- `WanVideoTorchCompileSettings` —— 8/13 个有
- `SimpleMath+` —— 7/13 个有
- `PoseDetectionOneToAllAnimation` —— 6/13 个有
- `Anything Everywhere` —— 5/13 个有
- `CR Text` —— 5/13 个有
- `ImageUpscaleWithModelBatched` —— 5/13 个有
- `RIFE VFI` —— 5/13 个有
- `RunningHub Deepcleaner` —— 5/13 个有
- `UpscaleModelLoader` —— 5/13 个有
- `ImageConcatMulti` —— 4/13 个有
- `PreviewImage` —— 4/13 个有
- `CR Prompt Text` —— 3/13 个有
- `easy cleanGpuUsed` —— 3/13 个有
- `INTConstant` —— 2/13 个有
- `TextInput_` —— 2/13 个有
- `easy clearCacheAll` —— 2/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `PrimitiveFloat` —— 1/13 个有
- `SDPoseOODLoader` —— 1/13 个有
- `SDPoseOODProcessor` —— 1/13 个有
- `VHS_VideoInfoSource` —— 1/13 个有
- `WanVideoLoraSelectMulti` —— 1/13 个有
- `YOLOModelLoader` —— 1/13 个有
- `easy convertAnything` —— 1/13 个有
- `ttN text` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
