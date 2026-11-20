---
name: text_to_image_sampler_clip_unet_200
type: Text To Image
frequency: 3
level: strong
coverage: 0.496333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, KSampler, PreviewAny, PreviewImage, ResolutionSelector, SaveImage, SetNode, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MOSS-Image 文生图_2108772466398158849.json, 图片生成/文生图/MOSS-Image 用 BBox 安排画面元素_2108928021003595778.json, 图片生成/文生图/MOSS-Image文生图工作流｜一句话直出高质量AI图片_2114621205297848321.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_200

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MOSS-Image 文生图_2108772466398158849.json、图片生成/文生图/MOSS-Image 用 BBox 安排画面元素_2108928021003595778.json、图片生成/文生图/MOSS-Image文生图工作流｜一句话直出高质量AI图片_2114621205297848321.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `PreviewAny`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `TextGenerate` —— 2/3 个有
- `CreateBoundingBoxes` —— 1/3 个有
- `Ideogram4PromptBuilderKJ` —— 1/3 个有
- `MOSSImageLayoutPrompt` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 50 | 50 - 50 | 3 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3 - 3.5 | 3 | 93% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3 - 3.5，3 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
