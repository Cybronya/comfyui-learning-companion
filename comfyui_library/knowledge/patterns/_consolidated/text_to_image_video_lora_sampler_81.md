---
name: text_to_image_video_lora_sampler_81
type: Text To Image
frequency: 9
level: strong
coverage: 0.879444
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax h3电商带货视频自动提示词模特产品展示_2088181792762318849.json, 视频生成/图生视频/全参连续帧优化｜minimaxh3提示词自动图生视频生成_2094719853226717186.json, 视频生成/图生视频/全能参考加速版图生视频｜AIGC短剧视频生成工作流_2087223105965084673.json, 视频生成/图生视频/全能视频生成｜MiniMax H3开源图生视频直出_2089796312794488834.json, 视频生成/图生视频/双采加速图生视频｜MINIMAX-H3视频生成工作流_2088326770620715010.json, 视频生成/图生视频/双采加速工作流MINIMAX H3图生视频风扇变装模板_2088358447304761345.json, 视频生成/图生视频/反推提示词极速二次采样高质量图文生视频｜MiniMax_H3视频超分写实图生视频_2088172964058587138.json, 视频生成/图生视频/反推提示词极速二采高质量｜MiniMax H3文生视频写实_2097527914727305218.json, 视频生成/图生视频/反推提示词极速二采｜MiniMax_H3写实图文生视频超分_2091790249075761153.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/minimax h3电商带货视频自动提示词模特产品展示_2088181792762318849.json、视频生成/图生视频/全参连续帧优化｜minimaxh3提示词自动图生视频生成_2094719853226717186.json、视频生成/图生视频/全能参考加速版图生视频｜AIGC短剧视频生成工作流_2087223105965084673.json、视频生成/图生视频/全能视频生成｜MiniMax H3开源图生视频直出_2089796312794488834.json、视频生成/图生视频/双采加速图生视频｜MINIMAX-H3视频生成工作流_2088326770620715010.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 8/9 个有
- `MiniMaxH3AVDecodeT8` —— 8/9 个有
- `MiniMaxH3AudioConditioningT8` —— 8/9 个有
- `BasicScheduler` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `KSamplerSelect` —— 6/9 个有
- `MiniMaxH3DualClockSamplerT8` —— 5/9 个有
- `PT_H3ConcatAVLatent` —— 5/9 个有
- `VAEEncode` —— 5/9 个有
- `CR Text` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `Dapao_LlamaCaption` —— 3/9 个有
- `Dapao_LlamaCaptionOptions` —— 3/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/9 个有
- `RegexReplace` —— 3/9 个有
- `easy promptConcat` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `RHHiddenNodes` —— 2/9 个有
- `PreviewImage` —— 1/9 个有
- `RHLLMChatNode` —— 1/9 个有
- `Text` —— 1/9 个有
- `VAEDecodeAudio` —— 1/9 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/9 个有
- `easy imageSplitGrid` —— 1/9 个有
- `easy indexAnything` —— 1/9 个有

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
