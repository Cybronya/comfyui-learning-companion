---
name: text_to_image_lora_sampler_clip_140
type: Text To Image
frequency: 12
level: strong
coverage: 0.88925
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/10Eros-Max Minimax BF16超级融合参考生视频-高质量加速版TEST3_2087401342334758913.json, 视频生成/图生视频/48GB高配版6倍加速参考生视频｜MiniMax H3图生视频工作流_2088219969338302466.json, 视频生成/图生视频/4STEP-REF-ALL全能参考｜H3视频图生工作流_2095115253225975809.json, 视频生成/图生视频/4步图片视频参考｜MiniMax-H3 Ref2VA图生视频_2092349573921599490.json, 视频生成/图生视频/6倍加速24GB通用版优化版｜MiniMax H3图生视频数字人工作流_2087156243797471233.json, 视频生成/图生视频/H3-4STEP-REF-ALL全能参考｜四步加速视频生成_2094941361458991106.json, 视频生成/图生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086421628958892033.json, 视频生成/图生视频/MiniMax H3加速版电商4图参考｜数字人模特产品展示图生视频_2090065106997698561.json, 视频生成/图生视频/MiniMax H3图生视频6倍加速48GB高配版｜速度狂飙_2113980295203606530.json, 视频生成/图生视频/MiniMaxH3参考生视频量化加速｜文本图像音频视频全能_2089438111041409026.json, 视频生成/图生视频/Minimax H3无色差版｜首尾帧参考生视频电商模特展示_2089376588533157889.json, 视频生成/图生视频/导演台双采样全能工作流｜MiniMax H3图生视频_2092388355215552514.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_140

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/10Eros-Max Minimax BF16超级融合参考生视频-高质量加速版TEST3_2087401342334758913.json、视频生成/图生视频/48GB高配版6倍加速参考生视频｜MiniMax H3图生视频工作流_2088219969338302466.json、视频生成/图生视频/4STEP-REF-ALL全能参考｜H3视频图生工作流_2095115253225975809.json、视频生成/图生视频/4步图片视频参考｜MiniMax-H3 Ref2VA图生视频_2092349573921599490.json、视频生成/图生视频/6倍加速24GB通用版优化版｜MiniMax H3图生视频数字人工作流_2087156243797471233.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 11/12 个有
- `ResolutionSelector` —— 11/12 个有
- `孤海注释` —— 11/12 个有
- `ComfyMathExpression` —— 10/12 个有
- `PrimitiveFloat` —— 10/12 个有
- `MiniMaxH3ReferenceToVideo` —— 9/12 个有
- `PrimitiveStringMultiline` —— 9/12 个有
- `ImageResizeKJv2` —— 5/12 个有
- `LoadAudio` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `EasyCache` —— 4/12 个有
- `MiniMaxH3BlockCacheT8` —— 3/12 个有
- `MiniMaxH3ImageToVideo` —— 3/12 个有
- `MiniMaxH3SigmaShift` —— 3/12 个有
- `PrimitiveInt` —— 3/12 个有
- `DF_Text_Box` —— 2/12 个有
- `MathExpression|pysssss` —— 2/12 个有
- `MiniMaxH3HybridLoader` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `RH_LLMAPI_Pro_Node` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `ComfyMiniMaxH3Director` —— 1/12 个有
- `ImageScaleToTotalPixels` —— 1/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/12 个有
- `ModelAttentionBackend` —— 1/12 个有
- `SolAttnMiniMax` —— 1/12 个有

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
