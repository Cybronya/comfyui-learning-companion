---
name: unknown_workflow_video_lora_sampler_181
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6228
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM, SimpleMath+, Text Concatenate, Text Multiline]
members: [视频生成/图生视频/1977338466017136642.json, 视频生成/图生视频/1975057390238306306.json, 视频生成/图生视频/2021869907490639874.json, 视频生成/图生视频/1961976886408757249.json, 视频生成/图生视频/2003771753522470913.json, 视频生成/图生视频/2010335855776374785.json, 视频生成/文生视频/1977338466017136642.json, 音频生成/音频生成/InfiniteTalkV2V 视频对口型数字人说话唱歌_2005896738135306242.json, 音频生成/音频生成/视频对口型 自用_2019776475708268545.json, 音频生成/音频生成/视频对口型（指定角色）_2012598659203997698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_181

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1977338466017136642.json、视频生成/图生视频/1975057390238306306.json、视频生成/图生视频/2021869907490639874.json、视频生成/图生视频/1961976886408757249.json、视频生成/图生视频/2003771753522470913.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `PrimitiveString` —— 9/10 个有
- `SimpleMath+` —— 9/10 个有
- `VHS_LoadVideo` —— 9/10 个有
- `WanVideoEncode` —— 9/10 个有
- `Audio Duration (mtb)` —— 6/10 个有
- `GetImageRangeFromBatch` —— 6/10 个有
- `ImageFromBatch+` —— 6/10 个有
- `JjkText` —— 6/10 个有
- `RH_Translator` —— 5/10 个有
- `LoadImage` —— 4/10 个有
- `WanVideoTorchCompileSettings` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `INTConstant` —— 3/10 个有
- `Text Concatenate` —— 3/10 个有
- `Text Multiline` —— 3/10 个有
- `Blur` —— 2/10 个有
- `SeedVR2GGUF` —— 2/10 个有
- `AILab_MaskPreview` —— 1/10 个有
- `ImageFromBatch` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `MaskListToMaskBatch` —— 1/10 个有
- `PreviewAudio` —— 1/10 个有
- `Text` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy sam3ModelLoader` —— 1/10 个有
- `easy sam3VideoSegmentation` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、SimpleMath+、Text Concatenate、Text Multiline
