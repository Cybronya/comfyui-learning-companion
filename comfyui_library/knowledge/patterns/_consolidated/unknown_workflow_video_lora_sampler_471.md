---
name: unknown_workflow_video_lora_sampler_471
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.65
common_nodes: [CLIPVisionLoader, CR Text, CreateCFGScheduleFloatList, Fast Groups Muter (rgthree), GetImageSizeAndCount, GetNode, INTConstant, ImageConcatMulti, ImagePadKJ, ImageResizeKJ, ImageResizeKJv2, ImpactInt, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, QwenLoader, SetNode, ShowText|pysssss, SimpleMath+, Text, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoPromptExtender, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoVRAMManagement, easy cleanGpuUsed]
problems: []
missing: [CR Text, SimpleMath+, easy cleanGpuUsed]
members: [视频生成/图生视频/1969973981489098753.json, 视频生成/图生视频/1971602288718573570.json, 视频生成/文生视频/1969973981489098753.json, 视频生成/文生视频/1971602288718573570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_471

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1969973981489098753.json、视频生成/图生视频/1971602288718573570.json、视频生成/文生视频/1969973981489098753.json、视频生成/文生视频/1971602288718573570.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `CreateCFGScheduleFloatList`
- `Fast Groups Muter (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImpactInt`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `QwenLoader`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoPromptExtender`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`
- `easy cleanGpuUsed`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、SimpleMath+、easy cleanGpuUsed
