---
name: text_to_image_sampler_clip_unet_262
type: Text To Image
frequency: 2
level: weak
coverage: 0.4575
common_nodes: [CLIPLoader, CLIPTextEncode, CombineOutputLists, EmptyLatentImage, GetNode, KSampler, PreviewAny, PreviewImage, SaveImage, SetNode, StringFormat, StringOutputList, UNETLoader, VAEDecode, VAELoader, XyzGridPlot]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/ComfyUI 自动化参数测试：用 OutputList 构建 XYZ Plot 对比网格图_2099469982060077058.json, 平台全量/LoRA 批量测试：多 LoRA x 多权重，XYZ 网格图自动对比_2101234635438125057.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_262

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/ComfyUI 自动化参数测试：用 OutputList 构建 XYZ Plot 对比网格图_2099469982060077058.json、平台全量/LoRA 批量测试：多 LoRA x 多权重，XYZ 网格图自动对比_2101234635438125057.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CombineOutputLists`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `PreviewAny`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `StringFormat`
- `StringOutputList`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XyzGridPlot`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `ComfyNumberConvert` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `NumberOutputList` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `SpreadsheetOutputList` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 640 | - | 2 | 40% |
| 高度 | 640 | - | 2 | 40% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 640，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 高度 中位数 640，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
