---
name: image_to_image_controlnet_sampler_clip_25
type: Image To Image
frequency: 2
level: weak
coverage: 0.904
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetLoader, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/野猪A6-电商产品光影融合V5_2004153498461741057.json, 视频生成/图生视频/Kontext姿态控制_1961408250308661250.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/野猪A6-电商产品光影融合V5_2004153498461741057.json、视频生成/图生视频/Kontext姿态控制_1961408250308661250.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Latent Batch Size` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetApplySD3` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `DepthAnythingPreprocessor` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SDXLEmptyLatentSizePicker+` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.95 | - | 2 | 74% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1280x768 (1.67) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.95，样本不足，未给区间，2 个样本
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
