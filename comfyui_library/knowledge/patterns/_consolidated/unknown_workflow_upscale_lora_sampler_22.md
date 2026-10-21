---
name: unknown_workflow_upscale_lora_sampler_22
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.778
common_nodes: [ConditioningZeroOut, DiptychCreate, DualCLIPLoader, FluxGuidance, ICEFConditioning, ImageConcanate, ImageCrop, ImageScaleDownToSize, ImageUpscaleWithModel, InContextEditInstruction, KSamplerAdvanced, LoraLoaderModelOnly, MaskPreview, PreviewImage, SaveImage, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: [Text Multiline, easy cleanGpuUsed]
members: [图片生成/文生图/1920517668280143874.json, 图片生成/文生图/1932629301877424130.json, 视频生成/图生视频/1932629301877424130.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1920517668280143874.json、图片生成/文生图/1932629301877424130.json、视频生成/图生视频/1932629301877424130.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `DiptychCreate`
- `DualCLIPLoader`
- `FluxGuidance`
- `ICEFConditioning`
- `ImageConcanate`
- `ImageCrop`
- `ImageScaleDownToSize`
- `ImageUpscaleWithModel`
- `InContextEditInstruction`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `PreviewImage`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 28 | 28 - 28 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 28，观测区间 28 - 28，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 28，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、easy cleanGpuUsed
