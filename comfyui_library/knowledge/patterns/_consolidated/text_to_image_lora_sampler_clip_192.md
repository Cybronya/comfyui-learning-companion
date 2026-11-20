---
name: text_to_image_lora_sampler_clip_192
type: Text To Image
frequency: 10
level: strong
coverage: 0.8946
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3参考生视频残影优化｜图生视频画质修复_2090455690967076865.json, 视频生成/图生视频/MinimaxH3故事板九宫格分镜-4步加速多参考图人物场景特效_2087363609331589121.json, 视频生成/图生视频/MinimaxH3海螺4步lightx2v加速lora-多重提速转场运镜图生视频_2087374035620556802.json, 视频生成/图生视频/i2v加速版直出｜Minimax H3文生图生视频场景特效_2092740361742536706.json, 视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json, 视频生成/图生视频/图生视频（支持首尾帧）3倍加速loraMinimaxH3-文生_2087432699580600321.json, 视频生成/图生视频/战斗特效图生视频｜MiniMax H3专用打斗镜头优化版_2089069191713353730.json, 视频生成/图生视频/战斗特效图生视频｜MiniMax H3战斗专用视频生成工作流_2088726129975840770.json, 视频生成/图生视频/残影优化｜MinimaxH3参考生视频画质修复直出_2090185681053245442.json, 视频生成/文生视频/Minimax H3文生视频残影优化｜文生视频画质修复_2090457027888898049.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_192

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3参考生视频残影优化｜图生视频画质修复_2090455690967076865.json、视频生成/图生视频/MinimaxH3故事板九宫格分镜-4步加速多参考图人物场景特效_2087363609331589121.json、视频生成/图生视频/MinimaxH3海螺4步lightx2v加速lora-多重提速转场运镜图生视频_2087374035620556802.json、视频生成/图生视频/i2v加速版直出｜Minimax H3文生图生视频场景特效_2092740361742536706.json、视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `SaveVideo` —— 7/10 个有
- `H3ExactRecover` —— 5/10 个有
- `H3InjectSchedule` —— 5/10 个有
- `H3JerkHeatmap` —— 5/10 个有
- `H3JerkOracle` —— 5/10 个有
- `H3TimeSmear` —— 5/10 个有
- `H3V2VInit` —— 5/10 个有
- `MiniMaxH3ImageToVideo` —— 5/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `MiniMaxH3ReferenceToVideo` —— 5/10 个有
- `Text Multiline` —— 5/10 个有
- `VAEEncode` —— 5/10 个有
- `VHS_VideoCombine` —— 5/10 个有
- `ModelPreviewOverrideKJ` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `H3AudioRecover` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
