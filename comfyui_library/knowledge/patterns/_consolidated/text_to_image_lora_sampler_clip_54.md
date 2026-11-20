---
name: text_to_image_lora_sampler_clip_54
type: Text To Image
frequency: 17
level: strong
coverage: 0.887235
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速工作流多图参考短剧制作Minimax_H3图生视频_2088378063548669954.json, 视频生成/图生视频/动漫转真人指定人物｜H3图生视频一键生成直出_2093465253832126465.json, 视频生成/图生视频/单人加速版数字人MinimaxH3图生视频口播生成工作流_2088352533071876097.json, 视频生成/图生视频/单人加速版数字人图生视频｜MinimaxH3数字人工作流_2088319249872941058.json, 视频生成/图生视频/单图参考加参考音｜Minimax H3图生视频生成_2093782725252706305.json, 视频生成/图生视频/单图参考无参考音｜Minimax H3图生视频工作流_2094012813646852097.json, 视频生成/图生视频/单图参考无参考音｜Minimax H3图生视频直出_2093784039185543170.json, 视频生成/图生视频/参考图+参考音频｜MiniMax H3 4步生视频直出_2090936385749475330.json, 视频生成/图生视频/参考模式10步+3步｜H3 Latent Upscaler图生视频_2090888594817900545.json, 视频生成/图生视频/双图参考+1参考音｜Minimax H3批量管理系统api用_2094010898447945730.json, 视频生成/图生视频/双图参考+2参考音｜Minimax H3音画同参图生视频生成_2089444909353889793.json, 视频生成/图生视频/双图参考加参考音｜Minimax H3批量管理系统API版_2093778584715481089.json, 视频生成/图生视频/数字人MV视频生成｜音频驱动口型同步工作流_2094882855536128001.json, 视频生成/图生视频/音频加图片秒变口播数字人｜MinimaxH3 全节点注释_2096234556499259394.json, 视频生成/图生视频/音频图片生成口播数字人｜MinimaxH3全节点注释版_2095947201854918658.json, 视频生成/图生视频/音频驱动单人数字人｜MinimaxH3 lightx2v加速出片_2096243868416167937.json, 视频生成/图生视频/音频驱动数字人单人版｜MinimaxH3 lightx2v加速_2095947625072779266.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/加速工作流多图参考短剧制作Minimax_H3图生视频_2088378063548669954.json、视频生成/图生视频/动漫转真人指定人物｜H3图生视频一键生成直出_2093465253832126465.json、视频生成/图生视频/单人加速版数字人MinimaxH3图生视频口播生成工作流_2088352533071876097.json、视频生成/图生视频/单人加速版数字人图生视频｜MinimaxH3数字人工作流_2088319249872941058.json、视频生成/图生视频/单图参考加参考音｜Minimax H3图生视频生成_2093782725252706305.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 16/17 个有
- `BasicScheduler` —— 16/17 个有
- `KSamplerSelect` —— 16/17 个有
- `VHS_VideoCombine` —— 16/17 个有
- `LoadImage` —— 15/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/17 个有
- `PrimitiveStringMultiline` —— 14/17 个有
- `LoadAudio` —— 11/17 个有
- `VAEDecodeAudio` —— 10/17 个有
- `MiniMaxH3SigmaShift` —— 8/17 个有
- `ModelAttentionBackend` —— 8/17 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 7/17 个有
- `INTConstant` —— 6/17 个有
- `ModelPreviewOverrideKJ` —— 6/17 个有
- `SoundFlow_GetLength` —— 5/17 个有
- `TrimAudioDuration` —— 5/17 个有
- `PreviewAudio` —— 3/17 个有
- `AudioCrop` —— 2/17 个有
- `CR Text` —— 2/17 个有
- `CreateVideo` —— 2/17 个有
- `SDVN Load Image Url` —— 2/17 个有
- `SaveVideo` —— 2/17 个有
- `VHS_LoadAudio` —— 2/17 个有
- `CFGGuider` —— 1/17 个有
- `ConditioningZeroOut` —— 1/17 个有
- `ManualSigmas` —— 1/17 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/17 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/17 个有
- `PlaySound|pysssss` —— 1/17 个有
- `SplitSigmas` —— 1/17 个有
- `Text` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
