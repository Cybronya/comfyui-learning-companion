---
name: text_to_image_lora_sampler_clip_9
type: Text To Image
frequency: 27
level: strong
coverage: 0.920111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [ShowAnything|Mie, intToFloat _O, CR Prompt Text]
members: [视频生成/图生视频/MiniMax H3图生视频｜Sage加速高质量直出_2095219197193318401.json, 视频生成/图生视频/MiniMax H3图生视频｜官方加速版工作流生成_2096335585295290369.json, 视频生成/图生视频/MiniMax H3多参图像音频生视频｜Singulari极速加速版_2107645905364152321.json, 视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json, 视频生成/图生视频/MiniMax H3多图参考优化版_音频参考极速生视频_2106612379277680642.json, 视频生成/图生视频/MiniMax H3多图参考音频参考加速优化版_图生视频高效产出工具_2105720092976836609.json, 视频生成/图生视频/MiniMax H3极速生视频优化版｜多图加音频参考全支持_2111086493161836545.json, 视频生成/图生视频/Sage加速图生视频｜MiniMax H3数字人处理2608_2095495228194115585.json, 视频生成/图生视频/加速版 MiniMax H3｜多参图像音频极速生视频_2096900307132444673.json, 视频生成/图生视频/加速版MiniMax H3多参图像音频极速生视频Singulari工作流，图生视频方案_2107951250322059266.json, 视频生成/文生视频/2108028586644041729.json, 视频生成/文生视频/H3多图参考音频参考极速生视频优化版 多模态创作_2099928699171860482.json, 视频生成/文生视频/MiniMax H3多图加音频参考｜加速优化出片更快_2097164515363352577.json, 视频生成/文生视频/MiniMax H3多图加音频参考｜生视频加速版效率翻倍_2107653791804903426.json, 视频生成/文生视频/MiniMax H3多图参考音频参考加速优化版工作流，文生视频图生视频方案_2107895013450534914.json, 视频生成/文生视频/MiniMax H3多图参考音频参考加速版工作流，文生视频图生视频处理方案_2107893442566254594.json, 视频生成/文生视频/MiniMax H3多图参考音频参考极速生视频优化版 多模态输入_2105361187130142721.json, 视频生成/文生视频/MiniMax H3多图参考音频参考极速生视频优化版工作流，文生视频图生视频方案_2108272979615510530.json, 视频生成/文生视频/MiniMax H3多图参考音频参考极速生视频优化版，文生视频图生视频_2106826270205108225.json, 视频生成/文生视频/MiniMax H3多图参考音频参考｜加速优化版生成_2094524838961565698.json, 视频生成/文生视频/MiniMax H3多图音频参考极速生视频 优化版多模态创作_2098652804280832001.json, 视频生成/文生视频/MiniMax H3多图音频双参考｜加速优化版视频更稳定_2107655293843890177.json, 视频生成/文生视频/MiniMax H3极速生视频优化版｜多图参考加音频参考双加持_2105120322000347138.json, 视频生成/文生视频/biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842.json, 视频生成/文生视频/多参图像音频极速生视频｜加速版MiniMax H3生成_2096328491850625026.json, 视频生成/文生视频/多图加音频双参考输入 MiniMax H3极速生视频优化版_2104268127499542529.json, 视频生成/文生视频/海螺MiniMax H3开源版Turbo全模式视频整合流处理工具_2101755741546835970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图生视频｜Sage加速高质量直出_2095219197193318401.json、视频生成/图生视频/MiniMax H3图生视频｜官方加速版工作流生成_2096335585295290369.json、视频生成/图生视频/MiniMax H3多参图像音频生视频｜Singulari极速加速版_2107645905364152321.json、视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json、视频生成/图生视频/MiniMax H3多图参考优化版_音频参考极速生视频_2106612379277680642.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 25/27 个有
- `PathchSageAttentionKJ` —— 25/27 个有
- `LoadAudio` —— 24/27 个有
- `MiniMaxH3ReferenceToVideo` —— 24/27 个有
- `ShowAnything|Mie` —— 23/27 个有
- `CR Prompt Text` —— 20/27 个有
- `ImageResizeKJv2` —— 20/27 个有
- `Int` —— 19/27 个有
- `intToFloat _O` —— 18/27 个有
- `SaveImage` —— 12/27 个有
- `PrimitiveFloat` —— 9/27 个有
- `ResolutionSelector` —— 9/27 个有
- `GetVideoComponents` —— 6/27 个有
- `LoadVideo` —— 6/27 个有
- `ImpactSwitch` —— 5/27 个有
- `PrimitiveStringMultiline` —— 5/27 个有
- `MiniMaxH3ImageToVideo` —— 4/27 个有
- `FlashVSRInitPipe` —— 2/27 个有
- `FlashVSRNodeAdv` —— 2/27 个有
- `GetImageSize` —— 2/27 个有
- `ImageScaleToTotalPixels` —— 2/27 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/27 个有
- `Seed (rgthree)` —— 2/27 个有
- `SolAttnPatch` —— 2/27 个有
- `VHS_VideoCombine` —— 2/27 个有
- `DF_Int_to_Float` —— 1/27 个有
- `Fast Groups Bypasser (rgthree)` —— 1/27 个有
- `MuyeTextEditOutput` —— 1/27 个有
- `PlaySound|pysssss` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高发问题（27/27 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ShowAnything|Mie、intToFloat _O、CR Prompt Text
