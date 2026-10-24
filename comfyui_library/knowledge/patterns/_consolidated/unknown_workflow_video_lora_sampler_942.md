---
name: unknown_workflow_video_lora_sampler_942
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.682
common_nodes: [CLIPVisionLoader, CR Text, CreateCFGScheduleFloatList, Fast Groups Muter (rgthree), GetImageSizeAndCount, GetNode, INTConstant, ImageConcatMulti, ImagePadKJ, ImageResizeKJ, ImageResizeKJv2, ImpactInt, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, QwenLoader, SetNode, ShowText|pysssss, SimpleMath+, Text, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoPromptExtender, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoVRAMManagement, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2文生图，图生图，首尾帧，多图参考大集合_1969973981489098753.json, 视频生成/文生视频/Wan2.2文生视频，图生视频，首尾帧，多图参考大集合_1971602288718573570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_942

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.2文生图，图生图，首尾帧，多图参考大集合_1969973981489098753.json、视频生成/文生视频/Wan2.2文生视频，图生视频，首尾帧，多图参考大集合_1971602288718573570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
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

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
