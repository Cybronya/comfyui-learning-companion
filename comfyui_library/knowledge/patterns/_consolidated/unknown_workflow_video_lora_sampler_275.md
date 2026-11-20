---
name: unknown_workflow_video_lora_sampler_275
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6243
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/infinitetalk-音频+视频数字人_1960547223945773057.json, 数字人/数字人/wanvideo_infinitetalk_小宝_2017971113397067777.json, 数字人/数字人/商用版-最强数字人视频对口型_1973158648119734274.json, 数字人/数字人/无限时长音乐数字人-InfiniteTalk单人视频到视频_1958187031639822338.json, 数字人/数字人/超真实无限时长唱歌数字人-InfiniteTalk_1986407714731552769.json, 视频生成/图生视频/InfiniteTalk+wan2.1单图片_视频生成口播数字人视频_1958754013288296450.json, 视频生成/图生视频/Y-InfiniteTalk单人图生视频_1958373813031485441.json, 视频生成/图生视频/打造自己的MTV数字人_1958218756659036162.json, 视频生成/图生视频/无限时长-InfiniteTalk【单人图生视频】和【视频改口型】_1961976886408757249.json, 视频生成/文生视频/无限时长-InfiniteTalk【单人图生视频】和【视频改口型】_1977338466017136642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_275

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/infinitetalk-音频+视频数字人_1960547223945773057.json、数字人/数字人/wanvideo_infinitetalk_小宝_2017971113397067777.json、数字人/数字人/商用版-最强数字人视频对口型_1973158648119734274.json、数字人/数字人/无限时长音乐数字人-InfiniteTalk单人视频到视频_1958187031639822338.json、数字人/数字人/超真实无限时长唱歌数字人-InfiniteTalk_1986407714731552769.json…）

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
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `ImageResizeKJv2` —— 9/10 个有
- `GetNode` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `VHS_LoadVideo` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `PrimitiveInt` —— 7/10 个有
- `GetImageSizeAndCount` —— 6/10 个有
- `INTConstant` —— 6/10 个有
- `Text Multiline` —— 6/10 个有
- `WanVideoEncode` —— 6/10 个有
- `WanVideoTextEncodeCached` —— 6/10 个有
- `JWIntegerToString` —— 5/10 个有
- `PreviewAny` —— 5/10 个有
- `LoadImage` —— 4/10 个有
- `LoadWanVideoT5TextEncoder` —— 4/10 个有
- `WanVideoTextEncode` —— 4/10 个有
- `GetImageRangeFromBatch` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `JWInteger` —— 2/10 个有
- `LayerUtility: PurgeVRAM` —— 2/10 个有
- `PrimitiveString` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `Text Concatenate` —— 2/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/10 个有
- `WanVideoUni3C_embeds` —— 2/10 个有
- `Blur` —— 1/10 个有
- `ImageBatchMulti` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `MuyeLoadImage` —— 1/10 个有
- `ReverseImageBatch` —— 1/10 个有
- `SeedVR2GGUF` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
