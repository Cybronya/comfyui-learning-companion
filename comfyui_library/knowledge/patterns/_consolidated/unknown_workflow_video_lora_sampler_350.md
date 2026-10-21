---
name: unknown_workflow_video_lora_sampler_350
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.539833
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM, SimpleMath+, Text Concatenate, Text Multiline]
members: [视频生成/图生视频/1977338466017136642.json, 视频生成/图生视频/1975057390238306306.json, 视频生成/图生视频/1961976886408757249.json, 视频生成/图生视频/1958125817404542978.json, 视频生成/图生视频/1958125770365423618.json, 视频生成/文生视频/1977338466017136642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_350

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1977338466017136642.json、视频生成/图生视频/1975057390238306306.json、视频生成/图生视频/1961976886408757249.json、视频生成/图生视频/1958125817404542978.json、视频生成/图生视频/1958125770365423618.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 5/6 个有
- `PrimitiveInt` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `RH_Translator` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `INTConstant` —— 3/6 个有
- `LayerUtility: PurgeVRAM` —— 3/6 个有
- `PrimitiveString` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `Text Concatenate` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `WanVideoEncode` —— 3/6 个有
- `Blur` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `SeedVR2GGUF` —— 2/6 个有
- `IndexTTSNode` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `JWIntegerToString` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、SimpleMath+、Text Concatenate、Text Multiline
