---
name: image_to_image_upscale_lora_sampler_131
type: Image To Image
frequency: 2
level: weak
coverage: 0.807
common_nodes: [CLIPTextEncode, ColorMatch, ConditioningZeroOut, DF_Float, DualCLIPLoader, DyPE_FLUX, FluxGuidance, GetImageSize, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSampler, Light-Tool: TextConnect, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy promptLine]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/高清真实还原人像修复-皮肤质感_1990767072382758913.json, 平台全量/保留原细节高清放大-flux-Dype-srpo-TTP_1986818814820167682.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_131

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高清真实还原人像修复-皮肤质感_1990767072382758913.json、平台全量/保留原细节高清放大-flux-Dype-srpo-TTP_1986818814820167682.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `DF_Float`
- `DualCLIPLoader`
- `DyPE_FLUX`
- `FluxGuidance`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `Light-Tool: TextConnect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy imageSizeByLongerSide` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 0.4 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
