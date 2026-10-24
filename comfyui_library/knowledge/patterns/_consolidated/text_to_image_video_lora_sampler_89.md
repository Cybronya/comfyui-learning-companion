---
name: text_to_image_video_lora_sampler_89
type: Text To Image
frequency: 9
level: strong
coverage: 0.741667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/自动提示词MV_4步加速版MinimaxH3音频驱动数字人_2085453705423446017.json, 视频生成/图生视频/自动提示词全能参考生视频REF2VA开源版MiniMax_2086806647741177857.json, 视频生成/图生视频/自定义歌曲MV视频生成｜MiniMax音频驱动图生视频直出_2091736922677932033.json, 视频生成/图生视频/自定义歌曲一键出片｜MiniMax MV音乐视频音频生成_2091752275076272130.json, 视频生成/图生视频/自定义歌曲音乐MV｜MiniMax音频图生视频生成工作流_2090222178607386626.json, 视频生成/图生视频/超级加速多图参考生视频｜Minimax_h3角色一致性角色表演工作流_2087208437443809281.json, 视频生成/文生视频/Fastvideo H3快速文生视频｜ComfyUI加速生成_2095222013941080065.json, 视频生成/文生视频/图MiniMax文生视频视频生视频图生视频_2085849570684260354.json, 视频生成/文生视频/快速文生视频｜Fastvideo H3角色表演ComfyUI工作流_2095559517340790785.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_89

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/自动提示词MV_4步加速版MinimaxH3音频驱动数字人_2085453705423446017.json、视频生成/图生视频/自动提示词全能参考生视频REF2VA开源版MiniMax_2086806647741177857.json、视频生成/图生视频/自定义歌曲MV视频生成｜MiniMax音频驱动图生视频直出_2091736922677932033.json、视频生成/图生视频/自定义歌曲一键出片｜MiniMax MV音乐视频音频生成_2091752275076272130.json、视频生成/图生视频/自定义歌曲音乐MV｜MiniMax音频图生视频生成工作流_2090222178607386626.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
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
- `PrimitiveFloat` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `VAEDecodeAudio` —— 8/9 个有
- `LoadImage` —— 7/9 个有
- `MiniMaxH3ReferenceToVideo` —— 7/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `GetNode` —— 6/9 个有
- `MiniMaxH3SigmaShift` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `LoadAudio` —— 3/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/9 个有
- `TrimAudioDuration` —— 3/9 个有
- `MiniMaxH3ImageToVideo` —— 2/9 个有
- `StringConcatenate` —— 2/9 个有
- `Text` —— 2/9 个有
- `JWFloatToString` —— 1/9 个有
- `LoadVideoUI` —— 1/9 个有
- `PainterVRAM` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `RHLLMChatNode` —— 1/9 个有
- `TextCombinerTwo` —— 1/9 个有
- `VHS_LoadAudioUpload` —— 1/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
