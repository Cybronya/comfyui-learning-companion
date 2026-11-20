---
name: unknown_workflow_clip_unet_vae_16
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.7265
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyFlux2LatentImage, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, SaveImage, StringReplace, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ernie-Image 文生图_2058025483396272130.json, 图片生成/文生图/Ernie_image_base-目前最好的开源文生图模型_2045741550596005889.json, 图片生成/文生图/Ernie_image_turbo+base-目前最好的开源文生图模型_2045748751431634945.json, 图片生成/文生图/Ernie_image_turbo-目前最好的开源文生图模型_2045716280753262593.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Ernie-Image 文生图_2058025483396272130.json、图片生成/文生图/Ernie_image_base-目前最好的开源文生图模型_2045741550596005889.json、图片生成/文生图/Ernie_image_turbo+base-目前最好的开源文生图模型_2045748751431634945.json、图片生成/文生图/Ernie_image_turbo-目前最好的开源文生图模型_2045716280753262593.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyFlux2LatentImage`
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
- `CustomAddLabel` —— 3/4 个有
- `KSampler` —— 3/4 个有
- `TTResolutionSelector` —— 3/4 个有
- `IntToText` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Primitive string multiline [Crystools]` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 3 | 32% |
| Prompt 约束强度(CFG) | 4 | 1 - 20 | 4 | 0% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，3 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 20，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
