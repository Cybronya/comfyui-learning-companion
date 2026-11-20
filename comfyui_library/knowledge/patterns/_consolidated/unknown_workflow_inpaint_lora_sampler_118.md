---
name: unknown_workflow_inpaint_lora_sampler_118
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPTextEncodeFlux, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [平台全量/Redux+Fill万物迁移【教程】_1996031316145717250.json, 平台全量/万物迁移-物品迁移_1904512724834123777.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_118

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Redux+Fill万物迁移【教程】_1996031316145717250.json、平台全量/万物迁移-物品迁移_1904512724834123777.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `Crop (mtb)` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `MaskFillHoles` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | - | 2 | 75% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
