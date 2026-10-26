---
name: image_to_image_lora_sampler_unet_42
type: Image To Image
frequency: 12
level: moderate
coverage: 0.704333
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/旧照变彩照_老照片修复+照片上色_细节增强_2064243413100355585.json, 图片生成/图生图/旧照片变彩色照片 老照片修复+照片上色_细节增强_2064261025423249410.json, 图片生成/图生图/旧照片变彩色照片_老照片修复+照片上色_细节增强_2057415428837830657.json, 图片生成/图生图/标准三视图 _ qwen_image_edit_2511_2096519638657097730.json, 图片生成/图生图/标准三视图 _ qwen_image_edit_2511_2111000262260379649.json, 图片生成/图生图/白底图换背景_2044055501784223746.json, 图片生成/图生图/老照片修复+全节点注释_2057042411645390849.json, 图片生成/图生图/老照片修复-修复_上色_细节增强_2040892962153959426.json, 图片生成/文生图/2.最强编辑融合，单图，双图，三图编辑qwen_image_edit_2511_2066121923188322306.json, 图片生成/文生图/Qwen_Image_Edit图像编辑模型_2105216109094981633.json, 图片生成/文生图/qwen动漫转真人+全节点注释_2055793141466320898.json, 图片生成/文生图/千问多角度templates-qwen_multiangle+全节点注释_2055470741176504322.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_42

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/旧照变彩照_老照片修复+照片上色_细节增强_2064243413100355585.json、图片生成/图生图/旧照片变彩色照片 老照片修复+照片上色_细节增强_2064261025423249410.json、图片生成/图生图/旧照片变彩色照片_老照片修复+照片上色_细节增强_2057415428837830657.json、图片生成/图生图/标准三视图 _ qwen_image_edit_2511_2096519638657097730.json、图片生成/图生图/标准三视图 _ qwen_image_edit_2511_2111000262260379649.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 11/12 个有
- `PrimitiveFloat` —— 10/12 个有
- `PrimitiveInt` —— 10/12 个有
- `ComfySwitchNode` —— 9/12 个有
- `PrimitiveBoolean` —— 9/12 个有
- `ReferenceLatent` —— 8/12 个有
- `ConditioningZeroOut` —— 7/12 个有
- `CLIPTextEncode` —— 5/12 个有
- `ImpactConditionalBranch` —— 5/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/12 个有
- `EmptyLatentImage` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `QwenMultiangleCameraNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 40 | 12 | 40% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 12 | 53% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1440 | - | 2 | 100% |
| 高度 | 1080 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 40，12 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1440，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（9/12 个样本）：Steps较低可能导致细节不足
