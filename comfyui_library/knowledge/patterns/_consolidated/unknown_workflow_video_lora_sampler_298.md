---
name: unknown_workflow_video_lora_sampler_298
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.964444
common_nodes: [Apply Whisper, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SoundFlow_TrimAudio, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/69-tszrvideo_2053019815362744322.json, 图片生成/反推提示词/99视频数字人spszr放大_2046871555069714433.json, 图片生成/反推提示词/数字人形象_2062166224678772738.json, 数字人/数字人/infinite视频单人对口型_2003664453008826370.json, 数字人/数字人/最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610.json, 数字人/数字人/视频数字人对口型_2017542922996031489.json, 视频生成/图生视频/【亲测好用】最强视频数字人对口型万相wan2.1Q8+InfiniteTalk+VoxCPM TTS超长超自然_1994362409961857025.json, 音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json, 音频生成/音频生成/视频数字人对口型_1985952196049215490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_298

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/69-tszrvideo_2053019815362744322.json、图片生成/反推提示词/99视频数字人spszr放大_2046871555069714433.json、图片生成/反推提示词/数字人形象_2062166224678772738.json、数字人/数字人/infinite视频单人对口型_2003664453008826370.json、数字人/数字人/最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `Apply Whisper`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SoundFlow_TrimAudio`
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
- `LoadAudio` —— 8/9 个有
- `SimpleMath+` —— 8/9 个有
- `VHS_LoadVideo` —— 8/9 个有
- `Float to Int` —— 7/9 个有
- `GetNode` —— 7/9 个有
- `RH_GetAudioDuration` —— 7/9 个有
- `easy anythingIndexSwitch` —— 7/9 个有
- `String Literal` —— 6/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `VoxCPM_TTS` —— 6/9 个有
- `CreateVideo` —— 3/9 个有
- `ImageConcatMulti` —— 3/9 个有
- `IndexTTS2_Emotion` —— 3/9 个有
- `RTXVideoSuperResolution` —— 3/9 个有
- `SaveVideo` —— 3/9 个有
- `Anything Everywhere` —— 2/9 个有
- `Audio Duration (mtb)` —— 1/9 个有
- `LoadVideoFromUrl` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `VHS_LoadAudio` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
