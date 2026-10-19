---
name: unknown_workflow_video_lora_sampler_754
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.938
common_nodes: [AudioCrop, CLIPVisionLoader, CreateVideo, INTConstant, ImageResizeKJ, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, PrimitiveFloat, RH_Captioner, RH_HeyGemNode, SaveAudio, SaveVideo, Text Concatenate (JPS), TextInput_, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频 科哥数字人_1971066907858214913.json, 视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频_1947692601040322562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_754

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频 科哥数字人_1971066907858214913.json、视频生成/图生视频/HeyGem＋index-tts＋图片＋wan视频模型=数字人口播视频_1947692601040322562.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
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
- `Bookmark (rgthree)` —— 1/2 个有
- `IndexTTS2Run` —— 1/2 个有
- `IndexTTSRun` —— 1/2 个有
- `Save_Audio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
