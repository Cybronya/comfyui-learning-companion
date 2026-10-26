---
name: unknown_workflow_video_sampler_vae_180
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8345
common_nodes: [AudioCrop, AudioSeparation, CR Text Concatenate, ColorMatch, CreateCFGScheduleFloatList, Display Int (rgthree), DownloadAndLoadWav2VecModel, GetImageSizeAndCount, INTConstant, ImageConcatMulti, ImageFromBatch+, ImageResizeKJ, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, PrimitiveString, SimpleMath+, SoundFlow_GetLength, Text Multiline, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy imageRemBg, easy int]
problems: []
missing: []
members: [数字人/数字人/wan2.2数字人_1987723803025412097.json, 数字人/数字人/wan2.2数字人_1991331380875362306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_180

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/wan2.2数字人_1987723803025412097.json、数字人/数字人/wan2.2数字人_1991331380875362306.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CR Text Concatenate`
- `ColorMatch`
- `CreateCFGScheduleFloatList`
- `Display Int (rgthree)`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `PrimitiveString`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `Text Multiline`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy imageRemBg`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `TT_img_enc` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
