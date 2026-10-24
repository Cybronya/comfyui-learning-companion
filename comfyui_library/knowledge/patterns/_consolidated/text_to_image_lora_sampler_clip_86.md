---
name: text_to_image_lora_sampler_clip_86
type: Text To Image
frequency: 15
level: strong
coverage: 0.910933
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/真人娃娃换装玩法｜MiniMax H3图生视频服装替换_2089062091096420353.json, 视频生成/图生视频/角色服装替换动作迁移视频方案 MinimaxH3 Easy全节点注释1080高画质_2093212762741764098.json, 视频生成/文生视频/5秒1080p仅8分钟｜MiniMax-H3图生视频全节点注释版_2093768843360563202.json, 视频生成/文生视频/5秒1080p只要8分钟｜MiniMax-H3图生视频全节点注释_2094005447392063489.json, 视频生成/文生视频/5秒1080p文生视频8分钟出片 MiniMax-H3 全节点注释_2094187651468455937.json, 视频生成/文生视频/8步增速全节点注释｜Minimax H3图生视频文生视频视频生视频_2088775119333318657.json, 视频生成/文生视频/8步增速全节点注释｜Minimax H3图生视频视频生视频提速_2089016657074278401.json, 视频生成/文生视频/8步增速全节点注释｜Minimax H3图生视频视频生视频提速版_2089684868778250242.json, 视频生成/文生视频/Easy多合一工作流｜MinimaxH3 全节点注释版_2089286157506007042.json, 视频生成/文生视频/Minimax H3开源加速版Lora6步直出1080P-文生视频短剧人物特效_2087379686644084738.json, 视频生成/文生视频/Minimax H3提速全节点注释｜8步增速图生视频视频生视频_2089374494271041537.json, 视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json, 视频生成/文生视频/SageAttention+LoRA双重加速｜MiniMax H3文生视频_2089404463130963970.json, 视频生成/文生视频/图生视频5秒1080p｜MiniMax-H3八分钟全节点注释_2090913102907920385.json, 视频生成/文生视频/海螺Minimax H3开源版文生视频H3加速Lora6步直出1080P_2086443392405430273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/真人娃娃换装玩法｜MiniMax H3图生视频服装替换_2089062091096420353.json、视频生成/图生视频/角色服装替换动作迁移视频方案 MinimaxH3 Easy全节点注释1080高画质_2093212762741764098.json、视频生成/文生视频/5秒1080p仅8分钟｜MiniMax-H3图生视频全节点注释版_2093768843360563202.json、视频生成/文生视频/5秒1080p只要8分钟｜MiniMax-H3图生视频全节点注释_2094005447392063489.json、视频生成/文生视频/5秒1080p文生视频8分钟出片 MiniMax-H3 全节点注释_2094187651468455937.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 14/15 个有
- `CreateVideo` —— 13/15 个有
- `SaveVideo` —— 13/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/15 个有
- `BasicScheduler` —— 10/15 个有
- `CR Text` —— 10/15 个有
- `ComfyMathExpression` —— 10/15 个有
- `KSamplerSelect` —— 10/15 个有
- `LoadImage` —— 10/15 个有
- `MiniMaxH3ImageToVideo` —— 10/15 个有
- `ResolutionSelector` —— 10/15 个有
- `PathchSageAttentionKJ` —— 7/15 个有
- `LoraLoaderBypassModelOnly` —— 6/15 个有
- `PrimitiveFloat` —— 6/15 个有
- `MiniMaxH3Easy` —— 5/15 个有
- `MiniMaxH3EasyLoader` —— 5/15 个有
- `MiniMaxH3EasyOutput` —— 5/15 个有
- `EasyCache` —— 4/15 个有
- `Int` —— 4/15 个有
- `MiniMaxH3DualClockSamplerT8` —— 4/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `MiniMaxH3SigmaShift` —— 2/15 个有
- `VHS_VideoCombine` —— 2/15 个有
- `LoadVideo` —— 1/15 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/15 个有
- `SpectrumSDXL` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（18/15 个样本）：Steps较低可能导致细节不足
