---
name: image_to_image_controlnet_sampler_vae
type: Image To Image
frequency: 2
level: weak
coverage: 0.929
common_nodes: [AIO_Preprocessor, CFGNorm, CLIPLoader, CR Simple Image Compare, ConditioningAverage, ControlNetApplySD3, ControlNetLoader, FluxKontextImageScale, KSampler, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PreviewImage, ReferenceLatent, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwenedit最新双节棍QwenEdit人物姿态控制支持controlnet_nunchaku_1967805080453918722.json, 图片生成/图生图/最新双节棍QwenEdit人物姿态控制支持_1972852575940878338.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_vae

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/qwenedit最新双节棍QwenEdit人物姿态控制支持controlnet_nunchaku_1967805080453918722.json、图片生成/图生图/最新双节棍QwenEdit人物姿态控制支持_1972852575940878338.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CFGNorm`
- `CLIPLoader`
- `CR Simple Image Compare`
- `ConditioningAverage`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy positive`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 0.98 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0.98，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.98，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
