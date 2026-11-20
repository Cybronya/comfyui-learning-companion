---
name: text_to_image_lora_sampler_clip_269
type: Text To Image
frequency: 8
level: strong
coverage: 0.874625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3参考生视频提示词优化二阶高清处理工具_2100427862649171970.json, 视频生成/图生视频/H3真实电影质感正式版_全能参考Latent放大_2100512015759532034.json, 视频生成/图生视频/MiniMax H3 全能参考｜Latent放大 真实电影质感图生视频_2097584321895948290.json, 视频生成/图生视频/MiniMax H3真实电影质感无水印正式版 全能参考Latent放大_2109038386567794689.json, 视频生成/图生视频/参考生视频提示词优化二阶高清｜MiniMax H3动作迁移图生视频_2091319533301747713.json, 视频生成/图生视频/文生图生首尾帧视频｜MiniMax_H3二阶高清直出_2090558225891553281.json, 视频生成/文生视频/H3全能视频｜vibex文生图生首尾帧通吃，二阶高清更细腻_2099860995895291906.json, 视频生成/文生视频/H3真实电影质感正式版 全能参考Latent放大_2099956140791656450.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_269

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3参考生视频提示词优化二阶高清处理工具_2100427862649171970.json、视频生成/图生视频/H3真实电影质感正式版_全能参考Latent放大_2100512015759532034.json、视频生成/图生视频/MiniMax H3 全能参考｜Latent放大 真实电影质感图生视频_2097584321895948290.json、视频生成/图生视频/MiniMax H3真实电影质感无水印正式版 全能参考Latent放大_2109038386567794689.json、视频生成/图生视频/参考生视频提示词优化二阶高清｜MiniMax H3动作迁移图生视频_2091319533301747713.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
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
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/8 个有
- `MinimaxH3LatentUpscaler3D` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `LoadAudio` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `孤海注释` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `Any Switch (rgthree)` —— 4/8 个有
- `ComfySwitchNode` —— 4/8 个有
- `DisableNoise` —— 4/8 个有
- `H3LatentUpscaleByJingchen573` —— 4/8 个有
- `H3SigmaRefiner` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `ManualSigmas` —— 4/8 个有
- `MiniMaxChunkFeedForward` —— 4/8 个有
- `MiniMaxH3BlockCacheT8` —— 4/8 个有
- `MiniMaxH3SigmaShift` —— 4/8 个有
- `MiniMaxLowVRAMAttention` —— 4/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `SaveImage` —— 4/8 个有
- `ShowText|pysssss` —— 4/8 个有
- `SpectrumApplyMiniMaxH3` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `PrimitiveBoolean` —— 3/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `EmptyImage` —— 2/8 个有
- `Label (rgthree)` —— 2/8 个有
- `MiniMaxH3ImageToVideo` —— 2/8 个有
- `MuyeTextEditOutput` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
