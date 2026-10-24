---
name: text_to_image_video_upscale_latent_upscale_8
type: Text To Image
frequency: 10
level: strong
coverage: 0.923
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax_H3人物替换LoRA版工作流，视频生视频人物替换处理工具_2108371023434436609.json, 视频生成/图生视频/MiniMax_H3双采样武戏专用文生图生多参首尾帧，文生视频图生视频方案_2109446019460190209.json, 视频生成/文生视频/MiniMax H3双采样武戏专用 文生图生多参首尾帧控制_2105108648811917314.json, 视频生成/文生视频/MiniMax H3双采样武戏专用多参首尾帧视频生成工具_2101361956228780033.json, 视频生成/文生视频/MiniMax H3双采样武戏专用文生图生多参首尾帧，文生视频图生视频方案_2107172340323930113.json, 视频生成/文生视频/MiniMax-H3双采样武戏专用｜文生图生多参首尾帧生成_2106966551298662401.json, 视频生成/文生视频/双采样武戏专用生成｜MiniMax-H3多参首尾帧_2095970956106887169.json, 视频生成/文生视频/文生图生多参首尾帧｜MiniMax-H3双采样武戏专用版_2101119158397267970.json, 视频生成/文生视频/武戏专用双采样文生图｜MiniMax-H3 多参首尾帧出片_2096261692538839041.json, 视频生成/视频生视频/MiniMax H3人物替换lora版_视频换人保持原动作_2106647464685170690.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_8

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3人物替换LoRA版工作流，视频生视频人物替换处理工具_2108371023434436609.json、视频生成/图生视频/MiniMax_H3双采样武戏专用文生图生多参首尾帧，文生视频图生视频方案_2109446019460190209.json、视频生成/文生视频/MiniMax H3双采样武戏专用 文生图生多参首尾帧控制_2105108648811917314.json、视频生成/文生视频/MiniMax H3双采样武戏专用多参首尾帧视频生成工具_2101361956228780033.json、视频生成/文生视频/MiniMax H3双采样武戏专用文生图生多参首尾帧，文生视频图生视频方案_2107172340323930113.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/10 个有
- `Fast Groups Bypasser (rgthree)` —— 8/10 个有
- `Int` —— 8/10 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 8/10 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 8/10 个有
- `PreviewAny` —— 8/10 个有
- `RH_Screenwriter` —— 8/10 个有
- `WujiH3PromptEnhancer` —— 8/10 个有
- `孤海注释` —— 8/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `easy promptConcat` —— 6/10 个有
- `LoraLoaderBypassModelOnly` —— 5/10 个有
- `SaveImage` —— 5/10 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 4/10 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 4/10 个有
- `WujiCleaner` —— 4/10 个有
- `CR Prompt Text` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `JWStringToFloat` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `EmptyImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
