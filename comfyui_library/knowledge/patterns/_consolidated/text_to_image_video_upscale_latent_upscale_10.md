---
name: text_to_image_video_upscale_latent_upscale_10
type: Text To Image
frequency: 6
level: strong
coverage: 0.925333
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DF_Int_to_Float, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageResizeKJv2, Int, JjkText, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustom, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VRAMReserver, VisualizeSigmasKJ, easy getNode, easy setNode, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX2.3极速文图生视频 脱口秀数字人人物特效直出_2104354109565526017.json, 视频生成/图生视频/LTX2.3极速文图生视频脱口秀爆款工作流，人物特效数字人图生视频_2103993809603481601.json, 视频生成/图生视频/LTX2.3极速脱口秀爆款工作流｜图文直接生成段子视频_2103699150805233666.json, 视频生成/图生视频/LTX2.3脱口秀爆款生成｜极速文图生视频工作流_2095944268912353281.json, 视频生成/图生视频/脱口秀爆款 LTX2.3 极速文生_图生视频｜角色表演_2096892099085033474.json, 视频生成/图生视频/脱口秀爆款极速生成｜LTX2.3 文图双路直出视频_2096223285339058177.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/LTX2.3极速文图生视频 脱口秀数字人人物特效直出_2104354109565526017.json、视频生成/图生视频/LTX2.3极速文图生视频脱口秀爆款工作流，人物特效数字人图生视频_2103993809603481601.json、视频生成/图生视频/LTX2.3极速脱口秀爆款工作流｜图文直接生成段子视频_2103699150805233666.json、视频生成/图生视频/LTX2.3脱口秀爆款生成｜极速文图生视频工作流_2095944268912353281.json、视频生成/图生视频/脱口秀爆款 LTX2.3 极速文生_图生视频｜角色表演_2096892099085033474.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Int_to_Float`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustom`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAMReserver`
- `VisualizeSigmasKJ`
- `easy getNode`
- `easy setNode`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
