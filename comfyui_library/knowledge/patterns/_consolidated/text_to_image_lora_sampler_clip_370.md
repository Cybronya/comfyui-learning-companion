---
name: text_to_image_lora_sampler_clip_370
type: Text To Image
frequency: 5
level: strong
coverage: 0.9076
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649.json, 图片生成/文生图/AI短剧创作FLUX3加速版文生图｜提示词进去成图就出_2111332075042328577.json, 图片生成/文生图/FLUX3加速版文生图standard模式｜输入提示词一键直出_2111311147206004737.json, 图片生成/文生图/FLUX3加速版文生图，快速直出高清创意形象_2111542604138635266.json, 图片生成/文生图/Flux3多图编辑加速版，反推提示词图生图利器_2111941221856923650.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_370

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX3.0 Klein多图编辑满血版，急速生成图生图_2111576431179419649.json、图片生成/文生图/AI短剧创作FLUX3加速版文生图｜提示词进去成图就出_2111332075042328577.json、图片生成/文生图/FLUX3加速版文生图standard模式｜输入提示词一键直出_2111311147206004737.json、图片生成/文生图/FLUX3加速版文生图，快速直出高清创意形象_2111542604138635266.json、图片生成/文生图/Flux3多图编辑加速版，反推提示词图生图利器_2111941221856923650.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/5 个有
- `ReferenceMultiLatent` —— 2/5 个有
- `AnySwitch` —— 1/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `CreateBoundingBoxes` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `Int` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
