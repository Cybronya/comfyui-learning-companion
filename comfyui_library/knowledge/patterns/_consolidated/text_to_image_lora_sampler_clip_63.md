---
name: text_to_image_lora_sampler_clip_63
type: Text To Image
frequency: 17
level: weak
coverage: 0.885176
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/四合一全家桶｜Qwen文生图+2511图生图+MiniMax首尾帧与多图视频_2111275974745743362.json, 视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094250837928407041.json, 视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094271866994257922.json, 视频生成/图生视频/图生视频（支持首尾帧）3倍加速loraMinimaxH3-文生_2087432699580600321.json, 视频生成/图生视频/图生视频｜MiniMax H3 8步加速首帧参考生视频 写实战斗特效_2089244304341561345.json, 视频生成/图生视频/多宫格稳定出片｜海螺H3开源加速漫剧短剧多参生成_2096535638643404801.json, 视频生成/图生视频/实用四合一工作流：Qwen文生图、2511图生图；MinMax首尾视频、MinMax多图视频_2110212930481508354.json, 视频生成/图生视频/开源加速海螺多参｜H3多宫格稳定出片漫剧短剧生成_2096307060739760129.json, 视频生成/图生视频/开源加速版来了｜海螺H3多宫格角色设计图生视频_2096543788733911041.json, 视频生成/图生视频/海螺H3开源加速多参版｜文生图生视频通吃，短剧漫剧稳定量产_2099487127842148353.json, 视频生成/图生视频/海螺多参漫剧短剧｜h3开源加速版多宫格稳定出片_2092903041468030978.json, 视频生成/图生视频/海螺多参稳定出片｜H3开源加速多宫格漫剧短剧生成_2096321156952453121.json, 视频生成/图生视频/海螺多宫格稳定出片加速｜MiniMax H3开源多参漫剧短剧_2092712378231255041.json, 视频生成/文生视频/24GB通用版6倍加速参考生视频｜MiniMax H3文生图生视频生视频工作流_2087179601289236482.json, 视频生成/文生视频/48GB高配版6倍加速参考生视频｜MiniMax H3文生图生视频工作流_2087157477258383362.json, 视频生成/文生视频/H3开源加速版多参文生视频图生视频多宫格稳定出片漫剧制作方案_2106491061026779138.json, 视频生成/文生视频/H3开源加速版多参文生视频图生视频，多宫格稳定出片适用于漫剧_制作_2106170895910924289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/四合一全家桶｜Qwen文生图+2511图生图+MiniMax首尾帧与多图视频_2111275974745743362.json、视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094250837928407041.json、视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094271866994257922.json、视频生成/图生视频/图生视频（支持首尾帧）3倍加速loraMinimaxH3-文生_2087432699580600321.json、视频生成/图生视频/图生视频｜MiniMax H3 8步加速首帧参考生视频 写实战斗特效_2089244304341561345.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 16/17 个有
- `solarL_SaveImagesToZip` —— 16/17 个有
- `CreateVideo` —— 15/17 个有
- `SaveVideo` —— 15/17 个有
- `孤海注释` —— 15/17 个有
- `ResolutionSelector` —— 14/17 个有
- `MiniMaxH3ReferenceToVideo` —— 13/17 个有
- `PathchSageAttentionKJ` —— 12/17 个有
- `PrimitiveStringMultiline` —— 12/17 个有
- `VHS_VideoCombine` —— 12/17 个有
- `EasyCache` —— 11/17 个有
- `Fast Groups Bypasser (rgthree)` —— 10/17 个有
- `ModelPatchTorchSettings` —— 9/17 个有
- `MiniMaxH3ImageToVideo` —— 6/17 个有
- `ImageResizeKJv2` —— 4/17 个有
- `SaveImage` —— 4/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/17 个有
- `ConditioningZeroOut` —— 2/17 个有
- `EmptyImage` —— 2/17 个有
- `LatentUpscale` —— 2/17 个有
- `MiniMaxH3SigmaShift` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `TextEncodeQwenImageEditPlus` —— 2/17 个有
- `VAEEncode` —— 2/17 个有
- `Label (rgthree)` —— 1/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/17 个有
- `LoadAudio` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 17 | 73% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 17 | 81% |
| 采样算法 | er_sde | - | 17 | 94% |
| 调度器 | beta | - | 17 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 1080 | 17 | 0% |
| 高度 | 80 | 80 - 1920 | 17 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 37/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，17 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，17 个样本，取值集中（一致性 81%）
- 采样算法 最常用 er_sde，17 个样本，一致性 94%
- 调度器 最常用 beta，17 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，17 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，17 个样本，取值分散，一致性仅 0%
- 高发问题（37/17 个样本）：Steps较低可能导致细节不足
