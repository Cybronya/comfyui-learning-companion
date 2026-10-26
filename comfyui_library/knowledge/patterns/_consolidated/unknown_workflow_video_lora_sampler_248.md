---
name: unknown_workflow_video_lora_sampler_248
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.630667
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/INFINITE talk，实现无限时长、口型精准的视频配音_1972120402749222914.json, 视频生成/图生视频/Infinitetalk-视频对口型_2073213335511846913.json, 视频生成/图生视频/打造自己的MTV数字人_1958218756659036162.json, 视频生成/图生视频/无限时长-InfiniteTalk【单人图生视频】和【视频改口型】_1961976886408757249.json, 视频生成/图生视频/视频对口型InfiniteTalk数字人（新版本非常好用）_2003771753522470913.json, 视频生成/图生视频/视频对口型InfiniteTalk数字人（新版本非常好用）_2010335855776374785.json, 视频生成/文生视频/无限时长-InfiniteTalk【单人图生视频】和【视频改口型】_1977338466017136642.json, 音频生成/音频生成/InfiniteTalkV2V 视频对口型数字人说话唱歌_2005896738135306242.json, 音频生成/音频生成/视频对口型 自用_2019776475708268545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_248

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/INFINITE talk，实现无限时长、口型精准的视频配音_1972120402749222914.json、视频生成/图生视频/Infinitetalk-视频对口型_2073213335511846913.json、视频生成/图生视频/打造自己的MTV数字人_1958218756659036162.json、视频生成/图生视频/无限时长-InfiniteTalk【单人图生视频】和【视频改口型】_1961976886408757249.json、视频生成/图生视频/视频对口型InfiniteTalk数字人（新版本非常好用）_2003771753522470913.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `PrimitiveInt` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `GetImageRangeFromBatch` —— 7/9 个有
- `ImageResizeKJv2` —— 7/9 个有
- `LayerUtility: PurgeVRAM` —— 6/9 个有
- `PrimitiveString` —— 6/9 个有
- `SimpleMath+` —— 6/9 个有
- `Audio Duration (mtb)` —— 5/9 个有
- `INTConstant` —— 5/9 个有
- `ImageFromBatch+` —— 4/9 个有
- `JjkText` —— 4/9 个有
- `WanVideoTorchCompileSettings` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `JWIntegerToString` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `RH_Translator` —— 2/9 个有
- `Text Concatenate` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `Blur` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `SeedVR2GGUF` —— 1/9 个有
- `Text` —— 1/9 个有
- `VHS_VideoInfo` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
