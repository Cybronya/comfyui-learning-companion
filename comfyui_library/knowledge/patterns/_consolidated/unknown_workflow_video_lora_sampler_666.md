---
name: unknown_workflow_video_lora_sampler_666
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/全能图片V1+MegaTTS3+InfiniteTalk数字人带货_1963202407591292929.json, 视频生成/图生视频/图生视频-基于InfiniteTalk_2005465061298761730.json, 视频生成/文生视频/全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_666

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/全能图片V1+MegaTTS3+InfiniteTalk数字人带货_1963202407591292929.json、视频生成/图生视频/图生视频-基于InfiniteTalk_2005465061298761730.json、视频生成/文生视频/全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `MelBandRoFormerModelLoader` —— 2/3 个有
- `MelBandRoFormerSampler` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `RH_Nano_Banana_Image2Image` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `SoundFlow_GetLength` —— 2/3 个有
- `String Literal` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `JWStringMultiline` —— 1/3 个有
- `MegaTTS3Run` —— 1/3 个有
- `SaveAudioMP3` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
