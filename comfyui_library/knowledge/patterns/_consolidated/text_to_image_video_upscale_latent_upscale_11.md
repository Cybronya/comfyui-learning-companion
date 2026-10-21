---
name: text_to_image_video_upscale_latent_upscale_11
type: Text To Image
frequency: 6
level: strong
coverage: 0.874333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/打斗场面高清呈现｜MinimaxH3武戏图生视频特效_2096524592583106561.json, 视频生成/图生视频/舞姿自动生成｜Minimax H3人物特效跳舞机_2096575779445497858.json, 视频生成/图生视频/跳舞自动机动作生成｜Minimax H3人物特效图生视频_2096316917907804162.json, 视频生成/文生视频/H3开源数字人口播带货 多图生视频电商内容制作_2098851175243280386.json, 视频生成/文生视频/MiniMax H3数字人视频带货 多图生视频口播工具_2098845262381932545.json, 视频生成/文生视频/MiniMaxH3数字人带货视频｜多图生视频批量产出带货素材_2099148701758484482.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/打斗场面高清呈现｜MinimaxH3武戏图生视频特效_2096524592583106561.json、视频生成/图生视频/舞姿自动生成｜Minimax H3人物特效跳舞机_2096575779445497858.json、视频生成/图生视频/跳舞自动机动作生成｜Minimax H3人物特效图生视频_2096316917907804162.json、视频生成/文生视频/H3开源数字人口播带货 多图生视频电商内容制作_2098851175243280386.json、视频生成/文生视频/MiniMax H3数字人视频带货 多图生视频口播工具_2098845262381932545.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `GetNode` —— 3/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `ModelAttentionBackend` —— 3/6 个有
- `ModelPreviewOverrideKJ` —— 3/6 个有
- `RHHiddenNodes` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `SplitSigmas` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `DF_Get_image_size` —— 1/6 个有
- `FlashVSR_SM_KSampler` —— 1/6 个有
- `FlashVSR_SM_Model` —— 1/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `Text` —— 1/6 个有
- `VideoCombineV2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
