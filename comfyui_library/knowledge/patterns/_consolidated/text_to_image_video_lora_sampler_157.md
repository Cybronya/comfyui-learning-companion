---
name: text_to_image_video_lora_sampler_157
type: Text To Image
frequency: 4
level: strong
coverage: 0.82325
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, GetImageSizeAndCount, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoraLoaderModelOnly, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417.json, 数字人/数字人/极速版数字人打造个人IP，视频生视频快速出片_2110886810279833601.json, 数字人/数字人/音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945.json, 视频生成/图生视频/Wan2.1 InfiniTetalk图像数字人配口型KJ节点人物特效_2088176935515021313.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417.json、数字人/数字人/极速版数字人打造个人IP，视频生视频快速出片_2110886810279833601.json、数字人/数字人/音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945.json、视频生成/图生视频/Wan2.1 InfiniTetalk图像数字人配口型KJ节点人物特效_2088176935515021313.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 3/4 个有
- `GetImageRangeFromBatch` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `WanVideoTextEncodeCached` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `ColorMatch` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `TrimAudioDuration` —— 2/4 个有
- `AudioCrop` —— 1/4 个有
- `AudioDuration_wan` —— 1/4 个有
- `H3ModeSwitch` —— 1/4 个有
- `IndexTTS2Run` —— 1/4 个有
- `LoadWanVideoT5TextEncoder` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `WanVideoTextEncode` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
