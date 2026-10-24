---
name: unknown_workflow_sampler_unet_vae_80
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.801727
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1_三视图+多表情+多视角_2109917911023439874.json, 图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json, 图片生成/图生图/Qwen Image 2.1去除ai感_2102264547909390337.json, 图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json, 图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json, 图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2108369878913740801.json, 图片生成/图生图/一键三视图+多表情+多视角！Qwen Image 2.1！B站艾橘溪_2109323918157897729.json, 图片生成/图生图/一键生成三视图+多表情+多视角！Qwen Image 2.1_2109583908793835521.json, 图片生成/图生图/一键生成三视图+多表情+多视角！Qwen Image 2.1_2109608921911611394.json, 图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json, 图片生成/文生图/角色设定集丨Qwen Image 2.1丨多视图·表情·姿态_2112093133474459649.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_80

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1_三视图+多表情+多视角_2109917911023439874.json、图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json、图片生成/图生图/Qwen Image 2.1去除ai感_2102264547909390337.json、图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json、图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 10/11 个有
- `ImageStitch` —— 10/11 个有
- `QwenImage21Cache` —— 10/11 个有
- `ResolutionSelector` —— 8/11 个有
- `JjkText` —— 7/11 个有
- `PrimitiveFloat` —— 5/11 个有
- `ImageScaleToTotalPixels` —— 3/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `Anything Everywhere3` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2368 | 11 | 68% |
| 高度 | 1024 | 1024 - 2048 | 11 | 66% |
| 采样步数 | 25 | 25 - 40 | 11 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2368，11 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，11 个样本
- 采样步数 中位数 25，观测区间 25 - 40，11 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
