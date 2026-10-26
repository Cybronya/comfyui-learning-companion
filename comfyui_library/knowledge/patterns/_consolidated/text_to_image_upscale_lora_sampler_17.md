---
name: text_to_image_upscale_lora_sampler_17
type: Text To Image
frequency: 10
level: strong
coverage: 0.7829
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KOOK_SaveJPGImage, KSampler, LoraLoaderModelOnly, RunningHub Deepcleaner, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万能图像洗图-Zimage_kook瑶光版_2034186472865140737.json, 图片生成/图生图/不花钱的电商海报高清生成_2066449995951333377.json, 图片生成/文生图/Kook_Zimage  最接近真实照片效果的LORA_2034909895190913025.json, 图片生成/文生图/ZB瑶光加密自动优化_2037050547345301505.json, 图片生成/文生图/ZB瑶光加密自动优化极速无扩图_2037071390456680450.json, 图片生成/文生图/Zimage一键生成海报_2034875531174354946.json, 图片生成/文生图/不花钱的电商海报高清生成_2068887981989130242.json, 图片生成/文生图/电商海报高清生成优化版-图片+文字生成-Zimage_2033966725204545538.json, 图片生成/文生图/（自用）ZB瑶光-自写词-无扩图极速版_2037064604660011009.json, 图片生成/文生图/（自用）ZB瑶光-自写词_2037044705757765634.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/万能图像洗图-Zimage_kook瑶光版_2034186472865140737.json、图片生成/图生图/不花钱的电商海报高清生成_2066449995951333377.json、图片生成/文生图/Kook_Zimage  最接近真实照片效果的LORA_2034909895190913025.json、图片生成/文生图/ZB瑶光加密自动优化_2037050547345301505.json、图片生成/文生图/ZB瑶光加密自动优化极速无扩图_2037071390456680450.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_SaveJPGImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `RunningHub Deepcleaner`
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
- `SaveImage` —— 7/10 个有
- `FastFilmGrain` —— 5/10 个有
- `GetNode` —— 5/10 个有
- `Image Comparer (rgthree)` —— 5/10 个有
- `LayerColor: BrightnessContrastV2` —— 5/10 个有
- `RH_LLMAPI_NODE` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `LoadImage` —— 4/10 个有
- `Text` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `PrimitiveBoolean` —— 3/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `TT_img_enc_v2` —— 3/10 个有
- `ZML_SwitchOutput` —— 3/10 个有
- `DapaoPromptNode` —— 2/10 个有
- `Fast Bypasser (rgthree)` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | res_2s | - | 10 | 100% |
| 调度器 | bong_tangent | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 10 | 100% |
| 高度 | 1920 | 1680 - 1920 | 10 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，10 个样本，一致性 100%
- 调度器 最常用 bong_tangent，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1680 - 1920，10 个样本，取值集中（一致性 94%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
