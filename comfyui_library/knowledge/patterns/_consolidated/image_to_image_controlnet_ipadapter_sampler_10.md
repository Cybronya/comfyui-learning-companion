---
name: image_to_image_controlnet_ipadapter_sampler_10
type: Image To Image
frequency: 2
level: weak
coverage: 0.8065
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, IPAdapterAdvanced, IPAdapterUnifiedLoader, KSampler, LineArtPreprocessor, LoadImage, PrepImageForClipVision, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [平台全量/全自动风格转绘，风格迁移像复制粘贴一样简单_1928070387006095362.json, 平台全量/展陈空间白膜线稿转商业效果图_2091098308143046657.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/全自动风格转绘，风格迁移像复制粘贴一样简单_1928070387006095362.json、平台全量/展陈空间白膜线稿转商业效果图_2091098308143046657.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LineArtPreprocessor`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MiniCPM_VQA` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy imagePixelPerfect` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.675 | - | 2 | 81% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.75 | - | 2 | 95% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.59 | - | 2 | 31% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.675，样本不足，未给区间，2 个样本，取值集中（一致性 81%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.75，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.59，样本不足，未给区间，2 个样本，取值分散，一致性仅 31%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
