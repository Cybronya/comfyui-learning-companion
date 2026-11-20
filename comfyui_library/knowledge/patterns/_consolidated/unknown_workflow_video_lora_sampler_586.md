---
name: unknown_workflow_video_lora_sampler_586
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9116
common_nodes: [CLIPVisionLoader, CreateVideo, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveFloat, RH_HeyGemNode, SaveAudio, SaveVideo, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/数字人嘴型7-48G显存_1937046981858725889.json, 数字人/数字人/HeyGem图片数字人_1936295290397708289.json, 视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频 科哥数字人_1971066907858214913.json, 视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频_1947692601040322562.json, 视频生成/图生视频/Heygem+FusionX+IndexTTS数字人_1936310993897295873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_586

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/数字人嘴型7-48G显存_1937046981858725889.json、数字人/数字人/HeyGem图片数字人_1936295290397708289.json、视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频 科哥数字人_1971066907858214913.json、视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频_1947692601040322562.json、视频生成/图生视频/Heygem+FusionX+IndexTTS数字人_1936310993897295873.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `CreateVideo`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveFloat`
- `RH_HeyGemNode`
- `SaveAudio`
- `SaveVideo`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `IndexTTSRun` —— 4/5 个有
- `AudioCrop` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `RH_Captioner` —— 3/5 个有
- `Text Concatenate (JPS)` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `D_VideoLengthAdjuster` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `VHS_LoadAudioUpload` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `Bookmark (rgthree)` —— 1/5 个有
- `IndexTTS2Run` —— 1/5 个有
- `JWIntegerAdd` —— 1/5 个有
- `MultiplyNode` —— 1/5 个有
- `Save_Audio` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
