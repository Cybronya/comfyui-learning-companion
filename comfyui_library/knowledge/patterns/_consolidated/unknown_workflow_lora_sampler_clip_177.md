---
name: unknown_workflow_lora_sampler_clip_177
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.627667
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, EmptySD3LatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, KSampler, Label (rgthree), LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, ReduxAdvanced, SaveImage, SetNode, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2025-04-15-flux-redux-nunchaku-dev_1912071465557028865.json, 图片生成/图生图/2025-04-16 性价比最高的换装流程_1912393569443770370.json, 图片生成/图生图/Nunchaku+Redux换装流程_1917662224092172290.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_177

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2025-04-15-flux-redux-nunchaku-dev_1912071465557028865.json、图片生成/图生图/2025-04-16 性价比最高的换装流程_1912393569443770370.json、图片生成/图生图/Nunchaku+Redux换装流程_1917662224092172290.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `ReduxAdvanced`
- `SaveImage`
- `SetNode`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `GroundingDinoModelLoader (segment anything2)` —— 2/3 个有
- `GroundingDinoSAM2Segment (segment anything2)` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `ImageScaleToMegapixels` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `SAM2ModelLoader (segment anything2)` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
