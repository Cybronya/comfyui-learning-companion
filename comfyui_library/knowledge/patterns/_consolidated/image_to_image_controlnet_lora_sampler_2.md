---
name: image_to_image_controlnet_lora_sampler_2
type: Image To Image
frequency: 2
level: weak
coverage: 0.458
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, GetNode, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, Int, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveBoolean, Qwen3_VQA, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, SetUnionControlNetType, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy imageConcat, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Light-Tool: TextConnect, easy cleanGpuUsed, easy imageBatchToImageList, easy imageConcat, easy imageListToImageBatch, CR SDXL Aspect Ratio, easy promptLine]
members: [图片生成/文生图/1988957962741878786.json, 图片生成/文生图/1988981381072031745.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1988957962741878786.json、图片生成/文生图/1988981381072031745.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `Int`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveBoolean`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `DF_Float` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `DyPE_FLUX` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Light-Tool: TextConnect` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `TTP_Tile_image_size` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy imageBatchToImageList` —— 1/2 个有
- `easy imageListToImageBatch` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 18 | - | 2 | 44% |
| Prompt 约束强度(CFG) | 1.005 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 0.7 | - | 2 | 57% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 18，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1.005，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Light-Tool: TextConnect、easy cleanGpuUsed、easy imageBatchToImageList、easy imageConcat
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
