---
name: image_to_image_lora_sampler_unet_203
type: Image To Image
frequency: 2
level: weak
coverage: 0.9315
common_nodes: [CFGNorm, CLIPLoader, CropByMask_UTK, Fast Groups Bypasser (rgthree), FastCanvas, FastCanvasTool, ImageRemoveAlpha_UTK, ImageScaleByAspectRatio_UTK, KSampler, LayerUtility: SaveImagePlus, LayerUtility: TextBox, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PurgeVRAM_UTK, TextBoxNode_UTK, TextConcatenate_UTK, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit指定位置双图融合、短视频短剧分镜、电商设计_1959589877602004993.json, 图片生成/图生图/Qwen_高级替换融合_1959539293326880770.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_203

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit指定位置双图融合、短视频短剧分镜、电商设计_1959589877602004993.json、图片生成/图生图/Qwen_高级替换融合_1959539293326880770.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CropByMask_UTK`
- `Fast Groups Bypasser (rgthree)`
- `FastCanvas`
- `FastCanvasTool`
- `ImageRemoveAlpha_UTK`
- `ImageScaleByAspectRatio_UTK`
- `KSampler`
- `LayerUtility: SaveImagePlus`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PurgeVRAM_UTK`
- `TextBoxNode_UTK`
- `TextConcatenate_UTK`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcatenateMulti_UTK` —— 1/2 个有
- `ImageConcatenate_UTK` —— 1/2 个有
- `ImageCropper` —— 1/2 个有
- `ImageScaleRestore_UTK` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `RestoreCropBox_UTK` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TorchCompileModel` —— 1/2 个有
- `easy imageSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
