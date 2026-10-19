---
name: text_to_image_lora_sampler_clip_116
type: Text To Image
frequency: 8
level: strong
coverage: 0.906625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/4STEP-REF-ALL全能参考｜H3视频图生工作流_2095115253225975809.json, 视频生成/图生视频/4步图片视频参考｜MiniMax-H3 Ref2VA图生视频_2092349573921599490.json, 视频生成/图生视频/8step加速开源版｜MinimaxH3参考生视频图生视频_2093224901363720194.json, 视频生成/图生视频/H3-4STEP-REF-ALL全能参考｜四步加速视频生成_2094941361458991106.json, 视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json, 视频生成/图生视频/MiniMax H3全能参考工作流｜图生视频万能底座_2105278066246373377.json, 视频生成/图生视频/MiniMax H3加速版电商4图参考｜数字人模特产品展示图生视频_2090065106997698561.json, 视频生成/文生视频/MinimaxH3开源版参考生视频｜9-3-3高质量生成_2095584855844278273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_116

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/4STEP-REF-ALL全能参考｜H3视频图生工作流_2095115253225975809.json、视频生成/图生视频/4步图片视频参考｜MiniMax-H3 Ref2VA图生视频_2092349573921599490.json、视频生成/图生视频/8step加速开源版｜MinimaxH3参考生视频图生视频_2093224901363720194.json、视频生成/图生视频/H3-4STEP-REF-ALL全能参考｜四步加速视频生成_2094941361458991106.json、视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
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
- `ComfyMathExpression` —— 6/8 个有
- `LoadAudio` —— 6/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `PathchSageAttentionKJ` —— 4/8 个有
- `VHS_LoadVideo` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `DF_Text_Box` —— 2/8 个有
- `GetVideoComponents` —— 2/8 个有
- `LoadVideo` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `MiniMaxH3SigmaShift` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `RH_LLMAPI_Pro_Node` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `LoraLoaderBypassModelOnly` —— 1/8 个有
- `MiniMaxH3HybridLoader` —— 1/8 个有
- `PreviewAny` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
