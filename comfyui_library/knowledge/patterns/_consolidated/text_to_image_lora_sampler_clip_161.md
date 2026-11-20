---
name: text_to_image_lora_sampler_clip_161
type: Text To Image
frequency: 11
level: strong
coverage: 0.853
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/fl2v_turbo加速｜MiniMax-H3图生视频文生视频提速_2089412676161204225.json, 视频生成/文生视频/h3文生_首尾帧视频_2087479552833576961.json, 视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json, 视频生成/文生视频/一键直出1080P竖屏｜动漫短剧三模视频工作流_2094052576818978817.json, 视频生成/文生视频/一键直出1080P竖屏｜动漫短剧工作流文生视频_2093846854189539329.json, 视频生成/文生视频/两步生成768P视频｜Minimax H3 多参数加速LoRA_2096256232272257025.json, 视频生成/文生视频/低动态真实感人物视频｜H3 sigma强化潜空间双采_2096336928575680513.json, 视频生成/文生视频/多参数视频生成768p｜Minimax H3加速LoRA两步_2095964673219846146.json, 视频生成/文生视频/多参生视频潜空间放大二采｜Minimax H3高质量版_2095969486913495042.json, 视频生成/文生视频/多参生视频潜空间放大｜Minimax H3 二采画质更稳_2096260116558467073.json, 视频生成/文生视频/多合一生视频V3.0｜Minimax H3文生首尾图参二采高清放大_2090209607414276097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/fl2v_turbo加速｜MiniMax-H3图生视频文生视频提速_2089412676161204225.json、视频生成/文生视频/h3文生_首尾帧视频_2087479552833576961.json、视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json、视频生成/文生视频/一键直出1080P竖屏｜动漫短剧三模视频工作流_2094052576818978817.json、视频生成/文生视频/一键直出1080P竖屏｜动漫短剧工作流文生视频_2093846854189539329.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
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
- `KSamplerSelect` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `CreateVideo` —— 9/11 个有
- `LTXVConcatAVLatent` —— 9/11 个有
- `LTXVSeparateAVLatent` —— 9/11 个有
- `MiniMaxH3SigmaShift` —— 9/11 个有
- `ModelAttentionBackend` —— 9/11 个有
- `SaveVideo` —— 9/11 个有
- `MiniMaxH3ReferenceToVideo` —— 8/11 个有
- `MinimaxH3LatentUpscaler3D` —— 7/11 个有
- `SplitSigmas` —— 7/11 个有
- `ModelPreviewOverrideKJ` —— 6/11 个有
- `PrimitiveStringMultiline` —— 6/11 个有
- `ManualSigmas` —— 5/11 个有
- `VHS_VideoCombine` —— 5/11 个有
- `MiniMaxH3ImageToVideo` —— 4/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/11 个有
- `GetVideoComponents` —— 2/11 个有
- `H3SigmaRefiner` —— 2/11 个有
- `LoadVideo` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `Text` —— 2/11 个有
- `忽略多组孤海` —— 2/11 个有
- `Any Switch (rgthree)` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `MiniMaxH3HybridLoader` —— 1/11 个有
- `MiniMaxH3TurboLoRA` —— 1/11 个有
- `MiniMaxH3TurboSampler` —— 1/11 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/11 个有
- `PixaromaDuration` —— 1/11 个有
- `PixaromaSizes` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
