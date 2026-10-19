---
name: text_to_image_lora_sampler_clip_67
type: Text To Image
frequency: 12
level: strong
coverage: 0.904
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json, 视频生成/图生视频/H3 LightX2V二采高清参考图生视频视频生视频_2088216027187474434.json, 视频生成/图生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100640992356556801.json, 视频生成/图生视频/H3多图参考生视频 视频生视频图生视频创作_2100303663238574081.json, 视频生成/图生视频/MINIMAX-H3文戏利器｜多图参考生视频手动版API调用_2105106295446663170.json, 视频生成/图生视频/多图参考角色一致｜MINIMAX-H3图生视频视频生视频直出_2093757341844983809.json, 视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3剧情向图生视频_2093777220228702209.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2090555558922383362.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2095937261144731649.json, 视频生成/图生视频/文戏多图参考｜MINIMAX-H3图生视频生成_2094025328523042818.json, 视频生成/文生视频/MINIMAX H3多参二采2K直出官方API文生视频图生视频_2088208139706519553.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json、视频生成/图生视频/H3 LightX2V二采高清参考图生视频视频生视频_2088216027187474434.json、视频生成/图生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100640992356556801.json、视频生成/图生视频/H3多图参考生视频 视频生视频图生视频创作_2100303663238574081.json、视频生成/图生视频/MINIMAX-H3文戏利器｜多图参考生视频手动版API调用_2105106295446663170.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LoadAudio` —— 11/12 个有
- `VAEDecodeAudio` —— 11/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/12 个有
- `VHS_VideoCombine` —— 8/12 个有
- `ExtendIntermediateSigmas` —— 7/12 个有
- `H3SigmaRefiner` —— 7/12 个有
- `INTConstant` —— 7/12 个有
- `LoraLoaderBypassModelOnly` —— 7/12 个有
- `ImageResizeKJv2` —— 6/12 个有
- `PT_H3ConcatAVLatent` —— 6/12 个有
- `VAEEncode` —— 6/12 个有
- `CreateVideo` —— 5/12 个有
- `MiniMaxH3AVDecodeT8` —— 5/12 个有
- `SaveVideo` —— 5/12 个有
- `VAEEncodeAudio` —— 5/12 个有
- `VHS_LoadVideo` —— 3/12 个有
- `SaveImage` —— 2/12 个有
- `EmptyImage` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `H3FaceStitch` —— 1/12 个有
- `H3FaceTrackCrop` —— 1/12 个有
- `H3InjectVideoLatent` —— 1/12 个有
- `H3PerFrameDenoise` —— 1/12 个有
- `MiniMaxH3NativeAudioLock` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
