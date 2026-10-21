---
name: text_to_image_video_lora_sampler_157
type: Text To Image
frequency: 4
level: strong
coverage: 0.79825
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, PrimitiveFloat, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MinimaxH3全能参考VDN一采｜文生视频多模式生成_2097108523267219458.json, 视频生成/文生视频/minimax8步工作流｜视频二创换角色换场景｜动作运镜全保留_2101853028855930882.json, 视频生成/文生视频/双时钟8步高质量极速多参V1｜Minimax文生图生视频生视频工作流_2087188424548769794.json, 视频生成/视频生视频/MiniMax_H3视频复刻加速版_数字人参考生视频与长视频直出工作流_2106181004804317185.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3全能参考VDN一采｜文生视频多模式生成_2097108523267219458.json、视频生成/文生视频/minimax8步工作流｜视频二创换角色换场景｜动作运镜全保留_2101853028855930882.json、视频生成/文生视频/双时钟8步高质量极速多参V1｜Minimax文生图生视频生视频工作流_2087188424548769794.json、视频生成/视频生视频/MiniMax_H3视频复刻加速版_数字人参考生视频与长视频直出工作流_2106181004804317185.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `MiniMaxH3AVDecodeT8` —— 3/4 个有
- `RandomNoise` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `LoraLoaderBypassModelOnly` —— 2/4 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `SolAttnMiniMax` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MiniMaxH3PDD8StepSetupT8Advanced` —— 1/4 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/4 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RandomSeedNoise` —— 1/4 个有
- `VAEDecodeAudio` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
