---
name: text_to_image_lora_sampler_clip_77
type: Text To Image
frequency: 11
level: strong
coverage: 0.876182
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/4步8步加速稳定MAX｜MiniMaxH3多合一自用版_2092748173281423361.json, 视频生成/文生视频/8步加速文生视频｜minimax_h3文字生成视频工作流_2088367583484538882.json, 视频生成/文生视频/8步加速电影质感 Minimax H3 文生视频LoRA强化出片_2094165667820957697.json, 视频生成/文生视频/9图3视频3音频全能多参音视频生成开源加速版｜海螺H3文生图生视频工作流_2088148034331963394.json, 视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json, 视频生成/文生视频/H3最优官流｜文生图生视频高质量一键生成_2092047166419324930.json, 视频生成/文生视频/H3最优官流｜文生视频图生视频双模式官方_2089391709946994690.json, 视频生成/文生视频/多参考视频超级加速版｜minimaxH3文生图生视频_2092330253984296962.json, 视频生成/文生视频/官方提示词模板加持｜MiniMax H3 多图参考提速40%_2096274541071917057.json, 视频生成/文生视频/官方流优化版｜H3 文生视频 图生视频全能直出_2089335705678991361.json, 视频生成/文生视频/官方长视频工作流｜H3文生图生视频生成直出_2092731706536194050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/4步8步加速稳定MAX｜MiniMaxH3多合一自用版_2092748173281423361.json、视频生成/文生视频/8步加速文生视频｜minimax_h3文字生成视频工作流_2088367583484538882.json、视频生成/文生视频/8步加速电影质感 Minimax H3 文生视频LoRA强化出片_2094165667820957697.json、视频生成/文生视频/9图3视频3音频全能多参音视频生成开源加速版｜海螺H3文生图生视频工作流_2088148034331963394.json、视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
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

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `PrimitiveStringMultiline` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `BasicScheduler` —— 9/11 个有
- `CreateVideo` —— 9/11 个有
- `SaveVideo` —— 9/11 个有
- `LoadAudio` —— 8/11 个有
- `VHS_LoadVideo` —— 8/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/11 个有
- `PathchSageAttentionKJ` —— 6/11 个有
- `ModelPreviewOverrideKJ` —— 5/11 个有
- `PrimitiveBoolean` —— 5/11 个有
- `ComfySwitchNode` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `ManualSigmas` —— 4/11 个有
- `EasyCache` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `MiniMaxH3ImageToVideo` —— 2/11 个有
- `GetImageRangeFromBatch` —— 1/11 个有
- `Int` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LazySwitchKJ` —— 1/11 个有
- `MiniMaxH3AddGuide` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `MiniMaxH3SigmaShift` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
