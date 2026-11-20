---
name: unknown_workflow_video_lora_sampler_588
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6244
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/03-09-03-WAN2.1-数字人-MultiTalk+indextts-双人-kijai_1989933411018133506.json, 数字人/数字人/03-10-02-WAN2.1-数字人-InfiniteTalk-两人_1989933552500436993.json, 数字人/数字人/03-10-03-WAN2.1-数字人-InfiniteTalk-长视频_1989933594921586689.json, 数字人/数字人/03-10-04-WAN2.1-数字人-InfiniteTalk-长视频-百组动态提示词_1989933698369941505.json, 数字人/数字人/单场景数字人(发布版)_2017248660681134081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_588

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/03-09-03-WAN2.1-数字人-MultiTalk+indextts-双人-kijai_1989933411018133506.json、数字人/数字人/03-10-02-WAN2.1-数字人-InfiniteTalk-两人_1989933552500436993.json、数字人/数字人/03-10-03-WAN2.1-数字人-InfiniteTalk-长视频_1989933594921586689.json、数字人/数字人/03-10-04-WAN2.1-数字人-InfiniteTalk-长视频-百组动态提示词_1989933698369941505.json、数字人/数字人/单场景数字人(发布版)_2017248660681134081.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `Audio Duration (mtb)` —— 3/5 个有
- `CR Prompt Text` —— 3/5 个有
- `GetImageSizeAndCount` —— 3/5 个有
- `JWIntegerToString` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `Anything Everywhere` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `ColorCorrectOfUtils` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageCASharpening+` —— 1/5 个有
- `JWFloat` —— 1/5 个有
- `MaskPreview+` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `MegaTTS3Run` —— 1/5 个有
- `MultiLinePromptMG` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SaveAudioMP3` —— 1/5 个有
- `SeparateMasks` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
