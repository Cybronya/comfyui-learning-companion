---
name: image_to_image_sampler_clip_unet_109
type: Image To Image
frequency: 4
level: strong
coverage: 0.90325
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, RH_Translator, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/FLUX Kontext超级局部重绘_1939221910398091265.json, 图片生成/图生图/Flux kontext dev电商万能改图王（单图版）_1942889428345831425.json, 图片生成/图生图/Kontext局部重绘_1939165958160502786.json, 图片生成/图生图/flux_kontext_dev_双图-提示词更听话_1938809488537538562.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_109

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX Kontext超级局部重绘_1939221910398091265.json、图片生成/图生图/Flux kontext dev电商万能改图王（单图版）_1942889428345831425.json、图片生成/图生图/Kontext局部重绘_1939165958160502786.json、图片生成/图生图/flux_kontext_dev_双图-提示词更听话_1938809488537538562.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `ImageAndMaskPreview` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageRemoveAlpha+` —— 2/4 个有
- `InpaintModelConditioning` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_sde | - | 4 | 50% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
