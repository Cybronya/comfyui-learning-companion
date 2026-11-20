---
name: unknown_workflow_sampler_unet_vae_64
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.805357
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json, 图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json, 图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json, 图片生成/图生图/Qwen-image-2.1-单图编辑_2104464258397462529.json, 图片生成/图生图/Qwen2.1四视图生成器_2101145681154101249.json, 图片生成/图生图/Qwen_Image_2.1_图像编辑_2105116270961192961.json, 图片生成/图生图/Qwen_Image_2.1_图像编辑_2105493174088192002.json, 图片生成/图生图/Qwen_Image_2.1_｜生图及编辑_2109445975751352321.json, 图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json, 图片生成/图生图/qwen_image_2_1_图像编辑-文本换装_2104452144555450369.json, 图片生成/图生图/qwen_image_2_1_手持指定物品_2104438895411818497.json, 图片生成/文生图/Qwen_Image_2.1_文生图_6步加速无PE_2107979311847399426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_64

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json、图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json、图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json、图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json、图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 13/14 个有
- `LoadImage` —— 13/14 个有
- `QwenImage21Cache` —— 13/14 个有
- `ResolutionSelector` —— 13/14 个有
- `PrimitiveStringMultiline` —— 6/14 个有
- `EmptyImage` —— 5/14 个有
- `PreviewImage` —— 5/14 个有
- `SaveImageAdvanced` —— 5/14 个有
- `CR Prompt Text` —— 3/14 个有
- `LoraLoaderModelOnly` —— 3/14 个有
- `RHLLMChatNode` —— 2/14 个有
- `ResizeLongestToNode` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 14 | 76% |
| 高度 | 1024 | 1024 - 2048 | 14 | 76% |
| 采样步数 | 25 | 6 - 50 | 14 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 14 | 45% |
| 采样算法 | euler | - | 14 | 93% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2048，14 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，14 个样本
- 采样步数 中位数 25，观测区间 6 - 50，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，14 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
