---
name: unknown_workflow_controlnet_ipadapter_sampler_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.903
common_nodes: [AIO_Preprocessor, BrushNet, BrushNetLoader, CLIPTextEncode, CR Latent Batch Size, CR Text Concatenate, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, ImageScale, InvertMask, KSampler, LoadImage, MaskToImage, PrepImageForClipVision, PreviewImage, SAMModelLoader (segment anything), SaveImage, ShowText|pysssss, TextInput_, VAEDecode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/一键直出 家具效果图_2035283572994609153.json, 平台全量/一键直出家具效果图_1900639325812310018.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_sampler_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键直出 家具效果图_2035283572994609153.json、平台全量/一键直出家具效果图_1900639325812310018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `ImageScale`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SaveImage`
- `ShowText|pysssss`
- `TextInput_`
- `VAEDecode`
- `WD14Tagger|pysssss`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
