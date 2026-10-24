---
name: image_to_image_controlnet_sampler_clip_9
type: Image To Image
frequency: 4
level: strong
coverage: 0.80525
common_nodes: [ApplyInstantIDAdvanced, ApplyPulid, Bounded Image Blend, Bounded Image Crop with Mask, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, DifferentialDiffusion, ImageRandomTransform+, ImageToMask, ImpactMakeImageBatch, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JWMaskResize, KSampler, LayerMask: MaskEdgeUltraDetail V2, LayerMask: MaskGrow, LoadImage, Mask Fill Holes, MaskToImage, PreviewImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, ReActorFaceSwap, RemapMaskRange, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, easy imageSize, easy int, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193.json, 图片生成/图生图/无损高质量换脸 一键生图系列_1917029740136566785.json, 图片生成/图生图/精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097.json, 图片生成/图生图/高质量换脸急速版_1907053889483333633.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193.json、图片生成/图生图/无损高质量换脸 一键生图系列_1917029740136566785.json、图片生成/图生图/精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097.json、图片生成/图生图/高质量换脸急速版_1907053889483333633.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyInstantIDAdvanced`
- `ApplyPulid`
- `Bounded Image Blend`
- `Bounded Image Crop with Mask`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `ImageRandomTransform+`
- `ImageToMask`
- `ImpactMakeImageBatch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `JWMaskResize`
- `KSampler`
- `LayerMask: MaskEdgeUltraDetail V2`
- `LayerMask: MaskGrow`
- `LoadImage`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `ReActorFaceSwap`
- `RemapMaskRange`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `easy imageSize`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `BboxDetectorSEGS` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `LayerMask: MaskPreview` —— 2/4 个有
- `LayerMask: PersonMaskUltra V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `PMRF` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `SAMDetectorCombined` —— 2/4 个有
- `SAMLoader` —— 2/4 个有
- `SeedVR2` —— 2/4 个有
- `UltralyticsDetectorProvider` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `FaceAnalysisModels` —— 1/4 个有
- `FaceEmbedDistance` —— 1/4 个有
- `SUPIR_Upscale` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1.4 | 1.4 - 1.5 | 4 | 97% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 0.44 | 0.44 - 0.5 | 4 | 94% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.4，观测区间 1.4 - 1.5，4 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 0.44，观测区间 0.44 - 0.5，4 个样本，取值集中（一致性 94%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
