---
name: text_to_image_lora_sampler_clip_164
type: Text To Image
frequency: 11
level: strong
coverage: 0.892818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json, 视频生成/图生视频/H3 LightX2V二采高清参考图生视频视频生视频_2088216027187474434.json, 视频生成/图生视频/MINIMAX-H3多图参考生视频｜多图输入角色一致生成_2094860073762902017.json, 视频生成/图生视频/MINIMAX-H3多图参考生视频｜视频生视频图生视频_2090436400712863745.json, 视频生成/图生视频/MINIMAX-H3多图参考生视频｜视频生视频图生视频都行_2114245257616519170.json, 视频生成/图生视频/MINIMAX-H3多图参考｜多张图片参考生成连贯视频_2101575258661806082.json, 视频生成/图生视频/MINIMAX-H3文戏利器｜多图参考生视频手动版API调用_2105106295446663170.json, 视频生成/图生视频/MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642.json, 视频生成/图生视频/多图参考角色一致｜MINIMAX-H3图生视频视频生视频直出_2093757341844983809.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2090555558922383362.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2095937261144731649.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json、视频生成/图生视频/H3 LightX2V二采高清参考图生视频视频生视频_2088216027187474434.json、视频生成/图生视频/MINIMAX-H3多图参考生视频｜多图输入角色一致生成_2094860073762902017.json、视频生成/图生视频/MINIMAX-H3多图参考生视频｜视频生视频图生视频_2090436400712863745.json、视频生成/图生视频/MINIMAX-H3多图参考生视频｜视频生视频图生视频都行_2114245257616519170.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 10/11 个有
- `VAEDecodeAudio` —— 10/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/11 个有
- `CreateVideo` —— 6/11 个有
- `ImageResizeKJv2` —— 6/11 个有
- `PT_H3ConcatAVLatent` —— 6/11 个有
- `SaveVideo` —— 6/11 个有
- `VAEEncode` —— 6/11 个有
- `VAEEncodeAudio` —— 6/11 个有
- `ExtendIntermediateSigmas` —— 5/11 个有
- `H3SigmaRefiner` —— 5/11 个有
- `INTConstant` —— 5/11 个有
- `LoraLoaderBypassModelOnly` —— 5/11 个有
- `VHS_VideoCombine` —— 5/11 个有
- `MiniMaxH3AVDecodeT8` —— 4/11 个有
- `AudioCrop` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `H3FaceStitch` —— 1/11 个有
- `H3FaceTrackCrop` —— 1/11 个有
- `H3InjectVideoLatent` —— 1/11 个有
- `H3PerFrameDenoise` —— 1/11 个有
- `MiniMaxH3NativeAudioLock` —— 1/11 个有
- `ModelAttentionBackend` —— 1/11 个有
- `PreviewAudio` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `SoundFlow_GetLength` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

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
