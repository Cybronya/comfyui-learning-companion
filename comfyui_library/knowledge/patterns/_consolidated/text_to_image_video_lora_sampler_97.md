---
name: text_to_image_video_lora_sampler_97
type: Text To Image
frequency: 8
level: strong
coverage: 0.887
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3全自动长视频数字人工作流｜图生视频一站式出片_2101897607634317313.json, 视频生成/图生视频/单人加速版数字人MinimaxH3图生视频口播生成工作流_2088352533071876097.json, 视频生成/图生视频/单人加速版数字人图生视频｜MinimaxH3数字人工作流_2088319249872941058.json, 视频生成/图生视频/数字人MV视频生成｜音频驱动口型同步工作流_2094882855536128001.json, 视频生成/图生视频/音频加图片秒变口播数字人｜MinimaxH3 全节点注释_2096234556499259394.json, 视频生成/图生视频/音频图片生成口播数字人｜MinimaxH3全节点注释版_2095947201854918658.json, 视频生成/图生视频/音频驱动单人数字人｜MinimaxH3 lightx2v加速出片_2096243868416167937.json, 视频生成/图生视频/音频驱动数字人单人版｜MinimaxH3 lightx2v加速_2095947625072779266.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_97

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3全自动长视频数字人工作流｜图生视频一站式出片_2101897607634317313.json、视频生成/图生视频/单人加速版数字人MinimaxH3图生视频口播生成工作流_2088352533071876097.json、视频生成/图生视频/单人加速版数字人图生视频｜MinimaxH3数字人工作流_2088319249872941058.json、视频生成/图生视频/数字人MV视频生成｜音频驱动口型同步工作流_2094882855536128001.json、视频生成/图生视频/音频加图片秒变口播数字人｜MinimaxH3 全节点注释_2096234556499259394.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 7/8 个有
- `LoadAudio` —— 6/8 个有
- `LoadImage` —— 6/8 个有
- `ModelPreviewOverrideKJ` —— 6/8 个有
- `TrimAudioDuration` —— 6/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `SoundFlow_GetLength` —— 5/8 个有
- `PreviewAudio` —— 4/8 个有
- `AudioCrop` —— 2/8 个有
- `CR Text` —— 2/8 个有
- `SDVN Load Image Url` —— 2/8 个有
- `VHS_LoadAudio` —— 2/8 个有
- `AudioConcat` —— 1/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Float` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `ImageBatchMulti` —— 1/8 个有
- `MiniMaxH3AddGuide` —— 1/8 个有
- `MiniMaxH3SigmaShift` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
