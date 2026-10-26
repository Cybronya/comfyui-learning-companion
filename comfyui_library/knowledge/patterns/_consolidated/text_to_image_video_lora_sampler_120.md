---
name: text_to_image_video_lora_sampler_120
type: Text To Image
frequency: 6
level: strong
coverage: 0.585667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), Float, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ResolutionSelector, SetNode, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 SelfLift全能流V3 VOSR速度质量兼顾工具_2113402636207742978.json, 视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json, 视频生成/图生视频/MiniMax H3短剧公司版本 图生视频高效出片处理工具_2113715561371885570.json, 视频生成/图生视频/打斗单采图生视频｜AITUDOU-MiniMax H3生成_2095847355185717249.json, 视频生成/文生视频/AITUDOU-H3+SelfLift组合｜影视级情绪表达出片_2106620640190095361.json, 视频生成/文生视频/MiniMax_H3_SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2108377073327894530.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 SelfLift全能流V3 VOSR速度质量兼顾工具_2113402636207742978.json、视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json、视频生成/图生视频/MiniMax H3短剧公司版本 图生视频高效出片处理工具_2113715561371885570.json、视频生成/图生视频/打斗单采图生视频｜AITUDOU-MiniMax H3生成_2095847355185717249.json、视频生成/文生视频/AITUDOU-H3+SelfLift组合｜影视级情绪表达出片_2106620640190095361.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 5/6 个有
- `ModelAttentionBackend` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `SelfLiftH3Sampler` —— 4/6 个有
- `BasicGuider` —— 3/6 个有
- `ExtendIntermediateSigmas` —— 3/6 个有
- `RandomNoise` —— 3/6 个有
- `SamplerCustomAdvanced` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `SolAttnMiniMax` —— 2/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `LTXVSeparateAVLatent` —— 1/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有
- `ModelPreviewOverrideKJ` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `QwenH3PromptLocal` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `VOSR2ModelLoader` —— 1/6 个有
- `VOSR2Upscale` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

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
