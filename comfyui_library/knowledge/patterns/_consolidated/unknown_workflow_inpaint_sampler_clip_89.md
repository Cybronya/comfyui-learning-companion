---
name: unknown_workflow_inpaint_sampler_clip_89
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.908667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商中国模特换外国模特V1.0_1939244320555769858.json, 平台全量/电商之女鞋增加腿模展示_1934184802910429186.json, 平台全量/电商假人服装模特转真人_1913783251628978178.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_89

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/电商中国模特换外国模特V1.0_1939244320555769858.json、平台全量/电商之女鞋增加腿模展示_1934184802910429186.json、平台全量/电商假人服装模特转真人_1913783251628978178.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/3 个有
- `MaskComposite` —— 2/3 个有
- `RepeatLatentBatch` —— 2/3 个有
- `BiRefNet_ModelLoader_Zho` —— 1/3 个有
- `BiRefNet_Zho` —— 1/3 个有
- `LayerMask: BiRefNetUltra` —— 1/3 个有
- `LoraLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 3 | 90% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
