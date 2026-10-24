---
name: unknown_workflow_sampler_unet_vae_28
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.835471
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json, 图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json, 图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json, 图片生成/图生图/Qwen-image-2.1-单图编辑_2104464258397462529.json, 图片生成/图生图/Qwen2.1四视图生成器_2101145681154101249.json, 图片生成/图生图/Qwen_Image_2.1_图像编辑_2105116270961192961.json, 图片生成/图生图/Qwen_Image_2.1_图像编辑_2105493174088192002.json, 图片生成/图生图/Qwen_人物四视图生成_2111240527051051009.json, 图片生成/图生图/qwen image 2.1 图编辑_2102212148364668930.json, 图片生成/图生图/qwen-image 2.1图像编辑_2101777177351122945.json, 图片生成/图生图/qwen-image-2.1图像编辑_2101918037409615874.json, 图片生成/图生图/qwen-image2.1 一键图片自动透明分层_2109549307715211265.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2109541250159435778.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112365438872154113.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_28

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json、图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json、图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json、图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json、图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 16/17 个有
- `ResolutionSelector` —— 16/17 个有
- `QwenImage21Cache` —— 15/17 个有
- `LoadImage` —— 14/17 个有
- `CR Prompt Text` —— 7/17 个有
- `SaveImageAdvanced` —— 6/17 个有
- `LoraLoaderModelOnly` —— 4/17 个有
- `PrimitiveStringMultiline` —— 4/17 个有
- `QwenPERewriteT8` —— 4/17 个有
- `Color Grading JK` —— 3/17 个有
- `RHLLMChatNode` —— 3/17 个有
- `easy showAnything` —— 3/17 个有
- `ShowText|pysssss` —— 2/17 个有
- `ResizeLongestToNode` —— 1/17 个有
- `easy promptLine` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 17 | 78% |
| 高度 | 1024 | 1024 - 2048 | 17 | 78% |
| 采样步数 | 25 | 7 - 50 | 17 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2048，17 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，17 个样本
- 采样步数 中位数 25，观测区间 7 - 50，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
