---
name: unknown_workflow_controlnet_lora_sampler_27
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.781
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DepthAnythingV2Preprocessor, EmptySD3LatentImage, FluxGuidance, ImageResizeKJ, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoader, PreviewImage, SaveImage, VAEDecode, easy imageSize]
problems: []
missing: []
members: [平台全量/Flux Controlnet(Native)_1887052581682728961.json, 平台全量/Flux 粘土风格生成器_1839390374396919809.json, 平台全量/Flux一键3D 皮克斯风格 3D pixar style_1845884322623713281.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Flux Controlnet(Native)_1887052581682728961.json、平台全量/Flux 粘土风格生成器_1839390374396919809.json、平台全量/Flux一键3D 皮克斯风格 3D pixar style_1845884322623713281.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LayerUtility: TextJoin` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `LayerMask: LoadFlorence2Model` —— 1/3 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.4 - 1 | 3 | 66% |
| 采样步数 | 20 | 12 - 20 | 3 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.4 - 1，3 个样本
- 采样步数 中位数 20，观测区间 12 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
