---
name: unknown_workflow_sampler_clip_unet_312
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7475
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyFlux2LatentImage, KSampler, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, SaveImage, StringReplace, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ernie-Image 文生图_2058025483396272130.json, 图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2044590595057917954.json, 图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2046103550576562177.json, 图片生成/文生图/HS-image_ernie_image_2044628228756742146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_312

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Ernie-Image 文生图_2058025483396272130.json、图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2044590595057917954.json、图片生成/文生图/Ernie文生图自动提示词优化满血版V1_2046103550576562177.json、图片生成/文生图/HS-image_ernie_image_2044628228756742146.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `SaveImage`
- `StringReplace`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `IntToText` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Primitive string multiline [Crystools]` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 20 - 50 | 4 | 57% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，观测区间 20 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
