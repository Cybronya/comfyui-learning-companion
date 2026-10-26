---
name: text_to_image_lora_sampler_clip_143
type: Text To Image
frequency: 12
level: strong
coverage: 0.904167
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/真人娃娃换装玩法｜MiniMax H3图生视频服装替换_2089062091096420353.json, 视频生成/图生视频/角色服装替换动作迁移视频方案 MinimaxH3 Easy全节点注释1080高画质_2093212762741764098.json, 视频生成/文生视频/5秒1080p仅8分钟｜MiniMax-H3图生视频全节点注释版_2093768843360563202.json, 视频生成/文生视频/5秒1080p只要8分钟｜MiniMax-H3图生视频全节点注释_2094005447392063489.json, 视频生成/文生视频/5秒1080p文生视频8分钟出片 MiniMax-H3 全节点注释_2094187651468455937.json, 视频生成/文生视频/8步加速文生视频｜minimax_h3文字生成视频工作流_2088367583484538882.json, 视频生成/文生视频/8步增速全节点注释｜Minimax H3图生视频文生视频视频生视频_2088775119333318657.json, 视频生成/文生视频/8步增速全节点注释｜Minimax H3图生视频视频生视频提速_2089016657074278401.json, 视频生成/文生视频/8步增速全节点注释｜Minimax H3图生视频视频生视频提速版_2089684868778250242.json, 视频生成/文生视频/Easy多合一工作流｜MinimaxH3 全节点注释版_2089286157506007042.json, 视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json, 视频生成/文生视频/MiniMax H3多合一Turbo4 Sage T8 Stable-R2V Turbo6 EXP二_2087347142024327170.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/真人娃娃换装玩法｜MiniMax H3图生视频服装替换_2089062091096420353.json、视频生成/图生视频/角色服装替换动作迁移视频方案 MinimaxH3 Easy全节点注释1080高画质_2093212762741764098.json、视频生成/文生视频/5秒1080p仅8分钟｜MiniMax-H3图生视频全节点注释版_2093768843360563202.json、视频生成/文生视频/5秒1080p只要8分钟｜MiniMax-H3图生视频全节点注释_2094005447392063489.json、视频生成/文生视频/5秒1080p文生视频8分钟出片 MiniMax-H3 全节点注释_2094187651468455937.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `孤海注释` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `LoadImage` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `ComfyMathExpression` —— 9/12 个有
- `ResolutionSelector` —— 9/12 个有
- `BasicScheduler` —— 8/12 个有
- `CR Text` —— 8/12 个有
- `KSamplerSelect` —— 8/12 个有
- `MiniMaxH3ImageToVideo` —— 8/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/12 个有
- `PathchSageAttentionKJ` —— 6/12 个有
- `PrimitiveFloat` —— 6/12 个有
- `EasyCache` —— 4/12 个有
- `LoraLoaderBypassModelOnly` —— 4/12 个有
- `MiniMaxH3DualClockSamplerT8` —— 4/12 个有
- `Int` —— 3/12 个有
- `MiniMaxH3Easy` —— 3/12 个有
- `MiniMaxH3EasyLoader` —— 3/12 个有
- `MiniMaxH3EasyOutput` —— 3/12 个有
- `PrimitiveStringMultiline` —— 3/12 个有
- `LoadVideo` —— 2/12 个有
- `MiniMaxH3ReferenceToVideo` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `ComfySwitchNode` —— 1/12 个有
- `GetVideoComponents` —— 1/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `LoadAudio` —— 1/12 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/12 个有
- `PT_H3ConcatAVLatent` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `SpectrumSDXL` —— 1/12 个有
- `VAEEncode` —— 1/12 个有
- `VAEEncodeAudio` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（14/12 个样本）：Steps较低可能导致细节不足
