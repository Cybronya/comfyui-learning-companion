---
name: text_to_image_lora_sampler_clip_173
type: Text To Image
frequency: 10
level: strong
coverage: 0.9269
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax_H3单模双采放大工作流8G显存版，低显存笔记本也能跑方案_2109819079400968194.json, 视频生成/图生视频/双采样高清画质流｜H3图生视频画质增强直出_2092695582556114946.json, 视频生成/图生视频/角色替换生成｜H3图生视频一键处理工作流_2095096657456226306.json, 视频生成/文生视频/2K多参考精修｜MiniMax H3 Ref2VA三阶极致重绘视频_2089479421605539841.json, 视频生成/文生视频/2K生成式精修超分｜FL2VA三阶极致放大 MiniMax H3视频增强_2089474848572661761.json, 视频生成/文生视频/FL2VA 三阶极致放大｜MiniMax H3 2K生成式精修超分_2089246007983951873.json, 视频生成/文生视频/MiniMax H3 FL2VA三阶放大｜图生视频2K生成式精修_2089401431915851778.json, 视频生成/文生视频/MiniMax H3 Ref2VA二阶超清重绘｜视频生视频多参考精修_2089402927868899330.json, 视频生成/文生视频/MiniMax H3单模双采放大工作流8G显存版，低显存笔记本也能跑方案_2106866016801345537.json, 视频生成/文生视频/Ref2VA 二阶超清重绘｜MiniMax H3 多参考图像精修_2089247666336256002.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_173

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3单模双采放大工作流8G显存版，低显存笔记本也能跑方案_2109819079400968194.json、视频生成/图生视频/双采样高清画质流｜H3图生视频画质增强直出_2092695582556114946.json、视频生成/图生视频/角色替换生成｜H3图生视频一键处理工作流_2095096657456226306.json、视频生成/文生视频/2K多参考精修｜MiniMax H3 Ref2VA三阶极致重绘视频_2089479421605539841.json、视频生成/文生视频/2K生成式精修超分｜FL2VA三阶极致放大 MiniMax H3视频增强_2089474848572661761.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：93%

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
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/10 个有
- `H3SigmaRefiner` —— 8/10 个有
- `MiniMaxH3SigmaShift` —— 8/10 个有
- `MiniMaxLowVRAMAttention` —— 8/10 个有
- `ModelAttentionBackend` —— 8/10 个有
- `easy int` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `GetImageSizeAndCount` —— 6/10 个有
- `MiniMaxChunkFeedForward` —— 6/10 个有
- `Yuan_RTXVideoUpscaleH3` —— 6/10 个有
- `PathchSageAttentionKJ` —— 5/10 个有
- `MinimaxH3LatentUpscaler3D` —— 4/10 个有
- `SaveImage` —— 4/10 个有
- `SplitSigmas` —— 4/10 个有
- `VAEEncode` —— 4/10 个有
- `CreateVideo` —— 3/10 个有
- `MiniMaxH3HybridLoader` —— 3/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `SaveVideo` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `FlashVSRNode` —— 2/10 个有
- `ModelPreviewOverrideKJ` —— 2/10 个有
- `Sleep` —— 2/10 个有
- `easy getNode` —— 2/10 个有
- `easy loraStack` —— 2/10 个有
- `easy loraStackApply` —— 2/10 个有
- `easy setNode` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `ImagePadForOutpaint` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

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
