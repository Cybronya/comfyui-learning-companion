---
name: unknown_workflow_sampler_unet_vae_83
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.835182
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen2.1文生图_2101145781234397185.json, 图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json, 图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json, 图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json, 图片生成/文生图/qwen_image2.文生图_2101942968000278530.json, 图片生成/文生图/qwen_image_2.1 _ 文生图_2103128462868443138.json, 图片生成/文生图/千问2.1！ 文生图！ 提示词自动优化！_2103393990568660994.json, 数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json, 数字人/数字人/千问2.1！ 文生图！ 提示词自动优化！_2101851079326658561.json, 视频生成/文生视频/Qwen_image_2.1_文生图_2104447797318733826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_83

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Qwen2.1文生图_2101145781234397185.json、图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json、图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json、图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json、图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 10/11 个有
- `JjkText` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `TextGenerateLTX2Prompt` —— 4/11 个有
- `easy showAnything` —— 4/11 个有
- `FastGroupsBypassSwitch` —— 3/11 个有
- `EmptyImage` —— 2/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `SaveImageAdvanced` —— 1/11 个有
- `TextEncodeQwenImageEditPlus` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 11 | 100% |
| 高度 | 1024 | 1024 - 1024 | 11 | 100% |
| 采样步数 | 25 | 25 - 50 | 11 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，11 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 50，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
