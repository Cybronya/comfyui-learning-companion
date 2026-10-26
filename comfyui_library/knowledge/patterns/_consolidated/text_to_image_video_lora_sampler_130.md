---
name: text_to_image_video_lora_sampler_130
type: Text To Image
frequency: 6
level: strong
coverage: 0.608333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/10Eros Max BETA5视频生成 多模态概念融合工作流_2098302417078153218.json, 视频生成/文生视频/MiniMax H3多参全能整合V2｜文生图生视频多模式工作流_2097487985720782850.json, 视频生成/文生视频/MiniMax H3多参整合工作流｜全模态视频多种模式生成_2097489623764262913.json, 视频生成/文生视频/MiniMax-H3全能参考｜文生视频图生视频多模态_2089708328279695361.json, 视频生成/文生视频/全能参考｜MiniMax-H3文生视频图生视频多模态生成_2089429895570083841.json, 视频生成/文生视频/多参全能整合V2｜MiniMax H3文生图生视频直出_2091634818105827330.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_130

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/10Eros Max BETA5视频生成 多模态概念融合工作流_2098302417078153218.json、视频生成/文生视频/MiniMax H3多参全能整合V2｜文生图生视频多模式工作流_2097487985720782850.json、视频生成/文生视频/MiniMax H3多参整合工作流｜全模态视频多种模式生成_2097489623764262913.json、视频生成/文生视频/MiniMax-H3全能参考｜文生视频图生视频多模态_2089708328279695361.json、视频生成/文生视频/全能参考｜MiniMax-H3文生视频图生视频多模态生成_2089429895570083841.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `H3SigmaRefiner` —— 5/6 个有
- `ModelPreviewOverrideKJ` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `SplitSigmas` —— 5/6 个有
- `CreateVideo` —— 4/6 个有
- `DapaoH3LocalPromptNode` —— 4/6 个有
- `Int` —— 4/6 个有
- `Int2String` —— 4/6 个有
- `JjkShowText` —— 4/6 个有
- `LTXVConcatAVLatent` —— 4/6 个有
- `LTXVSeparateAVLatent` —— 4/6 个有
- `MiniMaxH3AVDecodeT8` —— 4/6 个有
- `PrimitiveString` —— 4/6 个有
- `Text` —— 4/6 个有
- `VAEDecodeAudio` —— 4/6 个有
- `AudioCrop` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `PT_H3ConcatAVLatent` —— 3/6 个有
- `RunningHub Deepcleaner` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `VAEEncode` —— 3/6 个有
- `VAEEncodeAudio` —— 3/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/6 个有
- `Any Switch (rgthree)` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `DisableNoise` —— 2/6 个有
- `H3LatentUpscaleByJingchen573` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `MiniMaxLowVRAMAttention` —— 2/6 个有
- `MinimaxH3LatentUpscaler3D` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `DapaoH3VideoPromptNode` —— 1/6 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/6 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/6 个有

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
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
