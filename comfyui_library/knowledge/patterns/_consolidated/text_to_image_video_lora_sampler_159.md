---
name: text_to_image_video_lora_sampler_159
type: Text To Image
frequency: 3
level: strong
coverage: 0.810333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, GetImageRangeFromBatch, GetImageSizeAndCount, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoraLoaderModelOnly, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417.json, 数字人/数字人/极速版数字人打造个人IP，视频生视频快速出片_2110886810279833601.json, 数字人/数字人/音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_159

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/infinite talk wan2.1｜音频趋动数字人一键生成_2092547920280252417.json、数字人/数字人/极速版数字人打造个人IP，视频生视频快速出片_2110886810279833601.json、数字人/数字人/音频驱动数字人｜infinite talk wan2.1说话口播直出_2092319386735570945.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
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
- `AudioSeparation` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `ColorMatch` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `AudioDuration_wan` —— 1/3 个有
- `H3ModeSwitch` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `SaveImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
