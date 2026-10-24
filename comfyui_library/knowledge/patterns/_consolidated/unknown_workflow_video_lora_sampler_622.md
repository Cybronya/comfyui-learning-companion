---
name: unknown_workflow_video_lora_sampler_622
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [AudioCrop, AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, Display Int (rgthree), ImageResizeKJv2, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveAudio, SimpleMath+, SoundFlow_GetLength, ToInt, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanSoundImageToVideo, easy cleanGpuUsed, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/S2V 声音生成视频 Wan2.2_1967070568195481602.json, 视频生成/图生视频/WAN 2.2-S2V 声音+图像 生成视频_1972914336614273026.json, 视频生成/图生视频/WAN 2.2-S2V 声音+图像 生成视频_1983404597886787585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_622

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/S2V 声音生成视频 Wan2.2_1967070568195481602.json、视频生成/图生视频/WAN 2.2-S2V 声音+图像 生成视频_1972914336614273026.json、视频生成/图生视频/WAN 2.2-S2V 声音+图像 生成视频_1983404597886787585.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `Display Int (rgthree)`
- `ImageResizeKJv2`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveAudio`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `ToInt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Text` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
