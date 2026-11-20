---
name: image_to_image_controlnet_upscale_lora_16
type: Image To Image
frequency: 2
level: weak
coverage: 0.862
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, ControlNetLoaderAdvanced, ImageScaleBy, ImageUpscaleWithModel, KSampler, KSampler (Efficient), LineArtPreprocessor, LoadImage, LoraLoader, MiDaS-DepthMapPreprocessor, ModelSamplingDiscrete, PreviewImage, SaveImage, TilePreprocessor, Upscale Model Loader, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/建筑福音！设计稿一键出效果图_1892172241784971266.json, 平台全量/建筑设计稿上色_1879376265605013506.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/建筑福音！设计稿一键出效果图_1892172241784971266.json、平台全量/建筑设计稿上色_1879376265605013506.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ControlNetLoaderAdvanced`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSampler (Efficient)`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader`
- `MiDaS-DepthMapPreprocessor`
- `ModelSamplingDiscrete`
- `PreviewImage`
- `SaveImage`
- `TilePreprocessor`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 5 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | lcm | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.35 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.45，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
