---
name: image_to_image_sampler_clip_vae_20
type: Image To Image
frequency: 9
level: strong
coverage: 0.942667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext Presets官方预设+Nunchaku快速图生图_1944610343257559042.json, 图片生成/图生图/Flux Kontext Presets预设 加速版+放大_1944364779269967873.json, 图片生成/图生图/Flux-Kontext单图提取主体线稿_2086994384654000129.json, 图片生成/图生图/Flux1 Kontext 去除图片水印_1968539542431125506.json, 图片生成/图生图/Kontext人台模特衣服展示_1938854583487619073.json, 图片生成/图生图/图像编辑（单图）_1938449619573473282.json, 图片生成/图生图/图像编辑（单图）_2039936993047617537.json, 图片生成/图生图/🦖Flux Kontext Dev一句话修图（单图）_1938427261941121025.json, 图片生成/文生图/Kontext 单图-万能改图_1940687352694206465.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_20

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux Kontext Presets官方预设+Nunchaku快速图生图_1944610343257559042.json、图片生成/图生图/Flux Kontext Presets预设 加速版+放大_1944364779269967873.json、图片生成/图生图/Flux-Kontext单图提取主体线稿_2086994384654000129.json、图片生成/图生图/Flux1 Kontext 去除图片水印_1968539542431125506.json、图片生成/图生图/Kontext人台模特衣服展示_1938854583487619073.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 8/9 个有
- `ImageConcatMulti` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `UNETLoader` —— 7/9 个有
- `ImageStitch` —— 6/9 个有
- `RH_Translator` —— 6/9 个有
- `NunchakuFluxDiTLoader` —— 3/9 个有
- `NunchakuFluxLoraLoader` —— 3/9 个有
- `PMRF` —— 3/9 个有
- `LoadKontextPresets` —— 2/9 个有
- `DF_Image_scale_by_ratio` —— 1/9 个有
- `GoogleTranslateTextNode` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 9 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
