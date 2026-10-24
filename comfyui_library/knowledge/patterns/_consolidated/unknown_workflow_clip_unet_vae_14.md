---
name: unknown_workflow_clip_unet_vae_14
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.7136
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, PreviewAny, PrimitiveStringMultiline, SaveImage, StringReplace, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ernie-Image 文生图_2058025483396272130.json, 图片生成/文生图/ernie_image_2045033376498851842.json, 图片生成/文生图/ernie_image_turbo_2044689554212392961.json, 图片生成/文生图/ernie_image_自动扩写提示词_2045358547906596865.json, 图片生成/文生图/image_ernie_image_two_stage_2045034723260502018.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Ernie-Image 文生图_2058025483396272130.json、图片生成/文生图/ernie_image_2045033376498851842.json、图片生成/文生图/ernie_image_turbo_2044689554212392961.json、图片生成/文生图/ernie_image_自动扩写提示词_2045358547906596865.json、图片生成/文生图/image_ernie_image_two_stage_2045034723260502018.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImage`
- `StringReplace`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `KSampler` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `IntToText` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `Primitive string multiline [Crystools]` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 8 - 50 | 4 | 42% |
| Prompt 约束强度(CFG) | 4 | 1 - 20 | 5 | 0% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 35，观测区间 8 - 50，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 20，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
