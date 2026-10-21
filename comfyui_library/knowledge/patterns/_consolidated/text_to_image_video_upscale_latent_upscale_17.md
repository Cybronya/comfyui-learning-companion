---
name: text_to_image_video_upscale_latent_upscale_17
type: Text To Image
frequency: 4
level: strong
coverage: 0.62625
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), Float, GetNode, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3高动态高清反推模板图生视频处理工作流_2101033381319495682.json, 视频生成/图生视频/MiniMax H3双采全能V2文戏不油武戏动态强，电商带货参考生视频方案_2103180413962383361.json, 视频生成/图生视频/MiniMax H3双采全能V2音频驱动数字人，电商带货二采图生视频工作流_2103182055260647425.json, 视频生成/图生视频/MiniMax H3双采全能V2｜文戏细腻武戏动态强电商带货参考生视频_2103048629668892674.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/H3高动态高清反推模板图生视频处理工作流_2101033381319495682.json、视频生成/图生视频/MiniMax H3双采全能V2文戏不油武戏动态强，电商带货参考生视频方案_2103180413962383361.json、视频生成/图生视频/MiniMax H3双采全能V2音频驱动数字人，电商带货二采图生视频工作流_2103182055260647425.json、视频生成/图生视频/MiniMax H3双采全能V2｜文戏细腻武戏动态强电商带货参考生视频_2103048629668892674.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `GetNode`
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
- `SetNode`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `AudioCrop` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `Context (rgthree)` —— 1/4 个有
- `Int` —— 1/4 个有
- `JWIntegerToString` —— 1/4 个有
- `JoinStringMulti` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RIFEInterpolation` —— 1/4 个有
- `ShellAgentPluginOutputText` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy boolean` —— 1/4 个有
- `easy ifElse` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

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
