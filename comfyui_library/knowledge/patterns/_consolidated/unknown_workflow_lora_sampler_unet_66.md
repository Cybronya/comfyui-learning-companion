---
name: unknown_workflow_lora_sampler_unet_66
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.941556
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511单图参考编辑_bf16-基础工作流_2076904369496346625.json, 图片生成/图生图/FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658.json, 图片生成/图生图/Qwen Image Edit 2511-三图编辑_2004027345054932994.json, 图片生成/图生图/Qwen2511单图参考编辑-基础工作流_2077929626973855745.json, 图片生成/图生图/Qwen2511单图参考编辑-基础工作流_2078293379229773826.json, 图片生成/图生图/QwenEdit——2511_2004160555151728641.json, 图片生成/文生图/FireRed Image Edit 1.1三图输入编辑ComfyUI工作流_2033551521618599938.json, 图片生成/文生图/单图编辑_2003615026718121985.json, 图片生成/文生图/多图编辑_2003474271924043777.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_66

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/2511单图参考编辑_bf16-基础工作流_2076904369496346625.json、图片生成/图生图/FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658.json、图片生成/图生图/Qwen Image Edit 2511-三图编辑_2004027345054932994.json、图片生成/图生图/Qwen2511单图参考编辑-基础工作流_2077929626973855745.json、图片生成/图生图/Qwen2511单图参考编辑-基础工作流_2078293379229773826.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/9 个有
- `ResizeImagesByLongerEdge` —— 3/9 个有
- `TTResolutionSelector` —— 3/9 个有
- `UnetLoaderGGUF` —— 3/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `CR SDXL Aspect Ratio` —— 1/9 个有
- `ImpactImageInfo` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `Textbox` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 9 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，9 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（5/9 个样本）：Steps较低可能导致细节不足
