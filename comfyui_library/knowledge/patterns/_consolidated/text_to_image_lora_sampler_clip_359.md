---
name: text_to_image_lora_sampler_clip_359
type: Text To Image
frequency: 6
level: strong
coverage: 0.84
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EasyCache, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3四合一视频工作流-图生文生视频_2087368958709161986.json, 视频生成/文生视频/h3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2086205446850965505.json, 视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版_2085188692620177410.json, 视频生成/文生视频/满血无损全家桶文生单图多图生视频｜MiniMax H3视频生成工作流_2088218544206077953.json, 视频生成/文生视频/满血无损加速1.0｜MiniMax H3高清工作流 文生图生视频全能生成_2089417024777834497.json, 视频生成/文生视频/满血无损高清加速版｜MiniMax H3文生图生视频工作流_2088221162772975617.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_359

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3四合一视频工作流-图生文生视频_2087368958709161986.json、视频生成/文生视频/h3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2086205446850965505.json、视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版_2085188692620177410.json、视频生成/文生视频/满血无损全家桶文生单图多图生视频｜MiniMax H3视频生成工作流_2088218544206077953.json、视频生成/文生视频/满血无损加速1.0｜MiniMax H3高清工作流 文生图生视频全能生成_2089417024777834497.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `ModelPatchTorchSettings` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `孤海注释` —— 4/6 个有
- `UniBlockSwap` —— 3/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `MiniMaxH3ImageToVideo` —— 1/6 个有
- `RegexReplace` —— 1/6 个有
- `ResizeImagesByLongerEdge` —— 1/6 个有
- `VRAM_Debug` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `easy string` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
