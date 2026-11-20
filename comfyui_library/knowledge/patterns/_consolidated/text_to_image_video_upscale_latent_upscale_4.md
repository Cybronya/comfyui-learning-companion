---
name: text_to_image_video_upscale_latent_upscale_4
type: Text To Image
frequency: 14
level: strong
coverage: 0.697214
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3超强商品视频展示｜电商产品图生视频带货神器_2108008108562931714.json, 视频生成/图生视频/MiniMax H3长视频POV第一视角｜多参考双采样图生视频｜人物特效角色设计_2104751091027103746.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参工作流，角色一致性图生视频方案_2107184502861819906.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参｜角色一致性运镜图生视频_2106998238581714946.json, 视频生成/图生视频/MiniMax H3音频驱动数字人对口型唱歌说话口播Remix文戏版方案_2105744989383913473.json, 视频生成/图生视频/MiniMax_H3九图三音多参二采工作流，文生视频图生视频多参考方案_2109441522717515777.json, 视频生成/图生视频/MiniMax_H3双采生视频Hybird+VBVR逻辑强化均衡版，长视频稳定直出_2115982355251941378.json, 视频生成/图生视频/MiniMax_H3长视频直出双采多参工作流，角色一致性图生视频方案_2109461992850419714.json, 视频生成/图生视频/Minima H3武戏工作流 动作场景视频生成_2109003959313719297.json, 视频生成/图生视频/Minimax-H3电商宣传广告｜产品视频高质量生成_2095594718758531074.json, 视频生成/图生视频/文戏短剧专用工作流｜MINIMAX-H3 图生视频细腻演绎_2096245265643692034.json, 视频生成/文生视频/9月30日目前最强武戏高动态 极速高清自动提示词加手动提示词2选1_2105345913706340354.json, 视频生成/文生视频/MiniMax H3高动文武双修工作流，文生视频视频生视频图生视频方案_2107167458216996865.json, 视频生成/文生视频/minimaxh3高动文武双修工作流 视频生成均衡方案_2108674482876534786.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3超强商品视频展示｜电商产品图生视频带货神器_2108008108562931714.json、视频生成/图生视频/MiniMax H3长视频POV第一视角｜多参考双采样图生视频｜人物特效角色设计_2104751091027103746.json、视频生成/图生视频/MiniMax H3长视频直出双采多参工作流，角色一致性图生视频方案_2107184502861819906.json、视频生成/图生视频/MiniMax H3长视频直出双采多参｜角色一致性运镜图生视频_2106998238581714946.json、视频生成/图生视频/MiniMax H3音频驱动数字人对口型唱歌说话口播Remix文戏版方案_2105744989383913473.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 14 个 workflow 都包含：
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
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
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
- `SolAttnMiniMax` —— 13/14 个有
- `GetNode` —— 11/14 个有
- `SetNode` —— 11/14 个有
- `孤海注释` —— 11/14 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 9/14 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 9/14 个有
- `SaveImage` —— 9/14 个有
- `Float` —— 8/14 个有
- `PreviewImage` —— 8/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `easy cleanGpuUsed` —— 6/14 个有
- `Astra` —— 5/14 个有
- `ConcatTextOfUtils` —— 5/14 个有
- `CreateVideo` —— 5/14 个有
- `Fast Groups Bypasser (rgthree)` —— 5/14 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 5/14 个有
- `RunningHub Deepcleaner` —— 5/14 个有
- `SaveVideo` —— 5/14 个有
- `easy anythingIndexSwitch` —— 5/14 个有
- `LoadAudio` —— 4/14 个有
- `PreviewAny` —— 3/14 个有
- `RH_LLMAPI_Pro_Node` —— 3/14 个有
- `VAEDecodeAudio` —— 3/14 个有
- `EmptyImage` —— 2/14 个有
- `CR Text Concatenate` —— 1/14 个有
- `ImpactSwitch` —— 1/14 个有
- `MiniMaxChunkFeedForward` —— 1/14 个有
- `MiniMaxLowVRAMAttention` —— 1/14 个有
- `MuyeTextEditOutput` —— 1/14 个有
- `Text Multiline` —— 1/14 个有
- `忽略多组孤海` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
