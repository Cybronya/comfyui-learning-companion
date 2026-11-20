---
name: unknown_workflow_sampler_unet_vae_271
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.741333
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json, 图片生成/图生图/Qwen2.1图生图工作流_2101875984147509250.json, 图片生成/文生图/Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_271

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json、图片生成/图生图/Qwen2.1图生图工作流_2101875984147509250.json、图片生成/文生图/Qwen Image 2.1自助捏脸生成人物肖像资产_2111410566211391490.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `FacialCustomization` —— 1/3 个有
- `GH_ImageVideoComparer` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `MmuuaiGroupBypass` —— 1/3 个有
- `QwenImage21_T2IPromptRewrite` —— 1/3 个有
- `TextCombinerTwo` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 50 | 3 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 50，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
