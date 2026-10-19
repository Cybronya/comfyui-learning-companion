---
name: text_to_image_video_lora_sampler_76
type: Text To Image
frequency: 10
level: strong
coverage: 0.9216
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/2K多参考精修｜MiniMax H3 Ref2VA三阶极致重绘视频_2089479421605539841.json, 视频生成/文生视频/2K生成式精修超分｜FL2VA三阶极致放大 MiniMax H3视频增强_2089474848572661761.json, 视频生成/文生视频/FL2VA 三阶极致放大｜MiniMax H3 2K生成式精修超分_2089246007983951873.json, 视频生成/文生视频/MiniMax H3 FL2VA三阶放大｜图生视频2K生成式精修_2089401431915851778.json, 视频生成/文生视频/MiniMax H3 Ref2VA二阶超清重绘｜视频生视频多参考精修_2089402927868899330.json, 视频生成/文生视频/Minimax_H3文生视频图生视频｜双模式生成_2095590812737425410.json, 视频生成/文生视频/Ref2VA 二阶超清重绘｜MiniMax H3 多参考图像精修_2089247666336256002.json, 视频生成/文生视频/全能参考练习模式｜H3文生图生视频一键生成_2093263366285512706.json, 视频生成/文生视频/极速4分钟生成10秒视频｜海螺H3全能参考生视频_2091015558560047105.json, 视频生成/文生视频/首尾帧精修4K｜MiniMax H3 FL2VA二阶超清放大视频生成_2089476377941729282.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/2K多参考精修｜MiniMax H3 Ref2VA三阶极致重绘视频_2089479421605539841.json、视频生成/文生视频/2K生成式精修超分｜FL2VA三阶极致放大 MiniMax H3视频增强_2089474848572661761.json、视频生成/文生视频/FL2VA 三阶极致放大｜MiniMax H3 2K生成式精修超分_2089246007983951873.json、视频生成/文生视频/MiniMax H3 FL2VA三阶放大｜图生视频2K生成式精修_2089401431915851778.json、视频生成/文生视频/MiniMax H3 Ref2VA二阶超清重绘｜视频生视频多参考精修_2089402927868899330.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
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
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 9/10 个有
- `LTXVSeparateAVLatent` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `MiniMaxH3SigmaShift` —— 8/10 个有
- `MiniMaxLowVRAMAttention` —— 8/10 个有
- `GetImageSizeAndCount` —— 7/10 个有
- `H3SigmaRefiner` —— 7/10 个有
- `MiniMaxChunkFeedForward` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `ModelAttentionBackend` —— 7/10 个有
- `Yuan_RTXVideoUpscaleH3` —— 7/10 个有
- `easy int` —— 7/10 个有
- `PathchSageAttentionKJ` —— 6/10 个有
- `MiniMaxH3ImageToVideo` —— 5/10 个有
- `MiniMaxH3ReferenceToVideo` —— 5/10 个有
- `VAEEncode` —— 4/10 个有
- `MiniMaxH3HybridLoader` —— 3/10 个有
- `AnyBooleanSwitch` —— 2/10 个有
- `ManualSigmas` —— 2/10 个有
- `PrimitiveBoolean` —— 2/10 个有
- `ImagePadForOutpaint` —— 1/10 个有
- `MinimaxH3LatentUpscaler3D` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有

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
