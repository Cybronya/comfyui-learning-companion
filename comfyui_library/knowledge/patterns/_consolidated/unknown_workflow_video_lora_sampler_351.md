---
name: unknown_workflow_video_lora_sampler_351
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.93275
common_nodes: [CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/4高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）(1)_2118258030931435522.json, 数字人/数字人/multitalk自用2_2031936631246163970.json, 数字人/数字人/数字人_音画同步_对口型 Infinite Talk_2007786312845238273.json, 数字人/数字人/数字人_音画同步_对口型 Infinite Talk_2009303457294979073.json, 数字人/数字人/数字人_音画同步_对口型 Infinite Talk_2032822478120161282.json, 数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json, 视频生成/图生视频/30号特工：Infinite talk数字人=对口型爆款创造机：唱歌+脱口秀+口播栏目_2045026952746115073.json, "音频生成/音频生成/MV,音乐达人，高动态音乐数字人_2046930658349555714.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_351

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/4高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）(1)_2118258030931435522.json、数字人/数字人/multitalk自用2_2031936631246163970.json、数字人/数字人/数字人_音画同步_对口型 Infinite Talk_2007786312845238273.json、数字人/数字人/数字人_音画同步_对口型 Infinite Talk_2009303457294979073.json、数字人/数字人/数字人_音画同步_对口型 Infinite Talk_2032822478120161282.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 7/8 个有
- `JWInteger` —— 7/8 个有
- `AudioCrop` —— 6/8 个有
- `AudioSeparation` —— 6/8 个有
- `SimpleMath+` —— 5/8 个有
- `ToInt` —— 5/8 个有
- `Bjornulf_ShowInt` —— 4/8 个有
- `SoundFlow_GetLength` —— 4/8 个有
- `VRGDG_AudioCropTime` —— 3/8 个有
- `easy int` —— 3/8 个有
- `Bjornulf_ShowFloat` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ImpactSwitch` —— 2/8 个有
- `IndexTTS2Run` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `PrimitiveString` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `SaveAudio` —— 2/8 个有
- `ColorMatch` —— 1/8 个有
- `GetAudioDurationFromAudio` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `Pick From Batch (mtb)` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `WanVideoTorchCompileSettings` —— 1/8 个有
- `easy imageConcat` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
