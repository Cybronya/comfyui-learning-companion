---
name: text_to_image_video_lora_sampler_61
type: Text To Image
frequency: 14
level: strong
coverage: 0.577714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/全能参考二采高清放大｜H3 4步加速Lora图生视频_2096298417860468738.json, 视频生成/图生视频/全能参考去油防MINIMAX-H3脸崩工作流ENG_2087124608590901249.json, 视频生成/图生视频/加速放大Minimax参考生视频图生视频高清采样工作流_2088400575028355073.json, 视频生成/图生视频/参考生视频加速放大｜Minimax图生视频工作流_2088379811487113218.json, 视频生成/图生视频/四步加速出片｜H3全能参考二采高清放大带Lora_2096538998759059458.json, 视频生成/图生视频/图生视频直出｜H3模型gy定制流 高速生成视频一键出片_2089422856018030594.json, 视频生成/图生视频/多参考API用｜MiniMax H3工作流图生视频生成_2089482490334498817.json, 视频生成/图生视频/官方本地版文图音频视频生视频二次高清放大｜MiniMax H3关闭二阶图生视频_2088161682400047105.json, 视频生成/图生视频/官方版本二次高清放大视频视频）生视频音频图H3（文MiniMax_2087327299141197825.json, 视频生成/图生视频/超级多合一官方V2｜MiniMax H3场景特效图生视频_2089454565593804802.json, 视频生成/图生视频/闪电云 H3 图生视频兼容工作流_2114937509846278145.json, 视频生成/文生视频/GSMiniMaxH3多参二次采样放大工作流ENGENG高尚ENG_2087137351121326082.json, 视频生成/文生视频/多参全能整合｜MiniMax H3文生视频图生视频高速生成_2090141978154590210.json, 视频生成/文生视频/多参全能整合｜MiniMax H3文生视频图生视频高速生成_2090345152245223426.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/全能参考二采高清放大｜H3 4步加速Lora图生视频_2096298417860468738.json、视频生成/图生视频/全能参考去油防MINIMAX-H3脸崩工作流ENG_2087124608590901249.json、视频生成/图生视频/加速放大Minimax参考生视频图生视频高清采样工作流_2088400575028355073.json、视频生成/图生视频/参考生视频加速放大｜Minimax图生视频工作流_2088379811487113218.json、视频生成/图生视频/四步加速出片｜H3全能参考二采高清放大带Lora_2096538998759059458.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `solarL_SaveImagesToZip` —— 13/14 个有
- `GetNode` —— 12/14 个有
- `LoadAudio` —— 12/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/14 个有
- `MiniMaxH3ReferenceToVideo` —— 12/14 个有
- `PrimitiveFloat` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `VAEEncodeAudio` —— 12/14 个有
- `VHS_LoadVideo` —— 12/14 个有
- `MiniMaxH3AVDecodeT8` —— 11/14 个有
- `Fast Groups Bypasser (rgthree)` —— 10/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/14 个有
- `Text` —— 10/14 个有
- `PreviewImage` —— 8/14 个有
- `RunningHub Deepcleaner` —— 8/14 个有
- `CR Prompt Text` —— 4/14 个有
- `Int` —— 4/14 个有
- `LoraLoaderBypassModelOnly` —— 4/14 个有
- `PathchSageAttentionKJ` —— 3/14 个有
- `VAEDecodeAudio` —— 3/14 个有
- `CreateVideo` —— 2/14 个有
- `ImpactConditionalBranch` —— 2/14 个有
- `JjkShowText` —— 2/14 个有
- `MathExpression_UTK` —— 2/14 个有
- `MiniMaxH3AudioConditioningT8` —— 2/14 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/14 个有
- `PrimitiveString` —— 2/14 个有
- `RIFE VFI` —— 2/14 个有
- `ResizeShortestToNode` —— 2/14 个有
- `easy cleanGpuUsed` —— 2/14 个有
- `easy clearCacheAll` —— 2/14 个有
- `获取视频信息` —— 2/14 个有
- `CRTFirstLastFrameSelector` —— 1/14 个有
- `Dapao_LlamaH3Prompt` —— 1/14 个有
- `MiniMaxH3ImageToVideo` —— 1/14 个有
- `TrimAudioDuration` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
