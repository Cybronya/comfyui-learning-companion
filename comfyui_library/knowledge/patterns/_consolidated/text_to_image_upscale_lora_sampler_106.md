---
name: text_to_image_upscale_lora_sampler_106
type: Text To Image
frequency: 3
level: strong
coverage: 0.932
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, FastFilmGrain, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, LayerColor: BrightnessContrastV2, LoraLoaderModelOnly, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Kook_Zimage_瑶光_2038713096780390402.json, 图片生成/文生图/固定角色：泠月luna。文生图Z-image turbo_2042962433819545602.json, 图片生成/文生图/小姐姐名字：mzqr01。指定该角色 文生图（zimage turbo）_2040783114238173186.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Kook_Zimage_瑶光_2038713096780390402.json、图片生成/文生图/固定角色：泠月luna。文生图Z-image turbo_2042962433819545602.json、图片生成/文生图/小姐姐名字：mzqr01。指定该角色 文生图（zimage turbo）_2040783114238173186.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FastFilmGrain`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LoraLoaderModelOnly`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `KOOK_SaveJPGImage` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `CameraWatermarkNode` —— 1/3 个有
- `DuckHideNode` —— 1/3 个有
- `Int` —— 1/3 个有
- `KOOK_ImageCompression` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `TextInputBasic` —— 1/3 个有
- `ZML_BooleanSwitch` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy getNode` —— 1/3 个有
- `easy setNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | bong_tangent | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 bong_tangent，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
