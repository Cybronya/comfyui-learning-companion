---
name: unknown_workflow_controlnet_lora_sampler_30
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7275
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPTextEncode, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, FluxGuidance, GoogleTranslateTextNode, JJC_JoyCaption, KSampler (Efficient), LayerFilter: HDREffects, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoaderV2, PreviewImage, SaveImage, SetUnionControlNetType, ShowText|pysssss, StringFunction|pysssss, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Nunchaku3.0 明星洗图｜快速出图_1936991256188735489.json, 平台全量/一键运行：Nunchaku CN 3.0 洗图 快速出图_1936964109768495105.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Nunchaku3.0 明星洗图｜快速出图_1936991256188735489.json、平台全量/一键运行：Nunchaku CN 3.0 洗图 快速出图_1936964109768495105.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `GoogleTranslateTextNode`
- `JJC_JoyCaption`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoaderV2`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
