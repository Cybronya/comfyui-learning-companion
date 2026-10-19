---
name: text_to_image_video_upscale_latent_upscale_9
type: Text To Image
frequency: 8
level: strong
coverage: 0.928125
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json, 视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json, 视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json, 视频生成/图生视频/MiniMax H3双采参考生视频｜8步turbo分镜叙事_2095276866591608833.json, 视频生成/图生视频/MiniMax H3双采数字人口播 双Pass高清精修工作流_2098824235585200129.json, 视频生成/图生视频/MiniMax H3双采数字人口播｜双Pass高清精修视频生成_2097495644985446401.json, 视频生成/图生视频/MiniMax H3双采模式｜多图参考生视频画质更稳_2105138633752793090.json, 视频生成/图生视频/MiniMax H3双采采访表测试版，视频生视频图生视频采访场景方案_2103937143616917506.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json、视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json、视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json、视频生成/图生视频/MiniMax H3双采参考生视频｜8步turbo分镜叙事_2095276866591608833.json、视频生成/图生视频/MiniMax H3双采数字人口播 双Pass高清精修工作流_2098824235585200129.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `LoraLoaderBypassModelOnly` —— 6/8 个有
- `ConcatTextOfUtils` —— 4/8 个有
- `Float` —— 4/8 个有
- `SaveImage` —— 4/8 个有
- `easy anythingIndexSwitch` —— 4/8 个有
- `LoadAudio` —— 2/8 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/8 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `ImpactFloat` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `PurgeVRAM_UTK` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `ZFPromptDirectorLocalLLM` —— 1/8 个有
- `ZVH3InterviewFormV2` —— 1/8 个有
- `ZVH3ReferenceOutlet` —— 1/8 个有
- `ZVH3ReverseStage` —— 1/8 个有
- `ZVProcessingWindowOutlet` —— 1/8 个有
- `ZVUniversalMediaEvidenceDesk` —— 1/8 个有
- `easy compare` —— 1/8 个有
- `easy ifElse` —— 1/8 个有
- `llama_cpp_instruct_adv` —— 1/8 个有
- `llama_cpp_model_loader` —— 1/8 个有
- `llama_cpp_parameters` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
