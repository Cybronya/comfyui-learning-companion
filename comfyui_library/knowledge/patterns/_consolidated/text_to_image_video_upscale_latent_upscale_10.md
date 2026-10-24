---
name: text_to_image_video_upscale_latent_upscale_10
type: Text To Image
frequency: 7
level: strong
coverage: 0.918
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByShorterEdge, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/minimaxh3二采流数字人｜高质量口播视频生成_2095580661712252929.json, 视频生成/文生视频/六分钟极速出片｜海螺H3标准模式全能参考生视频_2096537255002333186.json, 视频生成/文生视频/极速4分钟1.2M｜海螺H3全能参考生视频9图3视频_2091189365241376770.json, 视频生成/文生视频/极速6分钟1.5M 10秒视频｜海螺H3全能参考生视频标准模式_2092014364084756481.json, 视频生成/文生视频/海螺H3全能参考生视频｜极速10秒1.5M标准模式_2096296816642973698.json, 视频生成/文生视频/海螺H3极速6分钟生成1.5M10秒视频｜标准模式全能参考_2097963506862739458.json, 视频生成/文生视频/海螺H3极速全能参考生视频｜标准模式多参考生成工作流_2097771711839166465.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_10

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/minimaxh3二采流数字人｜高质量口播视频生成_2095580661712252929.json、视频生成/文生视频/六分钟极速出片｜海螺H3标准模式全能参考生视频_2096537255002333186.json、视频生成/文生视频/极速4分钟1.2M｜海螺H3全能参考生视频9图3视频_2091189365241376770.json、视频生成/文生视频/极速6分钟1.5M 10秒视频｜海螺H3全能参考生视频标准模式_2092014364084756481.json、视频生成/文生视频/海螺H3全能参考生视频｜极速10秒1.5M标准模式_2096296816642973698.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByShorterEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AnyBooleanSwitch` —— 6/7 个有
- `PathchSageAttentionKJ` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `AudioCrop` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `MelBandRoFormerModelLoader` —— 1/7 个有
- `MelBandRoFormerSampler` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SoundFlow_GetLength` —— 1/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
