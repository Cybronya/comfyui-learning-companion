---
name: text_to_image_lora_sampler_clip_229
type: Text To Image
frequency: 9
level: strong
coverage: 0.88
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/2K多参考精修｜MiniMax H3 Ref2VA三阶极致重绘视频_2089479421605539841.json, 视频生成/文生视频/2K生成式精修超分｜FL2VA三阶极致放大 MiniMax H3视频增强_2089474848572661761.json, 视频生成/文生视频/FL2VA 三阶极致放大｜MiniMax H3 2K生成式精修超分_2089246007983951873.json, 视频生成/文生视频/MiniMax H3 FL2VA三阶放大｜图生视频2K生成式精修_2089401431915851778.json, 视频生成/文生视频/MiniMax H3 Ref2VA二阶超清重绘｜视频生视频多参考精修_2089402927868899330.json, 视频生成/文生视频/Minimax_H3文生视频图生视频｜双模式生成_2095590812737425410.json, 视频生成/文生视频/Ref2VA 二阶超清重绘｜MiniMax H3 多参考图像精修_2089247666336256002.json, 视频生成/文生视频/多合一生视频V3.0｜Minimax H3文生首尾图参二采高清放大_2090209607414276097.json, 视频生成/文生视频/首尾帧精修4K｜MiniMax H3 FL2VA二阶超清放大视频生成_2089476377941729282.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_229

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/2K多参考精修｜MiniMax H3 Ref2VA三阶极致重绘视频_2089479421605539841.json、视频生成/文生视频/2K生成式精修超分｜FL2VA三阶极致放大 MiniMax H3视频增强_2089474848572661761.json、视频生成/文生视频/FL2VA 三阶极致放大｜MiniMax H3 2K生成式精修超分_2089246007983951873.json、视频生成/文生视频/MiniMax H3 FL2VA三阶放大｜图生视频2K生成式精修_2089401431915851778.json、视频生成/文生视频/MiniMax H3 Ref2VA二阶超清重绘｜视频生视频多参考精修_2089402927868899330.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
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
- `H3SigmaRefiner` —— 8/9 个有
- `LTXVConcatAVLatent` —— 8/9 个有
- `LTXVSeparateAVLatent` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `MiniMaxLowVRAMAttention` —— 8/9 个有
- `ModelAttentionBackend` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `VHS_VideoCombine` —— 8/9 个有
- `GetImageSizeAndCount` —— 7/9 个有
- `MiniMaxChunkFeedForward` —— 7/9 个有
- `Yuan_RTXVideoUpscaleH3` —— 7/9 个有
- `easy int` —— 7/9 个有
- `MiniMaxH3ImageToVideo` —— 6/9 个有
- `PathchSageAttentionKJ` —— 5/9 个有
- `MiniMaxH3HybridLoader` —— 4/9 个有
- `MiniMaxH3ReferenceToVideo` —— 4/9 个有
- `VAEEncode` —— 4/9 个有
- `SolAttnPatch` —— 2/9 个有
- `Any Switch (rgthree)` —— 1/9 个有
- `CreateVideo` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `ImagePadForOutpaint` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/9 个有
- `SaveVideo` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `SplitSigmas` —— 1/9 个有
- `忽略多组孤海` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
