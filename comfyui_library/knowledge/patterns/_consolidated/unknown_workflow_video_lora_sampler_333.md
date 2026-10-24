---
name: unknown_workflow_video_lora_sampler_333
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.639
common_nodes: [ColorMatch, DWPreprocessor, GetImageSizeAndCount, GetNode, ImageResizeKJv2, Int2String, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, Text Multiline, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoFreeInitArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/图生图/凯凯优化1_1955926643237945345.json, 视频生成/图生视频/WAN动作迁移（30秒直出16GB显存可运行））_1964522660736679938.json, 视频生成/图生视频/【视频转绘】lightx2v_256 一口气201帧直出超高质量_1948987211699105793.json, 视频生成/图生视频/一致性视频转绘 Stand-In VACE_1956979813429776386.json, 视频生成/文生视频/一致性替换人物Stand-In VACE_1957623474036600834.json, 视频生成/文生视频/凯凯1_1955564554321367042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_333

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/凯凯优化1_1955926643237945345.json、视频生成/图生视频/WAN动作迁移（30秒直出16GB显存可运行））_1964522660736679938.json、视频生成/图生视频/【视频转绘】lightx2v_256 一口气201帧直出超高质量_1948987211699105793.json、视频生成/图生视频/一致性视频转绘 Stand-In VACE_1956979813429776386.json、视频生成/文生视频/一致性替换人物Stand-In VACE_1957623474036600834.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 6 个 workflow 都包含：
- `ColorMatch`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `Int2String`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `Text Multiline`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoFreeInitArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `ShowText` —— 5/6 个有
- `SimpleCondition+` —— 5/6 个有
- `ApplyFaceProcessor` —— 3/6 个有
- `DepthAnything_V2` —— 3/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/6 个有
- `FaceProcessorLoader` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `WanVideoAddStandInLatent` —— 3/6 个有
- `WanVideoEncode` —— 3/6 个有
- `WanVideoSetLoRAs` —— 3/6 个有
- `WanVideoSetRadialAttention` —— 3/6 个有
- `WanVideoVACEStartToEndFrame` —— 3/6 个有
- `preview_mask` —— 3/6 个有
- `AddLabel` —— 2/6 个有
- `ImageConcanate` —— 2/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/6 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/6 个有
- `Mask Invert` —— 1/6 个有
- `MaskToImage` —— 1/6 个有
- `Mix Color By Mask` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `WanVideoContextOptions` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
