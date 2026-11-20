---
name: text_to_image_sampler_clip_unet_114
type: Text To Image
frequency: 6
level: strong
coverage: 0.971
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2026Kontext-室内室外模型写实渲染V2.0_2043604660027658241.json, 图片生成/图生图/kontext-dev 室内客厅精装房家具布置和场景渲染_1981351444102160386.json, 图片生成/图生图/runninghubKontext-室内模型写实渲染V1_2043140986683006977.json, 图片生成/图生图/字体转3d字体_1998311838913847298.json, 图片生成/图生图/平面字体转3d膨胀字体_2015961573239558145.json, 平台全量/平面字体转3d膨胀字体_1939363683200057346.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2026Kontext-室内室外模型写实渲染V2.0_2043604660027658241.json、图片生成/图生图/kontext-dev 室内客厅精装房家具布置和场景渲染_1981351444102160386.json、图片生成/图生图/runninghubKontext-室内模型写实渲染V1_2043140986683006977.json、图片生成/图生图/字体转3d字体_1998311838913847298.json、图片生成/图生图/平面字体转3d膨胀字体_2015961573239558145.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `LoraLoader` —— 3/6 个有
- `Text Concatenate` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `SeedVR2LoadDiTModel` —— 2/6 个有
- `SeedVR2LoadVAEModel` —— 2/6 个有
- `SeedVR2VideoUpscaler` —— 2/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 640 | 512 - 768 | 6 | 80% |
| 采样步数 | 20 | 4 - 30 | 6 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | 0.7 - 1 | 3 | 84% |
| LoRA 文本强度 | 1 | 0.7 - 1 | 3 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 640，观测区间 512 - 768，6 个样本，取值集中（一致性 80%）
- 采样步数 中位数 20，观测区间 4 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
- LoRA 文本强度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
