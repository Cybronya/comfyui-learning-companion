---
name: unknown_workflow_video_lora_sampler_236
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.815111
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2017646230746173442.json, 视频生成/图生视频/1959143275817021441.json, 视频生成/图生视频/1994005595265105922.json, 视频生成/图生视频/1990334829420007425.json, 视频生成/图生视频/1978136142623203329.json, 视频生成/图生视频/1979895392475189249.json, 视频生成/图生视频/2039336418778030081.json, 视频生成/图生视频/1970560402209841153.json, 音频生成/音频生成/顶配视频版 单人-双人[完美口型数字人]_1970863789459546113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_236

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2017646230746173442.json、视频生成/图生视频/1959143275817021441.json、视频生成/图生视频/1994005595265105922.json、视频生成/图生视频/1990334829420007425.json、视频生成/图生视频/1978136142623203329.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 8/9 个有
- `GetImageSizeAndCount` —— 8/9 个有
- `PreviewAny` —— 8/9 个有
- `CR Prompt Text` —— 7/9 个有
- `JWInteger` —— 7/9 个有
- `WanVideoBlockSwap` —— 7/9 个有
- `GetNode` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `JWFloat` —— 3/9 个有
- `SaveAudio` —— 3/9 个有
- `easy int` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `MaskPreview+` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `MegaTTS3Run` —— 2/9 个有
- `PreviewAudio` —— 2/9 个有
- `SaveAudioMP3` —— 2/9 个有
- `SeparateMasks` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `VoxCPM_TTS` —— 2/9 个有
- `WanVideoTorchCompileSettings` —— 2/9 个有
- `easy downloadIndexTTSAndLoadModel` —— 2/9 个有
- `easy indexTTSAudioMerge` —— 2/9 个有
- `easy indexTTSGenerateSimple` —— 2/9 个有
- `Float` —— 1/9 个有
- `IndexTTS2Run` —— 1/9 个有
- `Int` —— 1/9 个有
- `LayerUtility: TextBox` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `SeedVCRun` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
