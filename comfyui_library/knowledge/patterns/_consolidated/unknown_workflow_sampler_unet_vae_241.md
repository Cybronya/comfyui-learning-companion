---
name: unknown_workflow_sampler_unet_vae_241
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7874
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/[Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2114264059032989698.json, 图片生成/反推提示词/[Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2115293263048568834.json, 图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json, 图片生成/图生图/Qwen-2.1cos角色生活自拍_2104713076036689921.json, 图片生成/文生图/[Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_241

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/[Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2114264059032989698.json、图片生成/反推提示词/[Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2115293263048568834.json、图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json、图片生成/图生图/Qwen-2.1cos角色生活自拍_2104713076036689921.json、图片生成/文生图/[Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `QwenImage21Cache` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `RHLLMChatNode` —— 3/5 个有
- `Seed (rgthree)` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Text` —— 3/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 40 | 25 - 40 | 5 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 40，5 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
