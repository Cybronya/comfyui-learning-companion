---
name: unknown_workflow_lora_sampler_clip_237
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.915333
common_nodes: [1hew_AudioDuration, AudioConcat, AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyAudio, INTConstant, ImageFromBatch, IndexTTS2Run, KSampler, LatentConcat, LatentCut, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, ModelSamplingSD3, MuyeTextEditOutput, PrimitiveFloat, PrimitiveInt, SaveAudio, SaveVideo, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, Video Slice, WanSoundImageToVideo, WanSoundImageToVideoExtend, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/【口播数字人】一体化长音频_零漂移_全自动片长_10段_V3版_2110271661361680386.json, 视频生成/图生视频/【口播数字人】一体化长音频_零漂移_全自动片长_10段_V3版_2111044721744367618.json, 视频生成/图生视频/【口播数字人】一体化长音频_零漂移_全自动片长_10段_V3版_2111055125790937090.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_237

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【口播数字人】一体化长音频_零漂移_全自动片长_10段_V3版_2110271661361680386.json、视频生成/图生视频/【口播数字人】一体化长音频_零漂移_全自动片长_10段_V3版_2111044721744367618.json、视频生成/图生视频/【口播数字人】一体化长音频_零漂移_全自动片长_10段_V3版_2111055125790937090.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `1hew_AudioDuration`
- `AudioConcat`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyAudio`
- `INTConstant`
- `ImageFromBatch`
- `IndexTTS2Run`
- `KSampler`
- `LatentConcat`
- `LatentCut`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `MuyeTextEditOutput`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveAudio`
- `SaveVideo`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `Video Slice`
- `WanSoundImageToVideo`
- `WanSoundImageToVideoExtend`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（30/3 个样本）：Steps较低可能导致细节不足
