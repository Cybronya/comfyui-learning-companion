---
name: text_to_image_video_lora_sampler_162
type: Text To Image
frequency: 3
level: strong
coverage: 0.902333
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, EmptyMiniMaxH3LatentAV, ImageConcatMulti, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AddGuide, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3_LMS视频高清修复_视频超分处理工具_2100423960998535170.json, 视频生成/图生视频/H3高清质感修复 视频画质增强处理生成工具_2099935023137910785.json, 视频生成/图生视频/H3高清质感修复_视频画质增强处理生成工具_2100513015132151810.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_162

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/H3_LMS视频高清修复_视频超分处理工具_2100423960998535170.json、视频生成/图生视频/H3高清质感修复 视频画质增强处理生成工具_2099935023137910785.json、视频生成/图生视频/H3高清质感修复_视频画质增强处理生成工具_2100513015132151810.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `EmptyMiniMaxH3LatentAV`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AddGuide`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 2/3 个有
- `ComfyNumberConvert` —— 2/3 个有
- `EmptyImage` —— 2/3 个有
- `ModelPreviewOverrideKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `SolAttnMiniMax` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
