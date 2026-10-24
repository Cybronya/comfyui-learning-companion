---
name: unknown_workflow_lora_sampler_clip_33
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9326
common_nodes: [CLIPLoader, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Wan降维打击生图生图提升画质_1945065856177229826.json, 图片生成/图生图/文生图（Flux+Wan2.1）国风美学优化_1958762603436728322.json, 图片生成/文生图/Aiwood-Flux+万相生图- 国风美学巅峰_2035906017795514370.json, 图片生成/文生图/Aiwood-Flux+万相生图-超真实顶级去AI，国风美学巅峰_1946275529144328193.json, 图片生成/文生图/FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json, 图片生成/文生图/Flux+万相生图-出图趋向完美_1944988238810636290.json, 图片生成/文生图/Flux+万相生图-超真实顶级去AI_1946757510213562369.json, 图片生成/文生图/Flux+万相生图_1946091501262958594.json, 图片生成/文生图/万相超强去AI感直出3K高清生图FLUX与Wan的完美组合_1946807683434311681.json, 图片生成/文生图/文生图（Flux+Wan2.1）国风美学_1946514636020543490.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Wan降维打击生图生图提升画质_1945065856177229826.json、图片生成/图生图/文生图（Flux+Wan2.1）国风美学优化_1958762603436728322.json、图片生成/文生图/Aiwood-Flux+万相生图- 国风美学巅峰_2035906017795514370.json、图片生成/文生图/Aiwood-Flux+万相生图-超真实顶级去AI，国风美学巅峰_1946275529144328193.json、图片生成/文生图/FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BetterFilmGrain` —— 8/10 个有
- `DeepTranslatorTextNode` —— 8/10 个有
- `EsesImageEffectBloom` —— 8/10 个有
- `ImageSharpen` —— 8/10 个有
- `Text Multiline` —— 8/10 个有
- `ImageConcanate` —— 6/10 个有
- `ImageScaleToMegapixels` —— 6/10 个有
- `Upscale Model Loader` —— 6/10 个有
- `LayerUtility: ImageReel` —— 3/10 个有
- `LayerUtility: ImageReelComposit` —— 3/10 个有
- `WanVideoNAG` —— 3/10 个有
- `Lora Loader Stack (rgthree)` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `TeaCache` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 10 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | uni_pc | - | 10 | 80% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 0.225 | 0.2 - 1 | 10 | 18% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 0.225，观测区间 0.2 - 1，10 个样本，取值分散，一致性仅 18%
