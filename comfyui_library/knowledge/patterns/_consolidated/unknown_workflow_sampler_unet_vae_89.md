---
name: unknown_workflow_sampler_unet_vae_89
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.813583
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1-图生图-V1_2101853390769840130.json, 图片生成/图生图/Qwen image 2.1-图生图-V1_2114660896239874049.json, 图片生成/图生图/Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113.json, 图片生成/图生图/Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274.json, 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表-V2_2108915941747810306.json, 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json, 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2114358796133953538.json, 图片生成/图生图/Qwen image 2.1多图编辑｜人物面部与全身三视图角色表一键出_2114672656506245121.json, 图片生成/图生图/Qwen-image2.1  多图像编辑工作流V2_2102399015068454914.json, 图片生成/图生图/Qwen_image_2.1-图生图-角色四视图-V1.1_2114880341025574914.json, 图片生成/图生图/Qwenimage2.1 图像编辑工作流_2101869615268847617.json, 图片生成/图生图/qwen image 2.1多图编辑_2101819535304253442.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_89

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1-图生图-V1_2101853390769840130.json、图片生成/图生图/Qwen image 2.1-图生图-V1_2114660896239874049.json、图片生成/图生图/Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113.json、图片生成/图生图/Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274.json、图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表-V2_2108915941747810306.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 11/12 个有
- `easy showAnything` —— 11/12 个有
- `BatchImagesNode` —— 9/12 个有
- `CR Text` —— 6/12 个有
- `PrimitiveStringMultiline` —— 6/12 个有
- `StringConcatenate` —— 6/12 个有
- `孤海注释` —— 4/12 个有
- `PrimitiveBoolean` —— 3/12 个有
- `ZNGB_ImageBatchMulti` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `NanFengH3LimitImageLongEdge` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `RHLLMChatNode` —— 1/12 个有
- `SaveImageAdvanced` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 25 - 50 | 12 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1024 | 1024 - 1024 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 25 - 50，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
