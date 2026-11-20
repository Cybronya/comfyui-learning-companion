---
name: image_to_image_controlnet_sampler_checkpoint
type: Image To Image
frequency: 8
level: strong
coverage: 0.781
common_nodes: [ApplyInstantIDAdvanced, ApplyPulid, Bounded Image Blend, Bounded Image Crop with Mask, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, DifferentialDiffusion, ImageRandomTransform+, ImageToMask, ImpactMakeImageBatch, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JWMaskResize, KSampler, LayerMask: MaskEdgeUltraDetail V2, LayerMask: MaskGrow, LoadImage, Mask Fill Holes, MaskToImage, PreviewImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, RemapMaskRange, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, easy imageSize, easy int, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193.json, 图片生成/图生图/无损高质量换脸 一键生图系列_1917029740136566785.json, 图片生成/图生图/精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097.json, 图片生成/图生图/高质量换脸急速版_1907053889483333633.json, 平台全量/SDXL 换脸 pullid + instantid_1831147617857269762.json, 平台全量/人物背景姿势不变InstantID+Pulid换脸-_1953716181674938370.json, 平台全量/换脸_1923291547755081729.json, 平台全量/极致换脸_1866825728313753601.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193.json、图片生成/图生图/无损高质量换脸 一键生图系列_1917029740136566785.json、图片生成/图生图/精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097.json、图片生成/图生图/高质量换脸急速版_1907053889483333633.json、平台全量/SDXL 换脸 pullid + instantid_1831147617857269762.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplyInstantIDAdvanced`
- `ApplyPulid`
- `Bounded Image Blend`
- `Bounded Image Crop with Mask`
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
- `RemapMaskRange`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `easy imageSize`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/8 个有
- `Image Comparer (rgthree)` —— 7/8 个有
- `ReActorFaceSwap` —— 7/8 个有
- `BboxDetectorSEGS` —— 5/8 个有
- `MaskPreview+` —— 5/8 个有
- `SAMDetectorCombined` —— 5/8 个有
- `SAMLoader` —— 5/8 个有
- `UltralyticsDetectorProvider` —— 5/8 个有
- `LoraLoader` —— 4/8 个有
- `FaceAnalysisModels` —— 3/8 个有
- `FaceEmbedDistance` —— 3/8 个有
- `ImageConcanate` —— 3/8 个有
- `LayerMask: MaskPreview` —— 3/8 个有
- `LayerMask: PersonMaskUltra V2` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 3/8 个有
- `PMRF` —— 3/8 个有
- `RH_Captioner` —— 3/8 个有
- `SeedVR2` —— 3/8 个有
- `SUPIR_Upscale` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `BNK_CLIPTextEncodeAdvanced` —— 1/8 个有
- `Context (rgthree)` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `UltimateSDUpscale` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1.4 | 0.8 - 1.5 | 8 | 84% |
| 采样算法 | euler_ancestral | - | 8 | 88% |
| 调度器 | sgm_uniform | - | 8 | 88% |
| 重绘幅度 | 0.44 | 0.2 - 0.5 | 8 | 79% |
| LoRA 模型强度 | 1 | 1 - 1.2 | 4 | 92% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.4，观测区间 0.8 - 1.5，8 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 88%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 88%
- 重绘幅度 中位数 0.44，观测区间 0.2 - 0.5，8 个样本
- LoRA 模型强度 中位数 1，观测区间 1 - 1.2，4 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（16/8 个样本）：Steps较低可能导致细节不足
