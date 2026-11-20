---
name: image_to_image_video_lora_sampler_25
type: Image To Image
frequency: 2
level: weak
coverage: 0.9305
common_nodes: [Any Switch (rgthree), AudioToFPS, CLIPLoader, ComfyMathExpression, ComfySwitchNode, ConditioningZeroOut, EmptyImage, Fast Muter (rgthree), FloatConstant, GetImageSize, INTConstant, ImageResizeKJv2, KSampler, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, Mute / Bypass Repeater (rgthree), PT_H3ConcatAVLatent, PrimitiveBoolean, Text Multiline, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MINIMAX H3 音频驱动双采数字人_2088680630900056065.json, 视频生成/文生视频/豹豹喵呜制作：音频驱动双采数字人_2088557539976892417.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MINIMAX H3 音频驱动双采数字人_2088680630900056065.json、视频生成/文生视频/豹豹喵呜制作：音频驱动双采数字人_2088557539976892417.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AudioToFPS`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyImage`
- `Fast Muter (rgthree)`
- `FloatConstant`
- `GetImageSize`
- `INTConstant`
- `ImageResizeKJv2`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `Mute / Bypass Repeater (rgthree)`
- `PT_H3ConcatAVLatent`
- `PrimitiveBoolean`
- `Text Multiline`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.2 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
