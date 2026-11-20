---
name: unknown_workflow_lora_sampler_unet_129
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.841167
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit 人物一致性参考_1970748764862488577.json, 图片生成/图生图/Qwen image Edit 免费修图神器，中文识别能力超强_1959933347139104770.json, 图片生成/图生图/与财神握手LoRA——Qwen-Image-Edit应用_1960877013387153409.json, 图片生成/图生图/人或者物铜像化——Qwen-Image-Edit的LoRA应用_1958111693622693889.json, 图片生成/文生图/兵马俑LoRA——Qwen-Image-Edit应用_1963214327899721729.json, 平台全量/QwenImageEdit-参考上下文图片换装_1960210253453406209.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_129

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen edit 人物一致性参考_1970748764862488577.json、图片生成/图生图/Qwen image Edit 免费修图神器，中文识别能力超强_1959933347139104770.json、图片生成/图生图/与财神握手LoRA——Qwen-Image-Edit应用_1960877013387153409.json、图片生成/图生图/人或者物铜像化——Qwen-Image-Edit的LoRA应用_1958111693622693889.json、图片生成/文生图/兵马俑LoRA——Qwen-Image-Edit应用_1963214327899721729.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `ImageStitch` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoadImageFromUrl` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy imageScaleDownBy` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 30 | 6 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 35% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 768 - 1920 | 6 | 68% |
| 高度 | 1024 | 1024 - 1536 | 6 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 30，6 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1920，6 个样本
- 高度 中位数 1024，观测区间 1024 - 1536，6 个样本，取值集中（一致性 83%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
