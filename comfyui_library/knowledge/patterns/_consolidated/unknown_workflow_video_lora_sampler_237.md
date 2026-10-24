---
name: unknown_workflow_video_lora_sampler_237
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.920375
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Wan2.1单人对口型_2096760991131455490.json, 视频生成/图生视频/IndexTTS 1.5 +InfiniteTalk数字人_1983435435332575234.json, 视频生成/图生视频/Wan2.1+InfiniteTalk_单人_图片转数字人_1988813564645355522.json, 视频生成/图生视频/Wan2.1单人对口型_2064352779824623618.json, "视频生成/图生视频/图加音频生视频,非常丝滑，支持160秒_2044837678058835969.json", 视频生成/图生视频/图加音频生视频_2016326225295314946.json, 视频生成/图生视频/图加音频生视频——V1_2018257190561255426.json, 视频生成/文生视频/infinitetalk图片数字人唱歌不限时长版_2004411444588408834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_237

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Wan2.1单人对口型_2096760991131455490.json、视频生成/图生视频/IndexTTS 1.5 +InfiniteTalk数字人_1983435435332575234.json、视频生成/图生视频/Wan2.1+InfiniteTalk_单人_图片转数字人_1988813564645355522.json、视频生成/图生视频/Wan2.1单人对口型_2064352779824623618.json、视频生成/图生视频/图加音频生视频,非常丝滑，支持160秒_2044837678058835969.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 7/8 个有
- `DownloadAndLoadWav2VecModel` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `INTConstant` —— 5/8 个有
- `WanVideoDecode` —— 5/8 个有
- `Anything Everywhere` —— 4/8 个有
- `AudioCrop` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `WanVideoPassImagesFromSamples` —— 3/8 个有
- `Wav2VecModelLoader` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `FancyTimerNode` —— 2/8 个有
- `ImageScale` —— 2/8 个有
- `easy getNode` —— 2/8 个有
- `easy setNode` —— 2/8 个有
- `IndexTTSNode` —— 1/8 个有
- `VHS_LoadAudioUpload` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
