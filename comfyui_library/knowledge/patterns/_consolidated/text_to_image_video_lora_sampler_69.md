---
name: text_to_image_video_lora_sampler_69
type: Text To Image
frequency: 11
level: strong
coverage: 0.784818
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多参考图生视频4步加速｜MiniMax H3提示词自动优化美少女_2091298868020473857.json, 视频生成/图生视频/首尾帧EMinimax_H3_NG海螺图生视频_2087147808825626625.json, 视频生成/图生视频/首尾帧加速版｜MiniMaxH3开源图生视频直出_2089828334866882562.json, 视频生成/图生视频/首尾帧生视频｜海螺Minimax_H3图生视频生成_2092176988864864257.json, 视频生成/文生视频/768P去油双时钟｜Lightx2v 8步Minimax文生视频加速_2093729420728168450.json, 视频生成/文生视频/H3-最优加速工作流文生视频图生视频_2085853717911400449.json, 视频生成/文生视频/H3全能多参提示词优化｜4步加速文生视频图生视频_2089386017529880578.json, 视频生成/文生视频/MiniMax H3 全能参考_自动提示词_2085967794637729794.json, 视频生成/文生视频/MiniMaxH3加速版尾帧做参考｜4步加速 文生视频视频生视频快出片_2104097352675057665.json, 视频生成/文生视频/全能多参考｜H3 4步加速生视频 提示词自动优化 文生图生视频生_2089331197225820161.json, 视频生成/文生视频/尾帧参考4步加速 MiniMaxH3极速生视频省时方案_2104330470908579842.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_69

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/多参考图生视频4步加速｜MiniMax H3提示词自动优化美少女_2091298868020473857.json、视频生成/图生视频/首尾帧EMinimax_H3_NG海螺图生视频_2087147808825626625.json、视频生成/图生视频/首尾帧加速版｜MiniMaxH3开源图生视频直出_2089828334866882562.json、视频生成/图生视频/首尾帧生视频｜海螺Minimax_H3图生视频生成_2092176988864864257.json、视频生成/文生视频/768P去油双时钟｜Lightx2v 8步Minimax文生视频加速_2093729420728168450.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `PrimitiveStringMultiline` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `JoinStringMulti` —— 6/11 个有
- `LoadAudio` —— 6/11 个有
- `MiniMaxH3AVDecodeT8` —— 6/11 个有
- `MiniMaxH3AudioConditioningT8` —— 6/11 个有
- `StringConcatenate` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `llama_cpp_instruct_adv` —— 6/11 个有
- `llama_cpp_model_loader` —— 6/11 个有
- `llama_cpp_parameters` —— 6/11 个有
- `Any Switch (rgthree)` —— 5/11 个有
- `BasicScheduler` —— 5/11 个有
- `GetNode` —— 5/11 个有
- `KSamplerSelect` —— 5/11 个有
- `LoraLoaderBypassModelOnly` —— 5/11 个有
- `MiniMaxH3ReferenceToVideo` —— 5/11 个有
- `PurgeVRAM_UTK` —— 5/11 个有
- `SetNode` —— 5/11 个有
- `ToString` —— 5/11 个有
- `VAEDecodeAudio` —— 5/11 个有
- `BatchImagesNode` —— 4/11 个有
- `MiniMaxH3DualClockSamplerT8` —— 4/11 个有
- `LoadVideo` —— 3/11 个有
- `GetLastFrameNode` —— 2/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/11 个有
- `ModelAttentionBackend` —— 2/11 个有
- `ModelPreviewOverrideKJ` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `workflow>2` —— 2/11 个有
- `Any To String (mtb)` —— 1/11 个有
- `CR Prompt Text` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `MiniMaxH3SigmaShift` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `UniBlockSwap` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
