---
name: image_to_image_sampler_vae_6
type: Image To Image
frequency: 16
level: moderate
coverage: 0.935812
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/增强背景和主图效果_2059630159023656961.json, 图片生成/图生图/材质修改Q2511_2008020062157934594.json, 图片生成/图生图/橘-qwen edit 2509 多图编辑基础流_2003471485438181377.json, 图片生成/图生图/灯光调节器-qwen_image_edit_2511_2011441135843024897.json, 图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099327221906362369.json, 图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099667042474479618.json, 图片生成/图生图/爆火新年祭_2005453436986552322.json, 图片生成/图生图/电商模特三视图_qwen_image_edit_2509_Jefsky_1976877911221456897.json, 图片生成/图生图/顶级图像编辑模型 Qwen-Image-Edit-2511工作流_2005170734341255169.json, 图片生成/图生图/👾怪獸-QWEN-EDIT-2511+重打光强化版👾_2014642307299020802.json, 图片生成/图生图/🦖2511可视化重打灯光_2011613758954676226.json, 图片生成/文生图/Qwen-Edit-2511-拜新年、新年祭、元旦节图生图工作流_2005959009792393217.json, 平台全量/QWEN 2511：可视化灯光调节(重打光lora强化版)_2040287707124998146.json, 平台全量/Qwen-Edit-2511 新年海报 活动春节拜年 拜新年 新年祭 元宵节 元旦 节日海报 图生图_2011252675752497154.json, 平台全量/【阡陌】Qwen-Eidt-2511可视化灯光视角颜色控制重打光工作流_2011047621598650369.json, 平台全量/灯光调节器-qwen_image_edit_2511_2098674249333559297.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_6

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/增强背景和主图效果_2059630159023656961.json、图片生成/图生图/材质修改Q2511_2008020062157934594.json、图片生成/图生图/橘-qwen edit 2509 多图编辑基础流_2003471485438181377.json、图片生成/图生图/灯光调节器-qwen_image_edit_2511_2011441135843024897.json、图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099327221906362369.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 15/16 个有
- `ModelSamplingAuraFlow` —— 15/16 个有
- `FluxKontextMultiReferenceLatentMethod` —— 13/16 个有
- `ImageScaleToTotalPixels` —— 13/16 个有
- `UNETLoader` —— 12/16 个有
- `LoraLoaderModelOnly` —— 11/16 个有
- `QwenMultiangleLightningNode` —— 8/16 个有
- `EmptySD3LatentImage` —— 7/16 个有
- `Anything Everywhere3` —— 4/16 个有
- `RHHiddenNodes` —— 4/16 个有
- `easy promptList` —— 4/16 个有
- `ReferenceLatent` —— 3/16 个有
- `easy showAnything` —— 3/16 个有
- `ConditioningZeroOut` —— 1/16 个有
- `FluxGuidance` —— 1/16 个有
- `UnetLoaderGGUF` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 16 | 8% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 81% |
| 调度器 | simple | - | 16 | 81% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，16 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 81%
- 调度器 最常用 simple，16 个样本，一致性 81%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
