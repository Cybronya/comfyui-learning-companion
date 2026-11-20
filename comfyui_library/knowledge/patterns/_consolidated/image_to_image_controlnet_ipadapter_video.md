---
name: image_to_image_controlnet_ipadapter_video
type: Image To Image
frequency: 3
level: strong
coverage: 0.923333
common_nodes: [ADE_AnimateDiffLoaderGen1, ADE_StandardUniformContextOptions, AIO_Preprocessor, Anything Everywhere3, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetApplyAdvanced, ControlNetLoaderAdvanced, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageScale, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Vid2Vid 风格迁移_1935000868536426498.json, 视频生成/图生视频/Vid2Vid 风格迁移 _ Style Transfer + IPA & Hotshot XL_1866016887959142402.json, 视频生成/图生视频/视频风格转绘_1915250665046872066.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_video

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Vid2Vid 风格迁移_1935000868536426498.json、视频生成/图生视频/Vid2Vid 风格迁移 _ Style Transfer + IPA & Hotshot XL_1866016887959142402.json、视频生成/图生视频/视频风格转绘_1915250665046872066.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `ADE_AnimateDiffLoaderGen1`
- `ADE_StandardUniformContextOptions`
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoaderAdvanced`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
