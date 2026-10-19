---
name: unknown_workflow_controlnet_sampler_clip_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.752
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, Image Comparer (rgthree), ImageConcanate, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1961108839028428802.json, 图片生成/文生图/1965617902089027586.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1961108839028428802.json、图片生成/文生图/1965617902089027586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.875 | - | 2 | 86% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 57% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.875，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: LoadJoyCaptionBeta1Model、LayerUtility: ImageScaleByAspectRatio V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
