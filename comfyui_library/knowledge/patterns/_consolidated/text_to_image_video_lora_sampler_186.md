---
name: text_to_image_video_lora_sampler_186
type: Text To Image
frequency: 2
level: weak
coverage: 0.774
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, EnhancedLoadDiffusionModel, Fast Groups Bypasser (rgthree), KSampler, KSamplerAdvanced, LoadAudio, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanSoundImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1966350469507526658.json, 视频生成/图生视频/1966350469507526658.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_186

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1966350469507526658.json、视频生成/图生视频/1966350469507526658.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
