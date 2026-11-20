---
name: unknown_workflow_video_lora_sampler_583
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9545
common_nodes: [DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/infinite+wan2.1多人对口型_1960541577531842561.json, 视频生成/图生视频/infinitetalk单人图生视频对口型_1960923370206498818.json, 视频生成/图生视频/infinitetalk双人对话（自动识别人物）_2035945836609277954.json, 视频生成/图生视频/multitalk-wan-双人-index tts_1941378778566389761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_583

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/infinite+wan2.1多人对口型_1960541577531842561.json、视频生成/图生视频/infinitetalk单人图生视频对口型_1960923370206498818.json、视频生成/图生视频/infinitetalk双人对话（自动识别人物）_2035945836609277954.json、视频生成/图生视频/multitalk-wan-双人-index tts_1941378778566389761.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `AudioSeparation` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `WanVideoClipVisionEncode` —— 3/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `SeparateMasks` —— 2/4 个有
- `AudioCropProcessUTK` —— 1/4 个有
- `ImageScaleToMegapixels` —— 1/4 个有
- `IndexTTSRun` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `MaskPreview` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RH_GetAudioDuration` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `StringToInt` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
