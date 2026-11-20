---
name: text_to_image_lora_sampler_clip_187
type: Text To Image
frequency: 10
level: weak
coverage: 0.8706
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/四合一全家桶｜Qwen文生图+2511图生图+MiniMax首尾帧与多图视频_2111275974745743362.json, 视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094250837928407041.json, 视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094271866994257922.json, 视频生成/图生视频/图生视频（支持首尾帧）3倍加速loraMinimaxH3-文生_2087432699580600321.json, 视频生成/图生视频/声音）4步lora视频MinimaxH3-多参生视频（图片_2087336403087745025.json, 视频生成/图生视频/多元素参考生视频｜minimax h3图生视频直出_2092387092469993474.json, 视频生成/图生视频/多图参考生成视频｜图生视频多图融合一键出片_2093775806538534914.json, 视频生成/图生视频/实用四合一工作流：Qwen文生图、2511图生图；MinMax首尾视频、MinMax多图视频_2110212930481508354.json, 视频生成/文生视频/4步8步加速稳定MAX｜MiniMaxH3多合一自用版_2092748173281423361.json, 视频生成/文生视频/MINIMAX H3多参二采2K直出官方API文生视频图生视频_2088208139706519553.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_187

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/四合一全家桶｜Qwen文生图+2511图生图+MiniMax首尾帧与多图视频_2111275974745743362.json、视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094250837928407041.json、视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094271866994257922.json、视频生成/图生视频/图生视频（支持首尾帧）3倍加速loraMinimaxH3-文生_2087432699580600321.json、视频生成/图生视频/声音）4步lora视频MinimaxH3-多参生视频（图片_2087336403087745025.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `JjkText` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `solarL_SaveImagesToZip` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `CreateVideo` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `MiniMaxH3ReferenceToVideo` —— 7/10 个有
- `ResolutionSelector` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `MiniMaxH3ImageToVideo` —— 6/10 个有
- `LoadAudio` —— 5/10 个有
- `VHS_LoadVideo` —— 5/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `VHS_VideoCombine` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `MiniMaxH3SigmaShift` —— 3/10 个有
- `VAEEncode` —— 3/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `LatentUpscale` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `TextEncodeQwenImageEditPlus` —— 2/10 个有
- `Int` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LazySwitchKJ` —— 1/10 个有
- `MiniMaxH3AVDecodeT8` —— 1/10 个有
- `PT_H3ConcatAVLatent` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `Text` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 10 | 67% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 10 | 75% |
| 采样算法 | er_sde | - | 10 | 90% |
| 调度器 | beta | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 1080 | 10 | 0% |
| 高度 | 80 | 80 - 1920 | 10 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，10 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，10 个样本
- 采样算法 最常用 er_sde，10 个样本，一致性 90%
- 调度器 最常用 beta，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，10 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，10 个样本，取值分散，一致性仅 0%
- 高发问题（13/10 个样本）：Steps较低可能导致细节不足
