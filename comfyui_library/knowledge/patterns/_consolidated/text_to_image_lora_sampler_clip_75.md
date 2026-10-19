---
name: text_to_image_lora_sampler_clip_75
type: Text To Image
frequency: 11
level: weak
coverage: 0.887182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/四合一全家桶｜Qwen文生图+2511图生图+MiniMax首尾帧与多图视频_2111275974745743362.json, 视频生成/图生视频/图生视频加速版｜MiniMax H3人物场景特效生成_2093842351939743746.json, 视频生成/图生视频/官流直出美少女视频｜Minimax-H3 图生视频原汁原味_2096269567709499393.json, 视频生成/图生视频/实用四合一工作流：Qwen文生图、2511图生图；MinMax首尾视频、MinMax多图视频_2110212930481508354.json, 视频生成/图生视频/导演台双采样全能工作流｜MiniMax H3图生视频_2092388355215552514.json, 视频生成/图生视频/高质量加速图生视频 Minimax H3 画质与速度兼顾快速出片_2094180356353249281.json, 视频生成/图生视频/高质量加速版图生视频｜Minimax H3一键高清生成_2094316328000778241.json, 视频生成/文生视频/24GB通用版6倍加速参考生视频｜MiniMax H3文生图生视频生视频工作流_2087179601289236482.json, 视频生成/文生视频/48GB高配版6倍加速参考生视频｜MiniMax H3文生图生视频工作流_2087157477258383362.json, 视频生成/文生视频/LightX2V Turbo加速｜MiniMax H3文生图生视频生视频工作流_2087187099337445378.json, 视频生成/文生视频/MiniMax参考生视频高质量加速版处理工具_2101029961053327362.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/四合一全家桶｜Qwen文生图+2511图生图+MiniMax首尾帧与多图视频_2111275974745743362.json、视频生成/图生视频/图生视频加速版｜MiniMax H3人物场景特效生成_2093842351939743746.json、视频生成/图生视频/官流直出美少女视频｜Minimax-H3 图生视频原汁原味_2096269567709499393.json、视频生成/图生视频/实用四合一工作流：Qwen文生图、2511图生图；MinMax首尾视频、MinMax多图视频_2110212930481508354.json、视频生成/图生视频/导演台双采样全能工作流｜MiniMax H3图生视频_2092388355215552514.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 10/11 个有
- `solarL_SaveImagesToZip` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `ResolutionSelector` —— 8/11 个有
- `MiniMaxH3ImageToVideo` —— 7/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `MiniMaxH3ReferenceToVideo` —— 6/11 个有
- `ImageResizeKJv2` —— 5/11 个有
- `MiniMaxH3BlockCacheT8` —— 4/11 个有
- `SaveImage` —— 3/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `EasyCache` —— 2/11 个有
- `GetImageSize` —— 2/11 个有
- `ImageScaleToTotalPixels` —— 2/11 个有
- `LatentUpscale` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `TextEncodeQwenImageEditPlus` —— 2/11 个有
- `VAEEncode` —— 2/11 个有
- `Label (rgthree)` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `MiniMaxH3SigmaShift` —— 1/11 个有
- `ResizeImageMaskNode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 11 | 68% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 76% |
| 采样算法 | er_sde | - | 11 | 91% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 1080 | 11 | 0% |
| 高度 | 80 | 80 - 1920 | 11 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，11 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 91%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，11 个样本，取值分散，一致性仅 0%
- 高发问题（14/11 个样本）：Steps较低可能导致细节不足
