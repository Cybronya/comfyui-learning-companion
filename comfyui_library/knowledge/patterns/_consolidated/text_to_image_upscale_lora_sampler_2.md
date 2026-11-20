---
name: text_to_image_upscale_lora_sampler_2
type: Text To Image
frequency: 28
level: moderate
coverage: 0.942536
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen2512 文生图工作流_2071432588077654017.json, 图片生成/文生图/Rika-zit去水印放大真实人像流_2057641336878227458.json, 图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078417819166920705.json, 图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078469610759872514.json, 图片生成/文生图/Zimage_瑶光_2115573777479323649.json, 图片生成/文生图/Zimage超级真实人像_Kook大佬瑶光lora_2042965185694011394.json, 图片生成/文生图/Zimage超级真实人像_Kook大佬瑶光lora_2052288192912605186.json, 图片生成/文生图/希帆解说漫-人设图生成_2051932454398775297.json, 图片生成/文生图/文生图-艺术人像摄影-Zimage_Kook版_2079401388609724418.json, 图片生成/文生图/文生图-艺术人像摄影-Zimage_Kook版_2087797024384176130.json, 图片生成/文生图/文生图-艺术人像摄影-Zimage_Kook版_2094592360981286913.json, 图片生成/文生图/文生图_2047653558849376258.json, 图片生成/文生图/文生图_Zimage_瑶光_2036105144634449921.json, 图片生成/文生图/文生图_Zimage_高清_2039868544275451905.json, 图片生成/文生图/无Ai感超强文生图_2076312965044858881.json, 图片生成/文生图/自用提示词生成人物_2084129308481773570.json, 图片生成/文生图/艺术人像摄影-Zimage_2079834947250122753.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079094992911552513.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2080552083677335553.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2081640212320575489.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2082387647414231042.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2104375192104562690.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2077757530842947586.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2078020927580884993.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻_2082352391269212161.json, 图片生成/文生图/艺术人像摄影超写实高清4K -Zimage_梦幻出片1_2094608432228814850.json, 图片生成/文生图/（自用）ZB瑶光-自写词_2037044705757765634.json, 图片生成/文生图/💫老许Gary：Z-image瑶光丨文生图_图像反推+SeedVR放大_2035003906622754817.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/文生图/Qwen2512 文生图工作流_2071432588077654017.json、图片生成/文生图/Rika-zit去水印放大真实人像流_2057641336878227458.json、图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078417819166920705.json、图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078469610759872514.json、图片生成/文生图/Zimage_瑶光_2115573777479323649.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 28 个 workflow 都包含：
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
- `GetImageSize+` —— 27/28 个有
- `ImageCASharpening+` —— 27/28 个有
- `RunningHub Deepcleaner` —— 27/28 个有
- `CR Text` —— 17/28 个有
- `PhotoShakeNode` —— 17/28 个有
- `PreviewImage` —— 17/28 个有
- `KOOK_SaveJPGImage` —— 11/28 个有
- `FastFilmGrain` —— 10/28 个有
- `LayerColor: BrightnessContrastV2` —— 10/28 个有
- `孤海注释` —— 5/28 个有
- `Fast Groups Bypasser (rgthree)` —— 4/28 个有
- `EmptyImage` —— 1/28 个有
- `Fast Bypasser (rgthree)` —— 1/28 个有
- `HAIGC_SaveImagesToZip` —— 1/28 个有
- `LayerUtility: PurgeVRAM` —— 1/28 个有
- `LoadImage` —— 1/28 个有
- `SaveImageToLocal` —— 1/28 个有
- `Text` —— 1/28 个有
- `easy imageSize` —— 1/28 个有
- `easy seed` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 28 | 100% |
| 高度 | 1384 | 1384 - 1920 | 28 | 84% |
| 采样步数 | 8 | 8 - 50 | 28 | 12% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 28 | 31% |
| 采样算法 | res_2s_ode | - | 28 | 57% |
| 调度器 | bong_tangent | - | 28 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，28 个样本，取值集中（一致性 100%）
- 高度 中位数 1384，观测区间 1384 - 1920，28 个样本，取值集中（一致性 84%）
- 采样步数 中位数 8，观测区间 8 - 50，28 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，28 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 res_2s_ode，28 个样本，一致性 57%
- 调度器 最常用 bong_tangent，28 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高发问题（27/28 个样本）：Steps较低可能导致细节不足
