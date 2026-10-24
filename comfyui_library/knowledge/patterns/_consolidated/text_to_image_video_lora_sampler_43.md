---
name: text_to_image_video_lora_sampler_43
type: Text To Image
frequency: 15
level: strong
coverage: 0.8666
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/动态数字人口播生成｜MiniMax H3音频驱动制作_2096471857250791426.json, 视频生成/图生视频/4步lora加速版Minimax_h3_音乐MV_2085452422591377409.json, 视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2089308419999223810.json, 视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2090728184093437953.json, 视频生成/图生视频/9图3视频3音频多参考｜Minimax H3开源版音视频生成_2089469135704117249.json, 视频生成/图生视频/9图3视频3音频｜海螺H3全能多参开源版音视频生成_2090229409646202881.json, 视频生成/图生视频/H3全能参考工作流，图生视频多参考视频生成方案_2108432045293793282.json, 视频生成/图生视频/H3单图生视频_2102656768471031809.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107218917725917186.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107335317010345985.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107445931183534081.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107957288756666370.json, 视频生成/图生视频/H3单采极速文戏工作流｜图生视频高效创作首选方案_2107667535738007554.json, 视频生成/图生视频/H3单采极速文戏流程，图生视频快速产出高质量片段_2110496089349640194.json, 视频生成/图生视频/H3单采极速文戏，图生视频快速产出高质量片段_2110827618437255169.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（数字人/数字人/动态数字人口播生成｜MiniMax H3音频驱动制作_2096471857250791426.json、视频生成/图生视频/4步lora加速版Minimax_h3_音乐MV_2085452422591377409.json、视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2089308419999223810.json、视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2090728184093437953.json、视频生成/图生视频/9图3视频3音频多参考｜Minimax H3开源版音视频生成_2089469135704117249.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
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
- `BasicGuider` —— 14/15 个有
- `BasicScheduler` —— 14/15 个有
- `KSamplerSelect` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `PrimitiveStringMultiline` —— 14/15 个有
- `RandomNoise` —— 14/15 个有
- `SamplerCustomAdvanced` —— 14/15 个有
- `LoadAudio` —— 13/15 个有
- `VAEDecodeAudio` —— 12/15 个有
- `孤海注释` —— 11/15 个有
- `VHS_LoadVideo` —— 10/15 个有
- `SaveImage` —— 9/15 个有
- `MiniMaxH3SigmaShift` —— 8/15 个有
- `ModelAttentionBackend` —— 8/15 个有
- `BlockSparseAttention` —— 7/15 个有
- `ExtendIntermediateSigmas` —— 7/15 个有
- `PreviewAny` —— 7/15 个有
- `EmptyImage` —— 6/15 个有
- `PreviewImage` —— 6/15 个有
- `PathchSageAttentionKJ` —— 5/15 个有
- `AudioCrop` —— 3/15 个有
- `PainterVRAM` —— 3/15 个有
- `SoundFlow_GetLength` —— 3/15 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/15 个有
- `easy showAnything` —— 3/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/15 个有
- `EnhancedLoadDiffusionModel` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `PreviewAudio` —— 1/15 个有
- `RHHiddenNodes` —— 1/15 个有
- `Text` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（19/15 个样本）：Steps较低可能导致细节不足
