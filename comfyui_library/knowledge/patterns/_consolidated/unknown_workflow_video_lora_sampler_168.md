---
name: unknown_workflow_video_lora_sampler_168
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.743545
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1970143422839463937.json, 视频生成/图生视频/1982723691039596546.json, 视频生成/图生视频/1988525080521129985.json, 视频生成/图生视频/1967501356460335105.json, 视频生成/图生视频/1996928089819136001.json, 视频生成/图生视频/1996900266379300866.json, 视频生成/图生视频/2000473873579638786.json, 视频生成/图生视频/1965116783160082434.json, 视频生成/图生视频/1965715999553159169.json, 音频生成/音频生成/infiniteTalk（音色克隆+音频生成）_1970169527449382913.json, 音频生成/音频生成/数字人TTS2+infiniteTalk高清电影对嘴型_1965919852949082113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_168

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1970143422839463937.json、视频生成/图生视频/1982723691039596546.json、视频生成/图生视频/1988525080521129985.json、视频生成/图生视频/1967501356460335105.json、视频生成/图生视频/1996928089819136001.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
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
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 10/11 个有
- `AudioCrop` —— 9/11 个有
- `AudioSeparation` —— 9/11 个有
- `INTConstant` —— 9/11 个有
- `PreviewAny` —— 9/11 个有
- `LayerUtility: PurgeVRAM V2` —— 8/11 个有
- `IndexTTS2Run` —— 7/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/11 个有
- `GetNode` —— 6/11 个有
- `ImageUpscaleWithModel` —— 6/11 个有
- `UpscaleModelLoader` —— 6/11 个有
- `CR Text` —— 4/11 个有
- `JjkText` —— 4/11 个有
- `MegaTTS3` —— 4/11 个有
- `ImpactSwitch` —— 2/11 个有
- `IndexTTS2_Emotion` —— 2/11 个有
- `JWInteger` —— 2/11 个有
- `PrimitiveFloat` —— 2/11 个有
- `RH_Translator` —— 2/11 个有
- `Fast Bypasser (rgthree)` —— 1/11 个有
- `MelBandRoFormerModelLoader` —— 1/11 个有
- `MelBandRoFormerSampler` —— 1/11 个有
- `MultiLinePromptIndex` —— 1/11 个有
- `SaveAudioMP3` —— 1/11 个有
- `Switch any [Crystools]` —— 1/11 个有
- `Wav2VecModelLoader` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
