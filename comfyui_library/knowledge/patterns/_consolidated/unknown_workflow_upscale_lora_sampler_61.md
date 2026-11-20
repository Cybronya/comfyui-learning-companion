---
name: unknown_workflow_upscale_lora_sampler_61
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.810667
common_nodes: [CLIPLoader, ConditioningZeroOut, DapaoImageCompressionNode, GetImageSize+, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, UpscaleModelLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Qwen2511动漫卡通人物转真人 接入SD-PPP实现 动漫卡通人物转真人_2073594967582396418.json, 图片生成/图生图/🐰Qwen2511 二次元转真实+4K超清放大🐰_2011730884642213889.json, 图片生成/图生图/💥千问2511最强二次元转真人💥_2009220179007381505.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen2511动漫卡通人物转真人 接入SD-PPP实现 动漫卡通人物转真人_2073594967582396418.json、图片生成/图生图/🐰Qwen2511 二次元转真实+4K超清放大🐰_2011730884642213889.json、图片生成/图生图/💥千问2511最强二次元转真人💥_2009220179007381505.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `DapaoImageCompressionNode`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `QwenEditOutputExtractor` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `DapaoSmartMemoryOptimizerNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta57 | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta57，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（2/3 个样本）：发现KSampler但没有VAEDecode
