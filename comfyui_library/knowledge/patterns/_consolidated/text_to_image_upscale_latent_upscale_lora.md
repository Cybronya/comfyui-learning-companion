---
name: text_to_image_upscale_latent_upscale_lora
type: Text To Image
frequency: 15
level: strong
coverage: 0.581533
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json, 视频生成/图生视频/MiniMax H3 Turbo V4｜Realism真人写实参考生视频｜超写实图生视频流_2108004956178567169.json, 视频生成/图生视频/MiniMax H3 多参考生视频 720p｜一采快二采质量高支持特效_2096841455523422209.json, 视频生成/图生视频/MiniMax H3动作迁移2.0史诗强化进阶版，视频生视频动态姿势迁移工具_2103188261547102209.json, 视频生成/图生视频/MiniMax H3动作迁移9分钟出视频，图生视频视频生视频高效产出方案_2103599685733801986.json, 视频生成/图生视频/MiniMax H3动作迁移9分钟出视频，图生视频视频生视频高效产出方案_2103930965801398273.json, 视频生成/图生视频/MiniMax H3多参生视频优化版｜9图3音3视频参考_2095604235936292865.json, 视频生成/图生视频/MiniMax H3多参考生视频 快速高质量图生视频_2098830853072834562.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版 高质量图生视频_2098861196861595649.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版｜多图融合一致性出片更稳｜图生视频_2099105339022073857.json, 视频生成/图生视频/Minimax H3多参考双采｜最强一致性Singularity出视频_2101538998190698498.json, 视频生成/文生视频/H3二采去油不爆音加速工作流 视频生成处理_2100647828073832450.json, 视频生成/文生视频/MiniMax H3 二采加速｜多参考图生视频效率翻倍实用工作流_2097500273798369281.json, 视频生成/文生视频/MiniMax H3二采去油不爆音加速工作流，文生视频图生视频制作级方案_2103555034809192449.json, 视频生成/文生视频/MiniMax H3二采去油不爆音加速工作流｜视频生视频不糊脸，音画同步更高级_2100506185672781826.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json、视频生成/图生视频/MiniMax H3 Turbo V4｜Realism真人写实参考生视频｜超写实图生视频流_2108004956178567169.json、视频生成/图生视频/MiniMax H3 多参考生视频 720p｜一采快二采质量高支持特效_2096841455523422209.json、视频生成/图生视频/MiniMax H3动作迁移2.0史诗强化进阶版，视频生视频动态姿势迁移工具_2103188261547102209.json、视频生成/图生视频/MiniMax H3动作迁移9分钟出视频，图生视频视频生视频高效产出方案_2103599685733801986.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `VHS_LoadVideo` —— 14/15 个有
- `easy float` —— 14/15 个有
- `Text` —— 12/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/15 个有
- `VHS_VideoCombine` —— 10/15 个有
- `ModelAttentionBackend` —— 7/15 个有
- `SaveImage` —— 7/15 个有
- `CreateVideo` —— 6/15 个有
- `Fast Groups Bypasser (rgthree)` —— 6/15 个有
- `SaveVideo` —— 6/15 个有
- `MiniMaxChunkFeedForward` —— 4/15 个有
- `MiniMaxH3TurboSampler` —— 4/15 个有
- `MiniMaxLowVRAMAttention` —— 4/15 个有
- `easy cleanGpuUsed` —— 3/15 个有
- `Lora Loader Stack (rgthree)` —— 2/15 个有
- `SolAttnMiniMax` —— 2/15 个有
- `Text Multiline` —— 2/15 个有
- `easy loraStack` —— 2/15 个有
- `easy loraStackApply` —— 2/15 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/15 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 1/15 个有
- `MiniMaxH3SigmaShift` —— 1/15 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 1/15 个有
- `PixaromaSaveMp4` —— 1/15 个有
- `SigmasToFloat` —— 1/15 个有
- `忽略多组孤海` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
