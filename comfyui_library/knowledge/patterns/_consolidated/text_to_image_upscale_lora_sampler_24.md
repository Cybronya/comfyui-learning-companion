---
name: text_to_image_upscale_lora_sampler_24
type: Text To Image
frequency: 9
level: moderate
coverage: 0.915333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen2512 文生图工作流_2071432588077654017.json, 图片生成/文生图/Rika-zit去水印放大真实人像流_2057641336878227458.json, 图片生成/文生图/ZIMAGE-瑶光文生图_2036262515121856513.json, 图片生成/文生图/Zimage-瑶光文生图工作流_2048264071597789186.json, 图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078417819166920705.json, 图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078469610759872514.json, 图片生成/文生图/Zimage_瑶光-真实人像与海报_2034978396467367938.json, 图片生成/文生图/Zimage_真实人像与海报+qwen3.5 反推 无限制_2035586422165475330.json, 图片生成/文生图/Zimage强化+瑶光+晓玉V3（文生图）_2042119298440765442.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Qwen2512 文生图工作流_2071432588077654017.json、图片生成/文生图/Rika-zit去水印放大真实人像流_2057641336878227458.json、图片生成/文生图/ZIMAGE-瑶光文生图_2036262515121856513.json、图片生成/文生图/Zimage-瑶光文生图工作流_2048264071597789186.json、图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078417819166920705.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 8/9 个有
- `ImageCASharpening+` —— 8/9 个有
- `RunningHub Deepcleaner` —— 8/9 个有
- `CR Text` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `FastFilmGrain` —— 5/9 个有
- `LayerColor: BrightnessContrastV2` —— 5/9 个有
- `PreviewImage` —— 4/9 个有
- `KOOK_SaveJPGImage` —— 3/9 个有
- `PhotoShakeNode` —— 3/9 个有
- `LoadImage` —— 2/9 个有
- `llama_cpp_instruct_adv` —— 2/9 个有
- `llama_cpp_model_loader` —— 2/9 个有
- `llama_cpp_parameters` —— 2/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `CR Text Replace` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `JDCN_StringToList` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `MemoryCleaner` —— 1/9 个有
- `ProcessString` —— 1/9 个有
- `SaveImageToLocal` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `easy imageSize` —— 1/9 个有
- `easy seed` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 9 | 100% |
| 高度 | 1920 | 1384 - 1920 | 9 | 88% |
| 采样步数 | 8 | 8 - 50 | 9 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 29% |
| 采样算法 | res_2s | - | 9 | 56% |
| 调度器 | bong_tangent | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1384 - 1920，9 个样本，取值集中（一致性 88%）
- 采样步数 中位数 8，观测区间 8 - 50，9 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 res_2s，9 个样本，一致性 56%
- 调度器 最常用 bong_tangent，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
