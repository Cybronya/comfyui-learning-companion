---
name: image_to_image_lora_sampler_unet_71
type: Image To Image
frequency: 10
level: strong
coverage: 0.7509
common_nodes: [CFGNorm, CLIPLoader, ComfySwitchNode, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/工作流基础系列15-FireRed-Image-Edit图像编辑工作流_2047986247905320961.json, 图片生成/图生图/旧照变彩照_老照片修复+照片上色_细节增强_2064243413100355585.json, 图片生成/图生图/旧照片变彩色照片 老照片修复+照片上色_细节增强_2064261025423249410.json, 图片生成/图生图/旧照片变彩色照片_老照片修复+照片上色_细节增强_2057415428837830657.json, 图片生成/图生图/老照片修复+全节点注释_2057042411645390849.json, 图片生成/图生图/老照片修复-修复_上色_细节增强_2040892962153959426.json, 平台全量/旧照片变彩色照片 老照片修复+照片上色_细节增强_2056568571765022721.json, 平台全量/旧照片变彩色照片 老照片修复+照片上色_细节增强_2064152768176279554.json, 平台全量/老旧照片修复-上色&修复&细节增强_2043529906130259969.json, 平台全量/老照片修复 照片上色_细节增强_2052938902478045185.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_71

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/工作流基础系列15-FireRed-Image-Edit图像编辑工作流_2047986247905320961.json、图片生成/图生图/旧照变彩照_老照片修复+照片上色_细节增强_2064243413100355585.json、图片生成/图生图/旧照片变彩色照片 老照片修复+照片上色_细节增强_2064261025423249410.json、图片生成/图生图/旧照片变彩色照片_老照片修复+照片上色_细节增强_2057415428837830657.json、图片生成/图生图/老照片修复+全节点注释_2057042411645390849.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ComfySwitchNode`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 9/10 个有
- `ConditioningZeroOut` —— 9/10 个有
- `ImpactConditionalBranch` —— 9/10 个有
- `ReferenceLatent` —— 9/10 个有
- `CR Text` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `LayerUtility: TextBox` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `easy ifElse` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 10 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
