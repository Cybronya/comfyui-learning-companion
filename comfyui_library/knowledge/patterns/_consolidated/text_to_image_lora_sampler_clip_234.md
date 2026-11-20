---
name: text_to_image_lora_sampler_clip_234
type: Text To Image
frequency: 9
level: strong
coverage: 0.896111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax H3文生视频工作流｜高质量视频生成_2095259805958098946.json, 视频生成/文生视频/Minimax H3潜空间放大FL2VA版｜文生图生视频工作流_2097781976299294722.json, 视频生成/文生视频/MinimaxH3文生视频4步LORA加速-文生视频工作流_2087387239872557058.json, 视频生成/文生视频/Minimax_h3超级加速文生视频｜角色一致表演流畅省币首选_2103681865688375297.json, 视频生成/文生视频/REF2VA-Upscale双采样｜MiniMax_H3视频生成角色表演_2092872749298569217.json, 视频生成/文生视频/Ref2VA多参考全能生成｜MiniMax H3文生图生视频工作流_2093072782388187137.json, 视频生成/文生视频/Ref2VA多参考｜MiniMax H3全能视频生成直出_2090570005984407553.json, 视频生成/文生视频/多参考全能生成｜MiniMax H3 Ref2VA视频处理_2093230903848947714.json, 视频生成/文生视频/文生+首尾帧全能｜MiniMax H3 FL2VA视频生成_2093227972433104897.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_234

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/Minimax H3文生视频工作流｜高质量视频生成_2095259805958098946.json、视频生成/文生视频/Minimax H3潜空间放大FL2VA版｜文生图生视频工作流_2097781976299294722.json、视频生成/文生视频/MinimaxH3文生视频4步LORA加速-文生视频工作流_2087387239872557058.json、视频生成/文生视频/Minimax_h3超级加速文生视频｜角色一致表演流畅省币首选_2103681865688375297.json、视频生成/文生视频/REF2VA-Upscale双采样｜MiniMax_H3视频生成角色表演_2092872749298569217.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

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
- `LoraLoaderModelOnly`
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
- `CreateVideo` —— 7/9 个有
- `SaveVideo` —— 7/9 个有
- `LTXVConcatAVLatent` —— 6/9 个有
- `LTXVSeparateAVLatent` —— 6/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/9 个有
- `SplitSigmas` —— 6/9 个有
- `LoadImage` —— 5/9 个有
- `MiniMaxH3ImageToVideo` —— 5/9 个有
- `MiniMaxH3SigmaShift` —— 5/9 个有
- `MinimaxH3LatentUpscaler3D` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `H3SigmaRefiner` —— 4/9 个有
- `MiniMaxH3ReferenceToVideo` —— 4/9 个有
- `ModelPreviewOverrideKJ` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `AudioCrop` —— 3/9 个有
- `LoadAudio` —— 3/9 个有
- `StringFunction|pysssss` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `ManualSigmas` —— 2/9 个有
- `ModelAttentionBackend` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `PainterVRAM` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `easy int` —— 1/9 个有

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
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
