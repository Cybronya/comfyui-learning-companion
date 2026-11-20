---
name: unknown_workflow_sampler_unet_vae_120
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.9407
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/boogu-edit-单图编辑_2068181907355029506.json, 图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json, 图片生成/图生图/小红书二图编辑(适用换装)_2034643139293618177.json, 图片生成/图生图/服装提取-上下_2038138778417635330.json, 图片生成/图生图/服装提取-前后上下_2038448443059871745.json, 图片生成/文生图/Qwen 手机上的3D广州_2032029277100707841.json, 图片生成/文生图/Qwen 手机上的3D深圳_2032032800974577666.json, 图片生成/文生图/动作编辑器应用之四__FireRed文生图_2021382520541028354.json, 平台全量/Qwen 2509_精准镜头控制之四_电商产品的SAM 3D Object应用_1994242457594429442.json, 平台全量/Qwen_Edit_2509一键白膜转材质LoRA_1985491458713075714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_120

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/boogu-edit-单图编辑_2068181907355029506.json、图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json、图片生成/图生图/小红书二图编辑(适用换装)_2034643139293618177.json、图片生成/图生图/服装提取-上下_2038138778417635330.json、图片生成/图生图/服装提取-前后上下_2038448443059871745.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `ModelSamplingAuraFlow` —— 9/10 个有
- `TextEncodeQwenImageEditPlus` —— 9/10 个有
- `CFGNorm` —— 8/10 个有
- `LoadImage` —— 8/10 个有
- `FluxKontextImageScale` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `GetImageSize` —— 2/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `GetImage` —— 1/10 个有
- `TextEncodeBooguEdit` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 10 | 78% |
| 高度 | 1024 | 512 - 1280 | 10 | 73% |
| 采样步数 | 6 | 4 - 30 | 10 | 8% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 10 | 40% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，10 个样本
- 高度 中位数 1024，观测区间 512 - 1280，10 个样本
- 采样步数 中位数 6，观测区间 4 - 30，10 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，10 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（13/10 个样本）：Steps较低可能导致细节不足
