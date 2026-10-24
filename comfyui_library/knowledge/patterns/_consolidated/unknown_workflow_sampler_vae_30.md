---
name: unknown_workflow_sampler_vae_30
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.799111
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 编辑 _ 纯净官流40步无PE_2102038528808013825.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2101702190703407106.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2101818506256932866.json, 图片生成/图生图/Qwen Image2.1图生图_2101893351074258945.json, 图片生成/图生图/Qwen Image2.1图生图_2103754247337762818.json, 图片生成/图生图/Qwen+image+2.1图片编辑-mums_2102062409107202049.json, 图片生成/图生图/Qwen_Image_2.1自动分镜_短剧分镜_2102322312635834369.json, 图片生成/图生图/qwen image 2.1 多图编辑 gguf 版_2101760247470841857.json, 图片生成/图生图/qwen_image_2.1-最强单图编辑无偏移_2104768411694878722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 编辑 _ 纯净官流40步无PE_2102038528808013825.json、图片生成/图生图/Qwen Image 2.1多图编辑_2101702190703407106.json、图片生成/图生图/Qwen Image 2.1：图像编辑_2101818506256932866.json、图片生成/图生图/Qwen Image2.1图生图_2101893351074258945.json、图片生成/图生图/Qwen Image2.1图生图_2103754247337762818.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 8/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `SaveImageAdvanced` —— 5/9 个有
- `PreviewImage` —— 4/9 个有
- `Text` —— 4/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `Fast Bypasser (rgthree)` —— 1/9 个有
- `PixaromaRunTimer` —— 1/9 个有
- `PixaromaSeed` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 9 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1024 | 1024 - 1024 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
