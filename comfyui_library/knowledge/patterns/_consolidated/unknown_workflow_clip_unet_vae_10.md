---
name: unknown_workflow_clip_unet_vae_10
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.717429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, PreviewAny, PrimitiveStringMultiline, SaveImage, StringReplace, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen3.5反推提示词+ernie_image_turbo_2046120898310180865.json, 图片生成/文生图/ernie_image_2045033376498851842.json, 图片生成/文生图/ernie_image_turbo_2044689554212392961.json, 图片生成/文生图/ernie_image_自动扩写提示词_2045358547906596865.json, 图片生成/文生图/image_ernie_image_two_stage_2045034723260502018.json, 图片生成/文生图/百度Ernie-Image文生图工作流（提示词优化）_2045138689319247873.json, 图片生成/文生图/百度官方工作流ernie_image_turbo_2044767600005095425.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen3.5反推提示词+ernie_image_turbo_2046120898310180865.json、图片生成/文生图/ernie_image_2045033376498851842.json、图片生成/文生图/ernie_image_turbo_2044689554212392961.json、图片生成/文生图/ernie_image_自动扩写提示词_2045358547906596865.json、图片生成/文生图/image_ernie_image_two_stage_2045034723260502018.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ComfySwitchNode` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `KSampler` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `KSamplerAdvanced` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 6 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 7 | 0% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，6 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
