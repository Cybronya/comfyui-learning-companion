---
name: text_to_image_lora_sampler_clip_152
type: Text To Image
frequency: 8
level: strong
coverage: 0.89975
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3参考生视频残影优化｜图生视频画质修复_2090455690967076865.json, 视频生成/图生视频/三图multi_ref参考生成｜minimax h3 i2v视频_2094928789578014722.json, 视频生成/图生视频/三图参考生视频｜multi_ref_minimax_h3_i2v生成_2095108277595099138.json, 视频生成/图生视频/战斗特效图生视频｜MiniMax H3专用打斗镜头优化版_2089069191713353730.json, 视频生成/图生视频/战斗特效图生视频｜MiniMax H3战斗专用视频生成工作流_2088726129975840770.json, 视频生成/图生视频/残影优化｜MinimaxH3参考生视频画质修复直出_2090185681053245442.json, 视频生成/文生视频/MiniMax-4步加速工作流文生视频视频生视频图生视频_2085455891675049986.json, 视频生成/文生视频/Minimax H3文生视频残影优化｜文生视频画质修复_2090457027888898049.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_152

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3参考生视频残影优化｜图生视频画质修复_2090455690967076865.json、视频生成/图生视频/三图multi_ref参考生成｜minimax h3 i2v视频_2094928789578014722.json、视频生成/图生视频/三图参考生视频｜multi_ref_minimax_h3_i2v生成_2095108277595099138.json、视频生成/图生视频/战斗特效图生视频｜MiniMax H3专用打斗镜头优化版_2089069191713353730.json、视频生成/图生视频/战斗特效图生视频｜MiniMax H3战斗专用视频生成工作流_2088726129975840770.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

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
- `LoadImage` —— 7/8 个有
- `MiniMaxH3ReferenceToVideo` —— 7/8 个有
- `VHS_VideoCombine` —— 7/8 个有
- `CreateVideo` —— 6/8 个有
- `H3ExactRecover` —— 5/8 个有
- `H3InjectSchedule` —— 5/8 个有
- `H3JerkHeatmap` —— 5/8 个有
- `H3JerkOracle` —— 5/8 个有
- `H3TimeSmear` —— 5/8 个有
- `H3V2VInit` —— 5/8 个有
- `Text Multiline` —— 5/8 个有
- `VAEEncode` —— 5/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `PainterVRAM` —— 2/8 个有
- `YK_LoadImageFromURL` —— 2/8 个有
- `H3AudioRecover` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有

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
