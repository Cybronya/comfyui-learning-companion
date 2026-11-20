---
name: text_to_image_video_lora_sampler_68
type: Text To Image
frequency: 12
level: strong
coverage: 0.80525
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3官方工作流文生视频｜基础视频生成_2090428143353024513.json, 视频生成/文生视频/MiniMax H3手机取物换装文生视频工作流，文生视频图生视频处理方案_2107568456165056514.json, 视频生成/文生视频/MiniMax H3数字人视频带货 多图生视频口播工具_2098845262381932545.json, 视频生成/文生视频/MiniMax H3文生视频V2版｜提示词一键生成视频_2089409853189091329.json, 视频生成/文生视频/MiniMax H3文生视频双采latent放大｜修复鬼影重影问题_2090417255657066498.json, 视频生成/文生视频/MiniMax H3活人感女友二采工作流 一键直出自然感视频_2098737048969633793.json, 视频生成/文生视频/全能参考生成视频｜MiniMax-H3文生图生视频_2095818212331048962.json, 视频生成/文生视频/双采latent放大｜MiniMax H3文生视频修复鬼影重影_2090542462141034498.json, 视频生成/文生视频/多参双采latent放大｜MiniMax H3三模视频生成_2091816029914746881.json, 视频生成/文生视频/多参双采latent放大｜MiniMax H3文生图生视频直出_2091651697952247809.json, 视频生成/文生视频/文生视频双采latent放大｜MiniMax H3直出生成_2091650435424808961.json, 视频生成/文生视频/文生视频双采放大｜MiniMax H3 latent高清生成_2091814698722357250.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3官方工作流文生视频｜基础视频生成_2090428143353024513.json、视频生成/文生视频/MiniMax H3手机取物换装文生视频工作流，文生视频图生视频处理方案_2107568456165056514.json、视频生成/文生视频/MiniMax H3数字人视频带货 多图生视频口播工具_2098845262381932545.json、视频生成/文生视频/MiniMax H3文生视频V2版｜提示词一键生成视频_2089409853189091329.json、视频生成/文生视频/MiniMax H3文生视频双采latent放大｜修复鬼影重影问题_2090417255657066498.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 11/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/12 个有
- `LTXVConcatAVLatent` —— 9/12 个有
- `LTXVSeparateAVLatent` —— 9/12 个有
- `LoadImage` —— 9/12 个有
- `PrimitiveStringMultiline` —— 9/12 个有
- `SaveImage` —— 9/12 个有
- `DiffusionModelLoaderKJ` —— 8/12 个有
- `Fast Groups Bypasser (rgthree)` —— 8/12 个有
- `MiniMaxH3ImageToVideo` —— 8/12 个有
- `MinimaxH3LatentUpscaler3D` —— 7/12 个有
- `UniBlockSwap` —— 7/12 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 6/12 个有
- `ShowText|fofo` —— 6/12 个有
- `MiniMaxH3ReferenceToVideo` —— 5/12 个有
- `GetNode` —— 4/12 个有
- `LoadAudio` —— 4/12 个有
- `ManualSigmas` —— 4/12 个有
- `SetNode` —— 4/12 个有
- `VHS_LoadVideo` —— 4/12 个有
- `CS-MultiImageLoader` —— 3/12 个有
- `ModelAttentionBackend` —— 3/12 个有
- `Label (rgthree)` —— 2/12 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/12 个有
- `Text` —— 2/12 个有
- `Any Switch (rgthree)` —— 1/12 个有
- `ExtendIntermediateSigmas` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `MiniMaxH3AVDecodeT8` —— 1/12 个有
- `MiniMaxH3SigmaShift` —— 1/12 个有
- `ModelPreviewOverrideKJ` —— 1/12 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/12 个有
- `RunningHub Deepcleaner` —— 1/12 个有
- `Seed (rgthree)` —— 1/12 个有
- `SolAttnMiniMax` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
