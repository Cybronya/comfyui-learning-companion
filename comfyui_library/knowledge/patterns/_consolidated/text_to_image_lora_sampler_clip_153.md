---
name: text_to_image_lora_sampler_clip_153
type: Text To Image
frequency: 8
level: strong
coverage: 0.62425
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimaxH3多图生成视频ENGENG_2087121643830333442.json, 视频生成/图生视频/图生视频直出｜H3模型gy定制流 高速生成视频一键出片_2089422856018030594.json, 视频生成/图生视频/图生视频｜MiniMax H3 8步加速首帧参考生视频 写实战斗特效_2089244304341561345.json, 视频生成/图生视频/多参考API用｜MiniMax H3工作流图生视频生成_2089482490334498817.json, 视频生成/图生视频/官方本地版文图音频视频生视频二次高清放大｜MiniMax H3关闭二阶图生视频_2088161682400047105.json, 视频生成/图生视频/官方版本二次高清放大视频视频）生视频音频图H3（文MiniMax_2087327299141197825.json, 视频生成/图生视频/短剧直出多合一｜MiniMax H3图生视频超级工作流_2093064037759279105.json, 视频生成/图生视频/短剧直出超级多合一｜MiniMax H3图生视频生成_2093219274356772866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/minimaxH3多图生成视频ENGENG_2087121643830333442.json、视频生成/图生视频/图生视频直出｜H3模型gy定制流 高速生成视频一键出片_2089422856018030594.json、视频生成/图生视频/图生视频｜MiniMax H3 8步加速首帧参考生视频 写实战斗特效_2089244304341561345.json、视频生成/图生视频/多参考API用｜MiniMax H3工作流图生视频生成_2089482490334498817.json、视频生成/图生视频/官方本地版文图音频视频生视频二次高清放大｜MiniMax H3关闭二阶图生视频_2088161682400047105.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `MiniMaxH3ReferenceToVideo` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `VHS_VideoCombine` —— 7/8 个有
- `ImageResizeKJv2` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `ResolutionSelector` —— 6/8 个有
- `Text` —— 6/8 个有
- `VAEDecodeAudio` —— 6/8 个有
- `VAEEncode` —— 6/8 个有
- `VAEEncodeAudio` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `LoadAudio` —— 5/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `PT_H3ConcatAVLatent` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `PrimitiveInt` —— 3/8 个有
- `RunningHub Deepcleaner` —— 3/8 个有
- `CFGGuider` —— 2/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `CreateVideo` —— 2/8 个有
- `LTXVConcatAVLatent` —— 2/8 个有
- `MiniMaxH3AVDecodeT8` —— 2/8 个有
- `ModelAttentionBackend` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `RegexExtract` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `YUAN_TXTConvertAny` —— 2/8 个有
- `YUAN_TXTJsonExtractor` —— 2/8 个有
- `YUAN_TXTParagraphSplitter` —— 2/8 个有
- `easy positive` —— 2/8 个有
- `CRTFirstLastFrameSelector` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有
- `easy mathInt` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
