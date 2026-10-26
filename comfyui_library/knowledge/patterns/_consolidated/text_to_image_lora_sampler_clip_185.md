---
name: text_to_image_lora_sampler_clip_185
type: Text To Image
frequency: 10
level: strong
coverage: 0.925
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Minimax参考生视频V3｜角色一致性视频生成_2094920140604403713.json, 视频生成/图生视频/BUNNY_H3高动态双采放大｜FL2VA_REF2VA专属｜打斗图生视频专用_2101851538271588353.json, 视频生成/图生视频/Eros Beta4电影感加速｜Minimax H3 Upscaler参考生视频_2095125881621663746.json, 视频生成/图生视频/H3高动态双采放大，图生视频高清增强分辨率提升工作流_2103273133582147585.json, 视频生成/图生视频/MiniMax H3参考生视频｜10Eros turbo动态叙事_2095275498304790529.json, 视频生成/图生视频/MiniMax H3参考生视频｜Dasiwa v2叠加singularity双采_2099863444169248769.json, 视频生成/图生视频/Minimax H3边跳边换装工作流｜图生视频动态效果生成_2097847006080356353.json, 视频生成/图生视频/Minimax H3边跳边换装｜舞蹈换装一镜到底_2097910210886197250.json, 视频生成/图生视频/参考生视频V3｜Minimax图生视频直出_2091659742254026753.json, 视频生成/文生视频/H3官流终极版工作流，文生视频视频生视频图生视频全覆盖方案_2105809880144769025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_185

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/Minimax参考生视频V3｜角色一致性视频生成_2094920140604403713.json、视频生成/图生视频/BUNNY_H3高动态双采放大｜FL2VA_REF2VA专属｜打斗图生视频专用_2101851538271588353.json、视频生成/图生视频/Eros Beta4电影感加速｜Minimax H3 Upscaler参考生视频_2095125881621663746.json、视频生成/图生视频/H3高动态双采放大，图生视频高清增强分辨率提升工作流_2103273133582147585.json、视频生成/图生视频/MiniMax H3参考生视频｜10Eros turbo动态叙事_2095275498304790529.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 9/10 个有
- `MiniMaxH3AVDecodeT8` —— 9/10 个有
- `MiniMaxH3AudioConditioningT8` —— 9/10 个有
- `MiniMaxH3DualClockSamplerT8` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/10 个有
- `SolAttnMiniMax` —— 9/10 个有
- `CR Prompt Text` —— 8/10 个有
- `VHS_VideoCombine` —— 8/10 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 7/10 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 7/10 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 7/10 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 7/10 个有
- `CreateVideo` —— 5/10 个有
- `LoadAudio` —— 5/10 个有
- `SaveVideo` —— 5/10 个有
- `KSamplerSelect` —— 3/10 个有
- `LTXVConcatAVLatent` —— 3/10 个有
- `LTXVSeparateAVLatent` —— 3/10 个有
- `ManualSigmas` —— 3/10 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 3/10 个有
- `ModelPreviewOverrideKJ` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `SaveImage` —— 3/10 个有
- `BatchImagesNode` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `StariAI-MiniMaxH3-Skill` —— 2/10 个有
- `llama_cpp_instruct_adv` —— 2/10 个有
- `llama_cpp_model_loader` —— 2/10 个有
- `llama_cpp_parameters` —— 2/10 个有
- `Any To String (mtb)` —— 1/10 个有
- `BasicScheduler` —— 1/10 个有
- `BlockSparseAttention` —— 1/10 个有
- `ConcatTextOfUtils` —— 1/10 个有
- `JoinStringMulti` —— 1/10 个有
- `MiniMaxH3HybridLoader` —— 1/10 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/10 个有
- `MiniMaxH3ReferenceToVideo` —— 1/10 个有
- `StringConcatenate` —— 1/10 个有
- `VAEDecodeAudio` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

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
