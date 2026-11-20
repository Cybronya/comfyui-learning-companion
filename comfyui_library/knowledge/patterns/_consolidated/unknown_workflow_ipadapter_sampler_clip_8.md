---
name: unknown_workflow_ipadapter_sampler_clip_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.83
common_nodes: [Anything Everywhere3, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, IPAdapterMS, IPAdapterUnifiedLoader, ImageConcanate, JjkText, KSampler (Efficient), LoadImage, PrepImageForClipVision, PreviewImage, SaveImage, Seed Everywhere, StyleAlignedBatchAlign, TextCombinerSix, VAELoader, WD14Tagger|pysssss, easy seed]
problems: []
missing: []
members: [平台全量/多巴胺人像贴纸_1813523574807261186.json, 平台全量/穆夏风格人物_1813140577016799233.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/多巴胺人像贴纸_1813523574807261186.json、平台全量/穆夏风格人物_1813140577016799233.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `IPAdapterMS`
- `IPAdapterUnifiedLoader`
- `ImageConcanate`
- `JjkText`
- `KSampler (Efficient)`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `SaveImage`
- `Seed Everywhere`
- `StyleAlignedBatchAlign`
- `TextCombinerSix`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ApplyInstantID` —— 1/2 个有
- `ApplyPulid` —— 1/2 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 1/2 个有
- `BRIA_RMBG_Zho` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `InstantIDFaceAnalysis` —— 1/2 个有
- `InstantIDModelLoader` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `PulidEvaClipLoader` —— 1/2 个有
- `PulidInsightFaceLoader` —— 1/2 个有
- `PulidModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
