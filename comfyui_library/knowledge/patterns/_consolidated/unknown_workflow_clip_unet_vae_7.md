---
name: unknown_workflow_clip_unet_vae_7
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.747625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, PreviewAny, SaveImage, StringReplace, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ERNIE-Image-turbo 文生图_2044607804283035649.json, 图片生成/文生图/Ernie Turbo文生图自动提示词优化极速版V1_2044590644466814977.json, 图片生成/文生图/Ernie Turbo文生图自动提示词优化极速版V1_2046109277659602945.json, 图片生成/文生图/Ernie-Image-8步快速出图_2046183724303261698.json, 图片生成/文生图/Ernie_image_base-目前最好的开源文生图模型_2045741550596005889.json, 图片生成/文生图/Ernie_image_turbo+base-目前最好的开源文生图模型_2045748751431634945.json, 图片生成/文生图/Ernie_image_turbo-目前最好的开源文生图模型_2045716280753262593.json, 图片生成/文生图/本地部署ERNIE-Image模型：24G 显存可跑，8 步快速出图！_2044965223928438786.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/ERNIE-Image-turbo 文生图_2044607804283035649.json、图片生成/文生图/Ernie Turbo文生图自动提示词优化极速版V1_2044590644466814977.json、图片生成/文生图/Ernie Turbo文生图自动提示词优化极速版V1_2046109277659602945.json、图片生成/文生图/Ernie-Image-8步快速出图_2046183724303261698.json、图片生成/文生图/Ernie_image_base-目前最好的开源文生图模型_2045741550596005889.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `PreviewAny`
- `SaveImage`
- `StringReplace`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 7/8 个有
- `KSampler` —— 7/8 个有
- `PrimitiveBoolean` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `CustomAddLabel` —— 3/8 个有
- `Int` —— 3/8 个有
- `TTResolutionSelector` —— 3/8 个有
- `KSamplerAdvanced` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 7 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 8 | 0% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
