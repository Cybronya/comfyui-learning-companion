---
name: unknown_workflow_sampler_unet_vae_66
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.847
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json, 图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json, 图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json, 图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json, 图片生成/图生图/Qwen2.1四视图生成器_2101145681154101249.json, 图片生成/图生图/Qwen_image_2.1_图生_2101865996205248513.json, 图片生成/图生图/Qwen_人物四视图生成_2111240527051051009.json, 图片生成/图生图/qwen image 2.1多图编辑_2101719348938362882.json, 图片生成/图生图/【Qwen Image 2.1】单图编辑_2104558675418505218.json, 图片生成/图生图/【Qwen Image 2.1】多图编辑_2104557931218956289.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_66

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1 单图编辑_2102026609086787586.json、图片生成/图生图/Qwen image2.1 多图编辑_2102039500712140802.json、图片生成/图生图/Qwen+image+2.1图片编辑.九宫格_2101870838822817793.json、图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json、图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 11/12 个有
- `QwenImage21Cache` —— 10/12 个有
- `CR Prompt Text` —— 7/12 个有
- `ShowText|pysssss` —— 3/12 个有
- `Anything Everywhere3` —— 2/12 个有
- `CR Text Concatenate` —— 2/12 个有
- `JjkText` —— 2/12 个有
- `RHLLMChatNode` —— 2/12 个有
- `ResizeLongestToNode` —— 2/12 个有
- `SaveImageAdvanced` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `TextGenerate` —— 2/12 个有
- `BatchImagesNode` —— 1/12 个有
- `CR Text` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1024 | 1024 - 1024 | 12 | 100% |
| 采样步数 | 25 | 25 - 50 | 12 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 50，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
