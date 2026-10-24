---
name: text_to_image_lora_sampler_clip_341
type: Text To Image
frequency: 5
level: strong
coverage: 0.8866
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux3_klein图像编辑，图片换背景图生图方案_2111573166886834178.json, 图片生成/图生图/Flux3单图编辑工作流，图生图其它图片处理方案_2111935169623052290.json, 图片生成/图生图/Qwen一键出人物三视图｜角色一致性拉满的图生图神器_2111264557317574658.json, 图片生成/图生图/refMod图生图8视角生成，单图产出环绕多视图_2112320029848068098.json, 图片生成/文生图/flux3编辑工作流，文生图图生图玩法随心切_2111577956366770178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_341

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux3_klein图像编辑，图片换背景图生图方案_2111573166886834178.json、图片生成/图生图/Flux3单图编辑工作流，图生图其它图片处理方案_2111935169623052290.json、图片生成/图生图/Qwen一键出人物三视图｜角色一致性拉满的图生图神器_2111264557317574658.json、图片生成/图生图/refMod图生图8视角生成，单图产出环绕多视图_2112320029848068098.json、图片生成/文生图/flux3编辑工作流，文生图图生图玩法随心切_2111577956366770178.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/5 个有
- `EmptyFlux2LatentImage` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageReel` —— 3/5 个有
- `LayerUtility: ImageReelComposit` —— 3/5 个有
- `ReferenceMultiLatent` —— 3/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `TextEncodeQwenImage21` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `QwenImage21Cache` —— 1/5 个有
- `easy promptLine` —— 1/5 个有
- `easy setNode` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

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
