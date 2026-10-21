---
name: unknown_workflow_video_lora_sampler_191
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.688
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1970143422839463937.json, 视频生成/图生视频/1982723691039596546.json, 视频生成/图生视频/1988525080521129985.json, 视频生成/图生视频/1960547168962641921.json, 视频生成/图生视频/1977757445852463106.json, 视频生成/图生视频/2012499953494528001.json, 视频生成/图生视频/1965116783160082434.json, 视频生成/图生视频/1965715999553159169.json, 音频生成/音频生成/infiniteTalk（音色克隆+音频生成）_1970169527449382913.json, 音频生成/音频生成/数字人TTS2+infiniteTalk高清电影对嘴型_1965919852949082113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_191

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1970143422839463937.json、视频生成/图生视频/1982723691039596546.json、视频生成/图生视频/1988525080521129985.json、视频生成/图生视频/1960547168962641921.json、视频生成/图生视频/1977757445852463106.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 10 个 workflow 都包含：
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
- `GetNode` —— 9/10 个有
- `AudioCrop` —— 8/10 个有
- `AudioSeparation` —— 8/10 个有
- `INTConstant` —— 8/10 个有
- `PreviewAny` —— 8/10 个有
- `PreviewAudio` —— 6/10 个有
- `LayerUtility: PurgeVRAM V2` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `IndexTTS2Run` —— 4/10 个有
- `MegaTTS3` —— 4/10 个有
- `ImageUpscaleWithModel` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `UpscaleModelLoader` —— 3/10 个有
- `ImpactSwitch` —— 2/10 个有
- `IndexTTS2_Emotion` —— 2/10 个有
- `JWInteger` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `JjkText` —— 1/10 个有
- `MultiLinePromptIndex` —— 1/10 个有
- `SaveAudioMP3` —— 1/10 个有
- `easy compare` —— 1/10 个有
- `easy ifElse` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
