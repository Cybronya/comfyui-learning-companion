---
name: text_to_image_video_lora_sampler_80
type: Text To Image
frequency: 9
level: strong
coverage: 0.847333
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PreviewAny, ResolutionSelector, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3 Selflift数字人三采｜角色一致画质再进阶_2103707327995138049.json, 视频生成/图生视频/Minimax H3 Selflift数字人｜口播带货数字人轻松做_2111136546035421186.json, 视频生成/图生视频/minimaxh3 Selflift数字人1080p｜超自然对口型图生视频_2100775766433816577.json, 视频生成/图生视频/短剧制作直出1080P最高质量版MMH3 Selflift工作流，图生视频方案_2106889115852689410.json, 视频生成/图生视频/短剧制作直出1080P最高质量版MMH3_Selflift工作流，图生视频方案_2109094089965789186.json, 视频生成/图生视频/短剧制作直出1080p最高质量版 MMH3 Selflift 视频生成优化_2109336160928616450.json, 视频生成/图生视频/短剧制作直出1080p最高质量版MMH3 Selflift 视频生成优化_2109762427930890242.json, 视频生成/文生视频/AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721.json, 视频生成/文生视频/AI音乐MV数字人新二采｜Minimax H3 Selflift联动出片_2100782399897554945.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 Selflift数字人三采｜角色一致画质再进阶_2103707327995138049.json、视频生成/图生视频/Minimax H3 Selflift数字人｜口播带货数字人轻松做_2111136546035421186.json、视频生成/图生视频/minimaxh3 Selflift数字人1080p｜超自然对口型图生视频_2100775766433816577.json、视频生成/图生视频/短剧制作直出1080P最高质量版MMH3 Selflift工作流，图生视频方案_2106889115852689410.json、视频生成/图生视频/短剧制作直出1080P最高质量版MMH3_Selflift工作流，图生视频方案_2109094089965789186.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PreviewAny`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `ModelPreviewOverrideKJ` —— 7/9 个有
- `ComfyNumberConvert` —— 5/9 个有
- `LTXVAudioVAEEncode` —— 5/9 个有
- `LTXVConcatAVLatent` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `SetLatentNoiseMask` —— 5/9 个有
- `SolidMask` —— 5/9 个有
- `SoundFlow_GetLength` —— 5/9 个有
- `TrimAudioDuration` —— 5/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `VAEDecodeAudio` —— 4/9 个有
- `Int` —— 2/9 个有
- `JWStringToFloat` —— 2/9 个有
- `QwenH3PromptLocal` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
