---
name: image_to_image_controlnet_lora_sampler_2
type: Image To Image
frequency: 16
level: strong
coverage: 0.917813
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DeepTranslatorTextNode, DepthAnythingV2Preprocessor, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, StringConcatenate, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageScaleToNormPixels]
problems: []
missing: []
members: [图片生成/图生图/F.1 kontext老照片划痕清理终极版_2066168189830131713.json, 图片生成/图生图/Goohai老照片高清修复-划痕清理终极版_2105193581542727681.json, 图片生成/图生图/专业级一键修复老照片瞬间定格旧时光_2060924372919087106.json, 图片生成/图生图/专业级一键修复老照片，瞬间定格旧时光_2058709062803607554.json, 图片生成/图生图/加深影像AI 老照片、破损划痕清理_2097229331507539970.json, 图片生成/图生图/破损老照片修复-真实自然-完美版V2_1989671898453823490.json, 图片生成/图生图/老孙AI 老照片划痕清理终极版_2085920574018244610.json, 图片生成/图生图/老照片修复_2082996870212833281.json, 图片生成/图生图/老照片划痕修复_2087267547275161602.json, 图片生成/图生图/老照片划痕清理终极版+上色_2101209187740114945.json, 图片生成/图生图/老照片划痕清理终极版+上色_2102209344493408257.json, 图片生成/图生图/老照片划痕清理终极版_2061324835594260482.json, 图片生成/图生图/老照片划痕清理终极版_2066513988875280386.json, 图片生成/图生图/老照片划痕清理终极版_2082028011280490498.json, 图片生成/图生图/老照片划痕清理终极版_2088088009953599489.json, 图片生成/图生图/老照片高清修复_2067553430914297858.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/F.1 kontext老照片划痕清理终极版_2066168189830131713.json、图片生成/图生图/Goohai老照片高清修复-划痕清理终极版_2105193581542727681.json、图片生成/图生图/专业级一键修复老照片瞬间定格旧时光_2060924372919087106.json、图片生成/图生图/专业级一键修复老照片，瞬间定格旧时光_2058709062803607554.json、图片生成/图生图/加深影像AI 老照片、破损划痕清理_2097229331507539970.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DeepTranslatorTextNode`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `StringConcatenate`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageScaleToNormPixels`

**可变部分**（部分 workflow 才有）：
- `DF_Float` —— 15/16 个有
- `孤海-浮点滑条` —— 15/16 个有
- `Float` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 0 - 1 | 16 | 74% |
| 采样步数 | 20 | 20 - 20 | 16 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 0 - 1，16 个样本
- 采样步数 中位数 20，观测区间 20 - 20，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
