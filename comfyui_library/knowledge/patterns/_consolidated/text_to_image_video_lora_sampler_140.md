---
name: text_to_image_video_lora_sampler_140
type: Text To Image
frequency: 4
level: strong
coverage: 0.905
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, GetImageRangeFromBatch, ImageResizeKJv2, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Infinitetalk视频转数字人动态更强更自然 数字人口播方案_2109715456281104385.json, 数字人/数字人/真人视频数字人口播对口型 数字人视频生成方案_2109073300885426178.json, 视频生成/图生视频/超强视频对口型唱歌数字人 数字人视频生成_2100276742337417218.json, 音频生成/音频生成/视频转视频配音｜InfiniteTalk数字人音频生成_2091228835768528897.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_140

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/Infinitetalk视频转数字人动态更强更自然 数字人口播方案_2109715456281104385.json、数字人/数字人/真人视频数字人口播对口型 数字人视频生成方案_2109073300885426178.json、视频生成/图生视频/超强视频对口型唱歌数字人 数字人视频生成_2100276742337417218.json、音频生成/音频生成/视频转视频配音｜InfiniteTalk数字人音频生成_2091228835768528897.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `AudioSeparation` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `SimpleMath+` —— 2/4 个有
- `SoundFlow_GetLength` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `easy int` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `Anything Everywhere` —— 1/4 个有
- `Display Int (rgthree)` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Float to Int` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `Getter` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageBatchMulti` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `Qwen3TTSModelLoader` —— 1/4 个有
- `Qwen3TTSVoiceDesign` —— 1/4 个有
- `ReverseImageBatch` —— 1/4 个有
- `Setter` —— 1/4 个有
- `ToInt` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有
- `VHS_SelectEveryNthImage` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
