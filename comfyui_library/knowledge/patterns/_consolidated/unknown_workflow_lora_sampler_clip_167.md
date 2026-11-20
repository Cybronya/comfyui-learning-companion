---
name: unknown_workflow_lora_sampler_clip_167
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.66225
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CreateVideo, ImageBatch, ImageFromBatch, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAELoader, WanInfiniteTalkToVideo]
problems: []
missing: []
members: [数字人/数字人/infinitalk-数字人唱歌对口型-无限时长_2060296846307844097.json, 视频生成/图生视频/InfiniteTalk：图片 + 音频，生成数字人视频_2042859514055106562.json, 视频生成/图生视频/InfiniteTalk：图片 + 音频，生成数字人视频_2066742321412136962.json, 视频生成/图生视频/官方版InfineTalk长视频生成(无劣化)_2019387715191578626.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/infinitalk-数字人唱歌对口型-无限时长_2060296846307844097.json、视频生成/图生视频/InfiniteTalk：图片 + 音频，生成数字人视频_2042859514055106562.json、视频生成/图生视频/InfiniteTalk：图片 + 音频，生成数字人视频_2066742321412136962.json、视频生成/图生视频/官方版InfineTalk长视频生成(无劣化)_2019387715191578626.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CreateVideo`
- `ImageBatch`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`
- `WanInfiniteTalkToVideo`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ModelPatchTorchSettings` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `FL_Audio_Crop` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `ImageScaleToMaxDimension` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `WujiAudioLoader` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
