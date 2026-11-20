---
name: unknown_workflow_video_sampler_clip_154
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94125
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, ImageConcanate, KSampler, LoadAudio, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSoundImageToVideo, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Comfyui官方S2V工作流_1960718130144325634.json, 视频生成/图生视频/Wan2.2-S2V-音频驱动的视频生成 官方流_1960878443531579394.json, 视频生成/图生视频/对口型wan2.2_S2V图片视频对口型_1960877190416142337.json, 视频生成/图生视频/🥳wan2.2 S2V 超稳定数字人生成【姿态迁移版】【超级加速版】🥳_1961973337251627010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_154

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Comfyui官方S2V工作流_1960718130144325634.json、视频生成/图生视频/Wan2.2-S2V-音频驱动的视频生成 官方流_1960878443531579394.json、视频生成/图生视频/对口型wan2.2_S2V图片视频对口型_1960877190416142337.json、视频生成/图生视频/🥳wan2.2 S2V 超稳定数字人生成【姿态迁移版】【超级加速版】🥳_1961973337251627010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageConcanate`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `TorchCompileModel` —— 3/4 个有
- `Audio Duration (mtb)` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `Float` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `Int` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `RH_GetAudioDuration` —— 2/4 个有
- `ToInt` —— 2/4 个有
- `easy convertAnything` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `AudioCrop` —— 1/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `ImageScaleToMegapixels` —— 1/4 个有
- `JWIntegerToString` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 4 | 69% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 4 | 54% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，4 个样本
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
