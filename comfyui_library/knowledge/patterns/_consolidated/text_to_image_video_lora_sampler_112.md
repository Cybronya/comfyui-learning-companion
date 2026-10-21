---
name: text_to_image_video_lora_sampler_112
type: Text To Image
frequency: 6
level: strong
coverage: 0.802833
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [ShowAnything|Mie, CR Prompt Text]
members: [视频生成/图生视频/MiniMax H3视频复刻角色替换二创翻拍工作流，视频生视频图生视频方案_2106616300503134209.json, 视频生成/图生视频/MiniMax H3超强商品视频展示｜电商产品图生视频带货神器_2108008108562931714.json, 视频生成/图生视频/MiniMax H3音频驱动数字人对口型唱歌说话口播Remix文戏版方案_2105744989383913473.json, 视频生成/图生视频/MiniMax_H3九图三音多参二采工作流，文生视频图生视频多参考方案_2109441522717515777.json, 视频生成/图生视频/Minima H3武戏工作流 动作场景视频生成_2109003959313719297.json, 视频生成/视频生视频/MiniMax H3视频复刻角色替换二创翻拍工作流_视频生视频图生视频方案_2106616300503134209.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3视频复刻角色替换二创翻拍工作流，视频生视频图生视频方案_2106616300503134209.json、视频生成/图生视频/MiniMax H3超强商品视频展示｜电商产品图生视频带货神器_2108008108562931714.json、视频生成/图生视频/MiniMax H3音频驱动数字人对口型唱歌说话口播Remix文戏版方案_2105744989383913473.json、视频生成/图生视频/MiniMax_H3九图三音多参二采工作流，文生视频图生视频多参考方案_2109441522717515777.json、视频生成/图生视频/Minima H3武戏工作流 动作场景视频生成_2109003959313719297.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
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
- `SaveImage` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 4/6 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 4/6 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 4/6 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `LoadAudio` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `ConcatTextOfUtils` —— 2/6 个有
- `DA3Inference` —— 2/6 个有
- `DA3Render` —— 2/6 个有
- `Int` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LoadDA3Model` —— 2/6 个有
- `LoadVideo` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `ShowAnything|Mie` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `VHS_LoadVideoFFmpeg` —— 2/6 个有
- `VHS_VideoInfo` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/6 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `VAEDecodeAudio` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ShowAnything|Mie、CR Prompt Text
