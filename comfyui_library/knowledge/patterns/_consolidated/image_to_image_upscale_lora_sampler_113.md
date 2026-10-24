---
name: image_to_image_upscale_lora_sampler_113
type: Image To Image
frequency: 2
level: weak
coverage: 0.7255
common_nodes: [Anything Everywhere3, CheckpointLoaderSimple, DepthAnythingV2Preprocessor, EmptyLatentImage, GetNode, IO_clear_cache, Image Blank, ImageBlend, ImageGenResolutionFromImage, ImagePadForOutpaint, ImageUpscaleWithModel, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoadLotusModel, LoraLoaderModelOnly, LotusSampler, PreviewImage, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SetNode, TextEncodeQwenImageEditPlusCustom_lrzjason, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy positive, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen编辑 AIO 12.28_2005157375503990785.json, 图片生成/文生图/千问编辑All In One 12.1_1997564330105323522.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen编辑 AIO 12.28_2005157375503990785.json、图片生成/文生图/千问编辑All In One 12.1_1997564330105323522.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CheckpointLoaderSimple`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `GetNode`
- `IO_clear_cache`
- `Image Blank`
- `ImageBlend`
- `ImageGenResolutionFromImage`
- `ImagePadForOutpaint`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadLotusModel`
- `LoraLoaderModelOnly`
- `LotusSampler`
- `PreviewImage`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy positive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_ImageStitch` —— 1/2 个有
- `AILab_MaskEnhancer` —— 1/2 个有
- `AILab_MaskOverlay` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ImageLoader` —— 1/2 个有
- `ImageLoaderPlus` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `MultiplePathsInput` —— 1/2 个有
- `MultiplePathsInputPlus` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `Qwen3_VQA_Plus` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Switch image [Crystools]` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 100% |
| 高度 | 1276 | - | 2 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1276，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
