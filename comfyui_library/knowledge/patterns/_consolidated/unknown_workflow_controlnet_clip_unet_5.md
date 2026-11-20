---
name: unknown_workflow_controlnet_clip_unet_5
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.432
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, Image Comparer (rgthree), ImageBlur, LoadImage, ModelPatchLoader, PreviewImage, PrimitiveFloat, ResizeImageMaskNode, ResolutionSelector, SaveImage, Seed (rgthree), SetNode, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, ZImageFunControlnet]
problems: []
missing: []
members: [平台全量/[Z-Image Series 03] Controlnet Tile 与 eta_2091879249308381185.json, 平台全量/[eta 04] 以 Krea 2 为例，跨模型复现 ETA 噪声控制_2095123842346868738.json, 平台全量/解锁隐藏的细节！Z-Image 采样进阶：RES4LYF ETA 节点详解 [Series 03.1_2093647464900423681.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/[Z-Image Series 03] Controlnet Tile 与 eta_2091879249308381185.json、平台全量/[eta 04] 以 Krea 2 为例，跨模型复现 ETA 噪声控制_2095123842346868738.json、平台全量/解锁隐藏的细节！Z-Image 采样进阶：RES4LYF ETA 节点详解 [Series 03.1_2093647464900423681.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：43%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageBlur`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `ZImageFunControlnet`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `ClownOptions_SDE_Beta` —— 2/3 个有
- `ClownsharKSampler_Beta` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `SamplerEulerAncestral` —— 2/3 个有
- `SharkOptions_Beta` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `TextBoxConcatenate` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `ClownSampler_Beta` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `GenerateNoise` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `InjectNoiseToLatent` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `LatentNoised` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | simple | - | 2 | 50% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 86% |
| 采样算法 | -1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 simple，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 中位数 -1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
