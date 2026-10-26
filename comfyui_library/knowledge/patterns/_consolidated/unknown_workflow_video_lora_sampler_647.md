---
name: unknown_workflow_video_lora_sampler_647
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.937
common_nodes: [AudioCrop, CLIPVisionLoader, CreateVideo, INTConstant, ImageResizeKJ, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, PrimitiveFloat, RH_Captioner, RH_HeyGemNode, SaveAudio, SaveVideo, Text Concatenate (JPS), TextInput_, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/HeyGem图片数字人_1936295290397708289.json, 视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频 科哥数字人_1971066907858214913.json, 视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频_1947692601040322562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_647

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/HeyGem图片数字人_1936295290397708289.json、视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频 科哥数字人_1971066907858214913.json、视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频_1947692601040322562.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `CLIPVisionLoader`
- `CreateVideo`
- `INTConstant`
- `ImageResizeKJ`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_Captioner`
- `RH_HeyGemNode`
- `SaveAudio`
- `SaveVideo`
- `Text Concatenate (JPS)`
- `TextInput_`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `IndexTTSRun` —— 2/3 个有
- `Bookmark (rgthree)` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `Save_Audio` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
