---
name: image_to_image_controlnet_ipadapter_sampler_11
type: Image To Image
frequency: 2
level: weak
coverage: 0.897
common_nodes: [Anything Everywhere3, CLIPTextEncode, CR Text, CR Text Concatenate, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, DepthAnythingPreprocessor, DifferentialDiffusion, EG_TX_SFBLS, IPAdapterAdvanced, IPAdapterUnifiedLoader, KSampler, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [平台全量/照片风格转绘V3_1921607127893229569.json, 平台全量/照片风格转绘_1921568236020645889.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/照片风格转绘V3_1921607127893229569.json、平台全量/照片风格转绘_1921568236020645889.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `DifferentialDiffusion`
- `EG_TX_SFBLS`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `INPAINT_VAEEncodeInpaintConditioning` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 57% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
