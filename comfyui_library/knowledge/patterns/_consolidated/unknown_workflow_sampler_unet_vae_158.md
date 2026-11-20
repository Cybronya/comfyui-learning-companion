---
name: unknown_workflow_sampler_unet_vae_158
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.81675
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 精准完美抠图｜自动修复遮挡区域_2104051381421305858.json, 图片生成/图生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2101702190703407106.json, 图片生成/图生图/Qwen Image 2.1自动分镜 短剧分镜_2102191085471752193.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2101818506256932866.json, 图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡_2104462379441549314.json, 图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2104044741108260865.json, 图片生成/图生图/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2114878025723629570.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_158

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 精准完美抠图｜自动修复遮挡区域_2104051381421305858.json、图片生成/图生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json、图片生成/图生图/Qwen Image 2.1多图编辑_2101702190703407106.json、图片生成/图生图/Qwen Image 2.1自动分镜 短剧分镜_2102191085471752193.json、图片生成/图生图/Qwen Image 2.1：图像编辑_2101818506256932866.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `SaveImageAdvanced` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `Text Multiline` —— 4/8 个有
- `XinbaoImageStandardizer` —— 4/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `ImageConcanate` —— 3/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `StringToAnyNode` —— 2/8 个有
- `easy boolean` —— 2/8 个有
- `easy ifElse` —— 2/8 个有
- `ttN concat` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `Text Concatenate` —— 1/8 个有
- `Text Find and Replace` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 8 | 37% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1200 | 8 | 94% |
| 高度 | 1024 | 1024 - 1200 | 8 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1200，8 个样本，取值集中（一致性 94%）
- 高度 中位数 1024，观测区间 1024 - 1200，8 个样本，取值集中（一致性 94%）
