---
name: text_to_image_lora_sampler_clip_97
type: Text To Image
frequency: 11
level: weak
coverage: 0.900545
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/实用四合一工作流：Qwen文生图、2511图生图；MinMax首尾视频、MinMax多图视频_2110212930481508354.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093430390005518337.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093761824507383810.json, 视频生成/图生视频/开源版数字人 MiniMax-H3 视频文案一体全节点注释_2094256504005292034.json, 视频生成/图生视频/战斗场面动态拉满｜Minimax H3最佳战斗版二代_2096534069990486018.json, 视频生成/图生视频/最佳动态战斗版V2｜Minimax H3图生视频高质量生成_2096318583386230785.json, 视频生成/文生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100678580580732929.json, 视频生成/文生视频/MiniMax H3开源版｜多图参考视频生成一键处理_2094756800972279809.json, 视频生成/文生视频/minmaxH3单采加速三连发｜文生视频图生视频 又快又稳出片神器_2105532532883283969.json, 视频生成/文生视频/minmaxH3单采加速多场景｜文生视频视频生视频图生视频全支持_2105530783984340993.json, 视频生成/文生视频/minmaxH3单采加速｜文生视频图生视频 极速出片小钢炮_2105529286273880065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_97

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/实用四合一工作流：Qwen文生图、2511图生图；MinMax首尾视频、MinMax多图视频_2110212930481508354.json、视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093430390005518337.json、视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093761824507383810.json、视频生成/图生视频/开源版数字人 MiniMax-H3 视频文案一体全节点注释_2094256504005292034.json、视频生成/图生视频/战斗场面动态拉满｜Minimax H3最佳战斗版二代_2096534069990486018.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `solarL_SaveImagesToZip` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `ExtendIntermediateSigmas` —— 5/11 个有
- `ModelAttentionBackend` —— 5/11 个有
- `LoadAudio` —— 4/11 个有
- `VHS_LoadVideo` —— 4/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `DisableNoise` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `ModelPreviewOverrideKJ` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `SplitSigmasDenoise` —— 2/11 个有
- `AudioCrop` —— 1/11 个有
- `CR Text` —— 1/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `LatentUpscale` —— 1/11 个有
- `MiniMaxH3ImageToVideo` —— 1/11 个有
- `TextEncodeQwenImageEditPlus` —— 1/11 个有
- `VAEEncode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 11 | 68% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 76% |
| 采样算法 | er_sde | - | 11 | 91% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 1080 | 11 | 0% |
| 高度 | 80 | 80 - 1920 | 11 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，11 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 91%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，11 个样本，取值分散，一致性仅 0%
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
