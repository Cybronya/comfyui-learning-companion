---
name: image_to_image_sampler_clip_unet_79
type: Image To Image
frequency: 7
level: strong
coverage: 0.934143
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX Kontext超级局部重绘_1939221910398091265.json, 图片生成/图生图/Flux kontext dev电商万能改图王（单图版）_1942889428345831425.json, 图片生成/图生图/Kontext局部重绘_1939165958160502786.json, 图片生成/图生图/flux kontext 超强图像编辑模型_1938518653468106753.json, 图片生成/图生图/flux kontext双图模式_1938527528707358722.json, 图片生成/图生图/flux_kontext_dev_双图-提示词更听话_1938809488537538562.json, 平台全量/kontext电商产品展示_1939952119786938369.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX Kontext超级局部重绘_1939221910398091265.json、图片生成/图生图/Flux kontext dev电商万能改图王（单图版）_1942889428345831425.json、图片生成/图生图/Kontext局部重绘_1939165958160502786.json、图片生成/图生图/flux kontext 超强图像编辑模型_1938518653468106753.json、图片生成/图生图/flux kontext双图模式_1938527528707358722.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 6/7 个有
- `FluxKontextImageScale` —— 5/7 个有
- `easy showAnything` —— 4/7 个有
- `ImageAndMaskPreview` —— 3/7 个有
- `ImageRemoveAlpha+` —— 3/7 个有
- `InpaintModelConditioning` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `AddLabel` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `GoogleTranslateTextNode` —— 1/7 个有
- `GrowMaskWithBlur` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `Text Multiline` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
