---
name: text_to_image_lora_sampler_clip_188
type: Text To Image
frequency: 10
level: strong
coverage: 0.8668
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3 Native vs DMAD文生视频工作流，文生视频图生视频方案_2106848580148482050.json, 视频生成/文生视频/MiniMax H3文生视频 官方全模态立体声生成_2098835843896139777.json, 视频生成/文生视频/MiniMax H3文生视频V2版｜提示词一键生成视频_2089409853189091329.json, 视频生成/文生视频/MiniMax H3文生视频加速版 官方Turbo加速出片_2099198028581265410.json, 视频生成/文生视频/MiniMax H3文生视频双采latent放大｜修复鬼影重影问题_2090417255657066498.json, 视频生成/文生视频/双采latent放大｜MiniMax H3文生视频修复鬼影重影_2090542462141034498.json, 视频生成/文生视频/多参双采latent放大｜MiniMax H3三模视频生成_2091816029914746881.json, 视频生成/文生视频/多参双采latent放大｜MiniMax H3文生图生视频直出_2091651697952247809.json, 视频生成/文生视频/文生视频双采latent放大｜MiniMax H3直出生成_2091650435424808961.json, 视频生成/文生视频/文生视频双采放大｜MiniMax H3 latent高清生成_2091814698722357250.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_188

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Native vs DMAD文生视频工作流，文生视频图生视频方案_2106848580148482050.json、视频生成/文生视频/MiniMax H3文生视频 官方全模态立体声生成_2098835843896139777.json、视频生成/文生视频/MiniMax H3文生视频V2版｜提示词一键生成视频_2089409853189091329.json、视频生成/文生视频/MiniMax H3文生视频加速版 官方Turbo加速出片_2099198028581265410.json、视频生成/文生视频/MiniMax H3文生视频双采latent放大｜修复鬼影重影问题_2090417255657066498.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `SaveImage` —— 9/10 个有
- `MiniMaxH3ImageToVideo` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `VHS_VideoCombine` —— 8/10 个有
- `DiffusionModelLoaderKJ` —— 7/10 个有
- `LTXVSeparateAVLatent` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `LTXVConcatAVLatent` —— 6/10 个有
- `LoadImage` —— 6/10 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 6/10 个有
- `ShowText|fofo` —— 6/10 个有
- `UniBlockSwap` —— 6/10 个有
- `MinimaxH3LatentUpscaler3D` —— 4/10 个有
- `CreateVideo` —— 3/10 个有
- `SaveVideo` —— 3/10 个有
- `CS-MultiImageLoader` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `LoadAudio` —— 2/10 个有
- `ManualSigmas` —— 2/10 个有
- `MiniMaxH3ReferenceToVideo` —— 2/10 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有

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
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
