---
name: text_to_image_lora_sampler_clip_286
type: Text To Image
frequency: 7
level: strong
coverage: 0.908714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax-H3 4步加速单图参考二次采样｜官方节点版文生视频图生视频_2090411973430304769.json, 视频生成/文生视频/剑斗多参模式视频生成｜战斗动作多参考一致性_2094543565945921538.json, 视频生成/文生视频/双采首尾帧战斗模式｜文生图生视频特效生成_2094783307044188162.json, 视频生成/文生视频/多参模式剑斗生成｜文生图生视频战斗特效工作流_2094789270803410946.json, 视频生成/文生视频/战斗双采首尾帧模式｜文生视频特效视频生成_2094537849541578753.json, 视频生成/文生视频/打斗强化三件套｜MiniMax_H3二采+打斗lora+动作修复_2092876212183068673.json, 视频生成/文生视频/打斗强化二采修复｜MiniMax H3打斗lora文生图生视频_2092687490728681474.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_286

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3 4步加速单图参考二次采样｜官方节点版文生视频图生视频_2090411973430304769.json、视频生成/文生视频/剑斗多参模式视频生成｜战斗动作多参考一致性_2094543565945921538.json、视频生成/文生视频/双采首尾帧战斗模式｜文生图生视频特效生成_2094783307044188162.json、视频生成/文生视频/多参模式剑斗生成｜文生图生视频战斗特效工作流_2094789270803410946.json、视频生成/文生视频/战斗双采首尾帧模式｜文生视频特效视频生成_2094537849541578753.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DisableNoise` —— 6/7 个有
- `ExtendIntermediateSigmas` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `SplitSigmasDenoise` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 5/7 个有
- `LTXVConcatAVLatent` —— 2/7 个有
- `LTXVSeparateAVLatent` —— 2/7 个有
- `MiniMaxH3ImageToVideo` —— 2/7 个有
- `MinimaxH3LatentUpscaler3D` —— 2/7 个有
- `EasyCache` —— 1/7 个有
- `Float` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `PT_H3ConcatAVLatent` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有
- `Text` —— 1/7 个有
- `VAEEncode` —— 1/7 个有
- `VAEEncodeAudio` —— 1/7 个有
- `VRAMReserver` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
