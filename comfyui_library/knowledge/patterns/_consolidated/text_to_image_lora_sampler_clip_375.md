---
name: text_to_image_lora_sampler_clip_375
type: Text To Image
frequency: 2
level: weak
coverage: 0.924
common_nodes: [AILab_QwenVL, AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LayerUtility: ImageScaleByAspectRatio, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 CN控制图生图工作流，文生图图生图控制处理工具_2107990625491709953.json, 图片生成/文生图/krea2-cn控制图生图_2105949894426058753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_375

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2 CN控制图生图工作流，文生图图生图控制处理工具_2107990625491709953.json、图片生成/文生图/krea2-cn控制图生图_2105949894426058753.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 808 | - | 2 | 10% |
| 高度 | 472 | - | 2 | 17% |
| 采样步数 | 7 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 808，样本不足，未给区间，2 个样本，取值分散，一致性仅 10%
- 高度 中位数 472，样本不足，未给区间，2 个样本，取值分散，一致性仅 17%
- 采样步数 中位数 7，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
