---
name: text_to_image_lora_sampler_clip_143
type: Text To Image
frequency: 11
level: strong
coverage: 0.905818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/4STEP-REF-ALL全能参考｜H3视频图生工作流_2095115253225975809.json, 视频生成/图生视频/4步图片视频参考｜MiniMax-H3 Ref2VA图生视频_2092349573921599490.json, 视频生成/图生视频/8step加速开源版｜MinimaxH3参考生视频图生视频_2093224901363720194.json, 视频生成/图生视频/8步加速1.0正式版｜minimax 1.0视频生视频图生视频工作流_2088345029642379265.json, 视频生成/图生视频/H3-4STEP-REF-ALL全能参考｜四步加速视频生成_2094941361458991106.json, 视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json, 视频生成/图生视频/MiniMax H3多参图像音频生视频｜Singulari极速加速版_2107645905364152321.json, 视频生成/图生视频/加速版 MiniMax H3｜多参图像音频极速生视频_2096900307132444673.json, 视频生成/图生视频/加速版MiniMax H3多参图像音频极速生视频Singulari工作流，图生视频方案_2107951250322059266.json, 视频生成/文生视频/biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842.json, 视频生成/文生视频/多参图像音频极速生视频｜加速版MiniMax H3生成_2096328491850625026.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/4STEP-REF-ALL全能参考｜H3视频图生工作流_2095115253225975809.json、视频生成/图生视频/4步图片视频参考｜MiniMax-H3 Ref2VA图生视频_2092349573921599490.json、视频生成/图生视频/8step加速开源版｜MinimaxH3参考生视频图生视频_2093224901363720194.json、视频生成/图生视频/8步加速1.0正式版｜minimax 1.0视频生视频图生视频工作流_2088345029642379265.json、视频生成/图生视频/H3-4STEP-REF-ALL全能参考｜四步加速视频生成_2094941361458991106.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
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
- `LoadAudio` —— 10/11 个有
- `ComfyMathExpression` —— 9/11 个有
- `PrimitiveFloat` —— 9/11 个有
- `CR Prompt Text` —— 7/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `GetVideoComponents` —— 6/11 个有
- `LoadVideo` —— 6/11 个有
- `EasyCache` —— 5/11 个有
- `ImpactSwitch` —— 5/11 个有
- `ShowAnything|Mie` —— 5/11 个有
- `VHS_LoadVideo` —— 3/11 个有
- `DF_Text_Box` —— 2/11 个有
- `MathExpression|pysssss` —— 2/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `RH_LLMAPI_Pro_Node` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `DF_Int_to_Float` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `MiniMaxH3SigmaShift` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有

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
