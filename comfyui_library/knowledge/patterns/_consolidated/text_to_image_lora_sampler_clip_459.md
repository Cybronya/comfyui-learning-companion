---
name: text_to_image_lora_sampler_clip_459
type: Text To Image
frequency: 4
level: strong
coverage: 0.887
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json, 视频生成/图生视频/H3 LightX2V二采高清参考图生视频视频生视频_2088216027187474434.json, 视频生成/图生视频/H3 Taomate 3步加速 中远距离不崩脸视频生成_2099588330131382273.json, 视频生成/图生视频/MiniMax H3 Ref顶级多参不偏色不油光图生视频处理工具_2102134491904036866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_459

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json、视频生成/图生视频/H3 LightX2V二采高清参考图生视频视频生视频_2088216027187474434.json、视频生成/图生视频/H3 Taomate 3步加速 中远距离不崩脸视频生成_2099588330131382273.json、视频生成/图生视频/MiniMax H3 Ref顶级多参不偏色不油光图生视频处理工具_2102134491904036866.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 3/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `CFGGuider` —— 1/4 个有
- `H3FaceStitch` —— 1/4 个有
- `H3FaceTrackCrop` —— 1/4 个有
- `H3InjectVideoLatent` —— 1/4 个有
- `H3PerFrameDenoise` —— 1/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MiniMaxChunkFeedForward` —— 1/4 个有
- `MiniMaxH3NativeAudioLock` —— 1/4 个有
- `MiniMaxLowVRAMAttention` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `PT_H3ConcatAVLatent` —— 1/4 个有
- `QwenH3PromptLocal` —— 1/4 个有
- `VAEEncode` —— 1/4 个有
- `VAEEncodeAudio` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `YC_ShowText` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
