---
name: text_to_image_lora_sampler_clip_113
type: Text To Image
frequency: 13
level: strong
coverage: 0.848923
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax H3文生视频工作流｜高质量视频生成_2095259805958098946.json, 视频生成/文生视频/Minimax H3潜空间放大FL2VA版｜文生图生视频工作流_2097781976299294722.json, 视频生成/文生视频/MinimaxH3文生视频4步LORA加速-文生视频工作流_2087387239872557058.json, 视频生成/文生视频/REF2VA-Upscale双采样｜MiniMax_H3视频生成角色表演_2092872749298569217.json, 视频生成/文生视频/Ref2VA多参考全能生成｜MiniMax H3文生图生视频工作流_2093072782388187137.json, 视频生成/文生视频/Ref2VA多参考｜MiniMax H3全能视频生成直出_2090570005984407553.json, 视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json, 视频生成/文生视频/一键直出1080P竖屏｜动漫短剧三模视频工作流_2094052576818978817.json, 视频生成/文生视频/一键直出1080P竖屏｜动漫短剧工作流文生视频_2093846854189539329.json, 视频生成/文生视频/万象AI+sigma强化潜空间放大｜海螺H3 1080P十秒_2091018350292987905.json, 视频生成/文生视频/全能参考真实电影感｜Minimax H3双采样超分4倍8倍加速_2094804271018631170.json, 视频生成/文生视频/多参考全能生成｜MiniMax H3 Ref2VA视频处理_2093230903848947714.json, 视频生成/文生视频/高清人脸｜海螺H3 sigma强化潜空间放大视频生成_2089812873718624257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/Minimax H3文生视频工作流｜高质量视频生成_2095259805958098946.json、视频生成/文生视频/Minimax H3潜空间放大FL2VA版｜文生图生视频工作流_2097781976299294722.json、视频生成/文生视频/MinimaxH3文生视频4步LORA加速-文生视频工作流_2087387239872557058.json、视频生成/文生视频/REF2VA-Upscale双采样｜MiniMax_H3视频生成角色表演_2092872749298569217.json、视频生成/文生视频/Ref2VA多参考全能生成｜MiniMax H3文生图生视频工作流_2093072782388187137.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
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
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 11/13 个有
- `LTXVSeparateAVLatent` —— 11/13 个有
- `SplitSigmas` —— 11/13 个有
- `CreateVideo` —— 10/13 个有
- `LoadImage` —— 10/13 个有
- `MiniMaxH3SigmaShift` —— 10/13 个有
- `SaveVideo` —— 10/13 个有
- `MiniMaxH3ReferenceToVideo` —— 9/13 个有
- `PrimitiveStringMultiline` —— 9/13 个有
- `ModelAttentionBackend` —— 8/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/13 个有
- `MinimaxH3LatentUpscaler3D` —— 7/13 个有
- `ModelPreviewOverrideKJ` —— 7/13 个有
- `H3SigmaRefiner` —— 6/13 个有
- `ManualSigmas` —— 5/13 个有
- `VHS_VideoCombine` —— 5/13 个有
- `LoadAudio` —— 4/13 个有
- `MiniMaxH3ImageToVideo` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `AudioCrop` —— 3/13 个有
- `GetNode` —— 3/13 个有
- `SetNode` —— 3/13 个有
- `StringFunction|pysssss` —— 3/13 个有
- `VHS_LoadVideo` —— 3/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/13 个有
- `MuyeTextEditOutput` —— 2/13 个有
- `SolAttnMiniMax` —— 2/13 个有
- `CR Text Concatenate` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `FlashVSRNode` —— 1/13 个有
- `HAIGC_VideoLoader` —— 1/13 个有
- `MiniMaxLowVRAMAttention` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `Sleep` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
