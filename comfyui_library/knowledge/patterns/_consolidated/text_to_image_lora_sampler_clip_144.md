---
name: text_to_image_lora_sampler_clip_144
type: Text To Image
frequency: 12
level: strong
coverage: 0.891167
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax H3 self-lift双采 BF16加sage四步加速lora高质量高速_2098296538933059585.json, 视频生成/文生视频/Minimax H3 self-lift双采 sage加速二十五步最高质量版_2098297223221178370.json, 视频生成/文生视频/Minimax H3加速双采｜Self-Lift工作流提速出片两不误_2101510468241289218.json, 视频生成/文生视频/Minimax H3满血版黑科技加速 Self-lift双采工作流_2098704152372277249.json, 视频生成/文生视频/SelfLift双采BF16max多宫格单图专用三音色参考工作流，图生视频方案_2106481893637181442.json, 视频生成/文生视频/SelfLift双采BF16max多宫格单图专用双音色参考工作流，图生视频方案_2106512263355125761.json, 视频生成/文生视频/selfift双采BF16max多宫格单图专用｜三音色参考自由切换_2106225447443984385.json, 视频生成/文生视频/低显存高速Minimax H3双采 self-lift模式lora加速质量版_2098116326828105730.json, 视频生成/文生视频/导演skill加持双采2K直出 MiniMax H3高质量视频生成_2104764024637444098.json, 视频生成/文生视频/导演skill加持双采2K直出 MiniMax H3高质量视频生成_2105437067290431490.json, 视频生成/文生视频/海螺H3融合模型加速双采｜self-lift文生视频工作流_2097819718035001346.json, 视频生成/文生视频/黑科技加速双采self-lift工作流｜文生视频快速生成_2097773293859328001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_144

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/Minimax H3 self-lift双采 BF16加sage四步加速lora高质量高速_2098296538933059585.json、视频生成/文生视频/Minimax H3 self-lift双采 sage加速二十五步最高质量版_2098297223221178370.json、视频生成/文生视频/Minimax H3加速双采｜Self-Lift工作流提速出片两不误_2101510468241289218.json、视频生成/文生视频/Minimax H3满血版黑科技加速 Self-lift双采工作流_2098704152372277249.json、视频生成/文生视频/SelfLift双采BF16max多宫格单图专用三音色参考工作流，图生视频方案_2106481893637181442.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 11/12 个有
- `SaveImage` —— 10/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/12 个有
- `LayerUtility: PurgeVRAM V2` —— 6/12 个有
- `MiniMaxChunkFeedForward` —— 6/12 个有
- `MiniMaxH3AVDecodeT8` —— 6/12 个有
- `MiniMaxH3AudioConditioningT8` —— 6/12 个有
- `MiniMaxH3ReferenceToVideo` —— 6/12 个有
- `MiniMaxLowVRAMAttention` —— 6/12 个有
- `ModelAttentionBackend` —— 6/12 个有
- `ModelPreviewOverrideKJ` —— 6/12 个有
- `VAEDecodeAudio` —— 6/12 个有
- `LoadAudio` —— 5/12 个有
- `CreateVideo` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `MiniMaxH3SigmaShift` —— 2/12 个有
- `MiniMaxH3Unified` —— 2/12 个有
- `AudioCrop` —— 1/12 个有
- `LoraLoaderBypassModelOnly` —— 1/12 个有
- `SaveVideo` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
