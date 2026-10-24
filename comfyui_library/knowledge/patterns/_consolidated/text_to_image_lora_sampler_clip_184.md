---
name: text_to_image_lora_sampler_clip_184
type: Text To Image
frequency: 9
level: strong
coverage: 0.910556
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, ReferenceMultiLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649.json, 图片生成/图生图/Flux3加速版多图编辑写真向｜人像写真改图不吃力_2111333564863307778.json, 图片生成/图生图/Flux3加速版多图编辑，sd-in 量化提速电商图生图_2111513720408068097.json, 图片生成/图生图/Flux3加速版多图编辑，人像写真图生图快速出片_2111535026918744066.json, 图片生成/图生图/Flux3图像编辑邪修流，图生图黑科技玩法实测_2111184292708704257.json, 图片生成/图生图/Flux3多图编辑加速版，1到4张参考图自由组合_2112334139688050690.json, 图片生成/图生图/Flux3多图编辑加速版，写真图生图效率翻倍_2111544034245308417.json, 图片生成/图生图/Flux3多图编辑加速版，图生图批量出图效率翻倍_2111890689465339906.json, 图片生成/图生图/Flux3多图编辑加速版｜最多4图混合最少1张也能跑｜多图融合编辑省时间_2112061118301691906.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_184

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649.json、图片生成/图生图/Flux3加速版多图编辑写真向｜人像写真改图不吃力_2111333564863307778.json、图片生成/图生图/Flux3加速版多图编辑，sd-in 量化提速电商图生图_2111513720408068097.json、图片生成/图生图/Flux3加速版多图编辑，人像写真图生图快速出片_2111535026918744066.json、图片生成/图生图/Flux3图像编辑邪修流，图生图黑科技玩法实测_2111184292708704257.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `ReferenceMultiLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 4/9 个有
- `Text` —— 4/9 个有
- `AnySwitch` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `ComfySwitchNode` —— 1/9 个有
- `CreateBoundingBoxes` —— 1/9 个有
- `Fast Bypasser (rgthree)` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `Int` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `QwenPERewriteT8` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
