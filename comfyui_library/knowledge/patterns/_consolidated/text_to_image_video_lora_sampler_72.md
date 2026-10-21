---
name: text_to_image_video_lora_sampler_72
type: Text To Image
frequency: 10
level: strong
coverage: 0.7795
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/自动提示词MV_4步加速版MinimaxH3音频驱动数字人_2085453705423446017.json, 视频生成/图生视频/自动提示词全能参考生视频REF2VA开源版MiniMax_2086806647741177857.json, 视频生成/图生视频/自定义歌曲MV视频生成｜MiniMax音频驱动图生视频直出_2091736922677932033.json, 视频生成/图生视频/自定义歌曲一键出片｜MiniMax MV音乐视频音频生成_2091752275076272130.json, 视频生成/图生视频/自定义歌曲音乐MV｜MiniMax音频图生视频生成工作流_2090222178607386626.json, 视频生成/文生视频/MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146.json, 视频生成/文生视频/MiniMax H3多参考工作流｜全接口开放内部开发版_2095279663810695169.json, 视频生成/文生视频/minimaxH3数字人音色参考｜音色克隆口播视频生成_2094942909484322818.json, 视频生成/文生视频/minimaxH3访谈类数字人｜口播访谈视频生成_2097949263094439937.json, 视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_72

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/自动提示词MV_4步加速版MinimaxH3音频驱动数字人_2085453705423446017.json、视频生成/图生视频/自动提示词全能参考生视频REF2VA开源版MiniMax_2086806647741177857.json、视频生成/图生视频/自定义歌曲MV视频生成｜MiniMax音频驱动图生视频直出_2091736922677932033.json、视频生成/图生视频/自定义歌曲一键出片｜MiniMax MV音乐视频音频生成_2091752275076272130.json、视频生成/图生视频/自定义歌曲音乐MV｜MiniMax音频图生视频生成工作流_2090222178607386626.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `GetNode` —— 8/10 个有
- `LoadAudio` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `MiniMaxH3SigmaShift` —— 7/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/10 个有
- `TrimAudioDuration` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `AudioCrop` —— 2/10 个有
- `ModelPreviewOverrideKJ` —— 2/10 个有
- `JWFloatToString` —— 1/10 个有
- `LoadVideoUI` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `RHLLMChatNode` —— 1/10 个有
- `Text` —— 1/10 个有
- `TextCombinerTwo` —— 1/10 个有
- `VHS_LoadAudioUpload` —— 1/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
