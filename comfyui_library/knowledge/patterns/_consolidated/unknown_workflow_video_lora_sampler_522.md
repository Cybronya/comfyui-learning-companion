---
name: unknown_workflow_video_lora_sampler_522
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7235
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/infinite talk 数字人-音频驱动图片_2017646230746173442.json, 视频生成/图生视频/infinitetalk双人对话版支持长时间语音_2026541463353434114.json, 视频生成/图生视频/infintetalk合成唱歌视频_1990334829420007425.json, 视频生成/图生视频/音频+图片数字人_2004504763003793409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_522

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/infinite talk 数字人-音频驱动图片_2017646230746173442.json、视频生成/图生视频/infinitetalk双人对话版支持长时间语音_2026541463353434114.json、视频生成/图生视频/infintetalk合成唱歌视频_1990334829420007425.json、视频生成/图生视频/音频+图片数字人_2004504763003793409.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 3/4 个有
- `WanVideoTextEncode` —— 3/4 个有
- `easy int` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Float` —— 1/4 个有
- `GetAudioDurationFromAudio` —— 1/4 个有
- `Int` —— 1/4 个有
- `JWFloat` —— 1/4 个有
- `LayerUtility: TextBox` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `SaveAudio` —— 1/4 个有
- `SeedVCRun` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoTextEncodeCached` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
