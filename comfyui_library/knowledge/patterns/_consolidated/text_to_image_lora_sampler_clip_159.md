---
name: text_to_image_lora_sampler_clip_159
type: Text To Image
frequency: 11
level: strong
coverage: 0.889818
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/真人娃娃换装玩法｜MiniMax H3图生视频服装替换_2089062091096420353.json, 视频生成/图生视频/角色服装替换动作迁移视频方案 MinimaxH3 Easy全节点注释1080高画质_2093212762741764098.json, 视频生成/文生视频/4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081.json, 视频生成/文生视频/Easy多合一工作流｜MinimaxH3 全节点注释版_2089286157506007042.json, 视频生成/文生视频/H3六步文生视频短片预检版 开源加速采样工作流_2098840495605764097.json, 视频生成/文生视频/H3六步文生视频短片预检版｜六步走完从想法到成片_2099146163709628418.json, 视频生成/文生视频/MiniMax H3 Easy Hybrid全能参考极简多合一工作流，文生视频图生视频方案_2105737236565282818.json, 视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json, 视频生成/文生视频/Minimax H3开源加速版Lora6步直出1080P-文生视频短剧人物特效_2087379686644084738.json, 视频生成/文生视频/Minimax-H3加速一站式-文生视频图生视频工作流_2087399914660777986.json, 视频生成/文生视频/MinimaxH3完美优化版 生视频质量与速度双优_2104296777661902850.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/真人娃娃换装玩法｜MiniMax H3图生视频服装替换_2089062091096420353.json、视频生成/图生视频/角色服装替换动作迁移视频方案 MinimaxH3 Easy全节点注释1080高画质_2093212762741764098.json、视频生成/文生视频/4步lora加速版（批量短剧专用）Minimax_h3_导演台插件3.0万象AI_2085854413360558081.json、视频生成/文生视频/Easy多合一工作流｜MinimaxH3 全节点注释版_2089286157506007042.json、视频生成/文生视频/H3六步文生视频短片预检版 开源加速采样工作流_2098840495605764097.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3Easy` —— 10/11 个有
- `MiniMaxH3EasyLoader` —— 10/11 个有
- `MiniMaxH3EasyOutput` —— 10/11 个有
- `BasicScheduler` —— 9/11 个有
- `KSamplerSelect` —— 9/11 个有
- `CreateVideo` —— 7/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `SaveVideo` —— 7/11 个有
- `LoadImage` —— 5/11 个有
- `VHS_VideoCombine` —— 4/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `SaveImage` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `LoadVideo` —— 2/11 个有
- `MiniMaxH3EasyMediaLoader` —— 2/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `SFH3MultimodalDirector` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `SpectrumApplyMiniMaxH3` —— 1/11 个有
- `SpectrumSDXL` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
