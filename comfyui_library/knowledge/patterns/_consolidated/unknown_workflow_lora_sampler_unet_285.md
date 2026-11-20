---
name: unknown_workflow_lora_sampler_unet_285
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.858
common_nodes: [ConditioningZeroOut, DiptychCreate, DualCLIPLoader, FluxGuidance, ICEFConditioning, InContextEditInstruction, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/产品变色设计，保持特征不变改变颜色_1942044272684384257.json, 平台全量/王炸@ICEdit（羊叔拆解优化版）_1921094924706463746.json, 平台全量/超强图像编辑处理——ICEdit-MoE图像编辑_1921762622008410113.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_285

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/产品变色设计，保持特征不变改变颜色_1942044272684384257.json、平台全量/王炸@ICEdit（羊叔拆解优化版）_1921094924706463746.json、平台全量/超强图像编辑处理——ICEdit-MoE图像编辑_1921762622008410113.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `DiptychCreate`
- `DualCLIPLoader`
- `FluxGuidance`
- `ICEFConditioning`
- `InContextEditInstruction`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PMRF` —— 2/3 个有
- `easy imageInsetCrop` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageCrop` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有

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
