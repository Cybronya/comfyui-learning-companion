---
name: unknown_workflow_controlnet_sampler_vae_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.509
common_nodes: [Any Switch (rgthree), BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, ControlNetApplyAdvanced, ControlNetLoader, CreateShapeMask, Efficient Loader, GetNode, ICLightConditioning, Image Comparer (rgthree), ImageGaussianBlur, ImageResize+, KSampler (Efficient), LineArtPreprocessor, LoadAndApplyICLightUnet, LoadImage, MaskToImage, PreviewImage, RemapImageRange, SaveImage, SetNode, VAEEncode]
problems: []
missing: []
members: [平台全量/IC-Light原点光源重打光_1808763589718634498.json, 平台全量/商品图重新打光_1821408969393876993.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_vae_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/IC-Light原点光源重打光_1808763589718634498.json、平台全量/商品图重新打光_1821408969393876993.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CreateShapeMask`
- `Efficient Loader`
- `GetNode`
- `ICLightConditioning`
- `Image Comparer (rgthree)`
- `ImageGaussianBlur`
- `ImageResize+`
- `KSampler (Efficient)`
- `LineArtPreprocessor`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `RemapImageRange`
- `SaveImage`
- `SetNode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `BatchPromptSchedule` —— 1/2 个有
- `CR Simple Prompt List` —— 1/2 个有
- `CR Simple Prompt List Keyframes` —— 1/2 个有
- `HD UltimateSDUpscale` —— 1/2 个有
- `IPAdapterFaceID` —— 1/2 个有
- `IPAdapterUnifiedLoaderFaceID` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 75% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | ddim_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 ddim_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
