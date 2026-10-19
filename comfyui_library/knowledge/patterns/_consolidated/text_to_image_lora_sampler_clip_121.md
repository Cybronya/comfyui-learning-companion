---
name: text_to_image_lora_sampler_clip_121
type: Text To Image
frequency: 8
level: strong
coverage: 0.860125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/fl2v_turbo加速｜MiniMax-H3图生视频文生视频提速_2089412676161204225.json, 视频生成/文生视频/h3文生_首尾帧视频_2087479552833576961.json, 视频生成/文生视频/lightx2v文生图生首尾帧加速-minimax_h3工作流_2087348521795153921.json, 视频生成/文生视频/minmaxH3单采加速｜文生视频图生视频 极速出片小钢炮_2105529286273880065.json, 视频生成/文生视频/一键工作流战斗特效｜文生视频图生视频工作流_2088376043441844226.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3视频生成直出_2092021354127253506.json, 视频生成/文生视频/全模态多参考视频生成｜MiniMax H3时间线控制+独立音频_2091205063564943362.json, 视频生成/文生视频/全系列增速工作流Minimax文生视频视频生视频图生视频_2087333816103948290.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_121

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/fl2v_turbo加速｜MiniMax-H3图生视频文生视频提速_2089412676161204225.json、视频生成/文生视频/h3文生_首尾帧视频_2087479552833576961.json、视频生成/文生视频/lightx2v文生图生首尾帧加速-minimax_h3工作流_2087348521795153921.json、视频生成/文生视频/minmaxH3单采加速｜文生视频图生视频 极速出片小钢炮_2105529286273880065.json、视频生成/文生视频/一键工作流战斗特效｜文生视频图生视频工作流_2088376043441844226.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `MiniMaxH3ImageToVideo` —— 5/8 个有
- `MiniMaxH3ReferenceToVideo` —— 4/8 个有
- `LoadAudio` —— 3/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `CR Float To Integer` —— 1/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetVideoComponents` —— 1/8 个有
- `LoadVideo` —— 1/8 个有
- `MiniMaxH3SigmaShift` —— 1/8 个有
- `MiniMaxH3TurboLoRA` —— 1/8 个有
- `MiniMaxH3TurboSampler` —— 1/8 个有
- `ModelAttentionBackend` —— 1/8 个有
- `PixaromaDuration` —— 1/8 个有
- `PixaromaSizes` —— 1/8 个有
- `UniBlockSwap` —— 1/8 个有
- `VRAMReserver` —— 1/8 个有
- `忽略多组孤海` —— 1/8 个有

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
