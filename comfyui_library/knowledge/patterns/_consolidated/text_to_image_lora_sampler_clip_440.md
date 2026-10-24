---
name: text_to_image_lora_sampler_clip_440
type: Text To Image
frequency: 4
level: strong
coverage: 0.902
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LLaDA Image文生图全扩散架构 全参数扩散模型图像生成_2098692650353385474.json, 图片生成/文生图/文生图｜AI一句话出图，输入描述秒变高质量图片_2099875922370449410.json, 视频生成/文生视频/Anima-2.9B官方文生图｜文生视频视频生视频图生视频_2090076387519582210.json, 视频生成/文生视频/官方文生图｜Anima-2.9B动漫图像生成直出_2089790880378081282.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_440

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/LLaDA Image文生图全扩散架构 全参数扩散模型图像生成_2098692650353385474.json、图片生成/文生图/文生图｜AI一句话出图，输入描述秒变高质量图片_2099875922370449410.json、视频生成/文生视频/Anima-2.9B官方文生图｜文生视频视频生视频图生视频_2090076387519582210.json、视频生成/文生视频/官方文生图｜Anima-2.9B动漫图像生成直出_2089790880378081282.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/4 个有
- `EmptyFlux2LatentImage` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `KSampler Config (rgthree)` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `T8LLaDAImageCheckpointLoader` —— 2/4 个有
- `T8LLaDAImageScheduler` —— 2/4 个有
- `VAELoaderKJ` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `TextGenerate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
