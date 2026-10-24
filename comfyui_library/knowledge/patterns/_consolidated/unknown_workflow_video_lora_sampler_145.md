---
name: unknown_workflow_video_lora_sampler_145
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.726333
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/infiniteTalk（音色克隆+音频生成）_1970143422839463937.json, 视频生成/图生视频/infinitetalk+indextts2带情感控制打造对口型_唱歌数字人 强强联合一键生成_1982723691039596546.json, 视频生成/图生视频/infinitetalk+indextts2带情感控制打造对口型_唱歌数字人 强强联合一键生成_1988525080521129985.json, 视频生成/图生视频/infinitetalk-音频+图片数字人_1960547168962641921.json, 视频生成/图生视频/infinitetalk-音频+图片数字人_1977757445852463106.json, 视频生成/图生视频/三笔成书——数字人=图片+文本+声音克隆_1996928089819136001.json, 视频生成/图生视频/数字人=图片+文本+声音克隆_1996900266379300866.json, 视频生成/图生视频/数字人=图片+文本+声音克隆王改革_2000473873579638786.json, 视频生成/图生视频/数字人TTS2+infiniteTalk高清电影对嘴型_1965116783160082434.json, 视频生成/图生视频/数字人对嘴型InfiniteTalk无限时长加载音频版_1965715999553159169.json, 音频生成/音频生成/infiniteTalk（音色克隆+音频生成）_1970169527449382913.json, 音频生成/音频生成/数字人TTS2+infiniteTalk高清电影对嘴型_1965919852949082113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_145

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/infiniteTalk（音色克隆+音频生成）_1970143422839463937.json、视频生成/图生视频/infinitetalk+indextts2带情感控制打造对口型_唱歌数字人 强强联合一键生成_1982723691039596546.json、视频生成/图生视频/infinitetalk+indextts2带情感控制打造对口型_唱歌数字人 强强联合一键生成_1988525080521129985.json、视频生成/图生视频/infinitetalk-音频+图片数字人_1960547168962641921.json、视频生成/图生视频/infinitetalk-音频+图片数字人_1977757445852463106.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 12 个 workflow 都包含：
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
- `AudioCrop` —— 10/12 个有
- `AudioSeparation` —— 10/12 个有
- `INTConstant` —— 10/12 个有
- `PreviewAny` —— 10/12 个有
- `PreviewAudio` —— 9/12 个有
- `GetNode` —— 8/12 个有
- `LayerUtility: PurgeVRAM V2` —— 8/12 个有
- `IndexTTS2Run` —— 7/12 个有
- `ImageUpscaleWithModel` —— 6/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/12 个有
- `UpscaleModelLoader` —— 6/12 个有
- `CR Text` —— 4/12 个有
- `JjkText` —— 4/12 个有
- `MegaTTS3` —— 4/12 个有
- `ImpactSwitch` —— 2/12 个有
- `IndexTTS2_Emotion` —— 2/12 个有
- `JWInteger` —— 2/12 个有
- `PrimitiveFloat` —— 2/12 个有
- `RH_Translator` —— 2/12 个有
- `MultiLinePromptIndex` —— 1/12 个有
- `SaveAudioMP3` —— 1/12 个有
- `easy compare` —— 1/12 个有
- `easy ifElse` —— 1/12 个有
- `easy imageSize` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
