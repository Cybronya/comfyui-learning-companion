---
name: unknown_workflow_video_lora_sampler_327
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.963714
common_nodes: [Apply Whisper, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, SoundFlow_TrimAudio, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy anythingIndexSwitch]
problems: []
missing: []
members: [图片生成/反推提示词/69-tszrvideo_2053019815362744322.json, 图片生成/反推提示词/99视频数字人spszr放大_2046871555069714433.json, 图片生成/反推提示词/数字人形象_2062166224678772738.json, 数字人/数字人/infinite视频单人对口型_2003664453008826370.json, 数字人/数字人/最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610.json, 数字人/数字人/视频数字人对口型_2017542922996031489.json, 视频生成/图生视频/【亲测好用】最强视频数字人对口型万相wan2.1Q8+InfiniteTalk+VoxCPM TTS超长超自然_1994362409961857025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_327

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/69-tszrvideo_2053019815362744322.json、图片生成/反推提示词/99视频数字人spszr放大_2046871555069714433.json、图片生成/反推提示词/数字人形象_2062166224678772738.json、数字人/数字人/infinite视频单人对口型_2003664453008826370.json、数字人/数字人/最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `Apply Whisper`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
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
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `Float to Int` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `RH_GetAudioDuration` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `String Literal` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `VoxCPM_TTS` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `IndexTTS2_Emotion` —— 3/7 个有
- `RTXVideoSuperResolution` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `Audio Duration (mtb)` —— 1/7 个有
- `LoadVideoFromUrl` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `VHS_LoadAudio` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
