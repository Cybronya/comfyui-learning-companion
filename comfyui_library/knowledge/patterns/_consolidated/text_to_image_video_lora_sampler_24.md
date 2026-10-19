---
name: text_to_image_video_lora_sampler_24
type: Text To Image
frequency: 18
level: strong
coverage: 0.872278
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/动态数字人口播生成｜MiniMax H3音频驱动制作_2096471857250791426.json, 视频生成/图生视频/4步lora加速版Minimax_h3_音乐MV_2085452422591377409.json, 视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2089308419999223810.json, 视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2090728184093437953.json, 视频生成/图生视频/9图3视频3音频多参考｜Minimax H3开源版音视频生成_2089469135704117249.json, 视频生成/图生视频/9图3视频3音频｜海螺H3全能多参开源版音视频生成_2090229409646202881.json, 视频生成/图生视频/H3全能参考工作流，图生视频多参考视频生成方案_2108432045293793282.json, 视频生成/图生视频/H3单图生视频_2102656768471031809.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107218917725917186.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107335317010345985.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107445931183534081.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107957288756666370.json, 视频生成/图生视频/H3单采极速文戏工作流｜图生视频高效创作首选方案_2107667535738007554.json, 视频生成/图生视频/H3单采极速文戏流程，图生视频快速产出高质量片段_2110496089349640194.json, 视频生成/图生视频/H3单采极速文戏，图生视频快速产出高质量片段_2110827618437255169.json, 视频生成/文生视频/H3官方流程单采极速文戏｜文生视频图生视频快速生成_2106986232776585218.json, 视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107179960334114818.json, 视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107462612324806657.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（数字人/数字人/动态数字人口播生成｜MiniMax H3音频驱动制作_2096471857250791426.json、视频生成/图生视频/4步lora加速版Minimax_h3_音乐MV_2085452422591377409.json、视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2089308419999223810.json、视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2090728184093437953.json、视频生成/图生视频/9图3视频3音频多参考｜Minimax H3开源版音视频生成_2089469135704117249.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 17/18 个有
- `BasicScheduler` —— 17/18 个有
- `KSamplerSelect` —— 17/18 个有
- `PrimitiveFloat` —— 17/18 个有
- `PrimitiveStringMultiline` —— 17/18 个有
- `RandomNoise` —— 17/18 个有
- `SamplerCustomAdvanced` —— 17/18 个有
- `LoadAudio` —— 16/18 个有
- `VAEDecodeAudio` —— 15/18 个有
- `VHS_LoadVideo` —— 13/18 个有
- `孤海注释` —— 13/18 个有
- `MiniMaxH3SigmaShift` —— 11/18 个有
- `ModelAttentionBackend` —— 11/18 个有
- `SaveImage` —— 11/18 个有
- `BlockSparseAttention` —— 10/18 个有
- `ExtendIntermediateSigmas` —— 10/18 个有
- `PreviewAny` —— 10/18 个有
- `EmptyImage` —— 7/18 个有
- `PreviewImage` —— 7/18 个有
- `PathchSageAttentionKJ` —— 5/18 个有
- `AudioCrop` —— 3/18 个有
- `ModelPreviewOverrideKJ` —— 3/18 个有
- `PainterVRAM` —— 3/18 个有
- `SoundFlow_GetLength` —— 3/18 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/18 个有
- `easy showAnything` —— 3/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/18 个有
- `EnhancedLoadDiffusionModel` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `PreviewAudio` —— 1/18 个有
- `RHHiddenNodes` —— 1/18 个有
- `Text` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（22/18 个样本）：Steps较低可能导致细节不足
