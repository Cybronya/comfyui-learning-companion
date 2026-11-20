---
name: text_to_image_upscale_lora_sampler
type: Text To Image
frequency: 56
level: moderate
coverage: 0.930839
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, RunningHub Deepcleaner, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万能图像洗图-Zimage_kook瑶光版_2034186472865140737.json, 图片生成/图生图/不花钱的电商海报高清生成_2066449995951333377.json, 图片生成/文生图/Kook_Zimage_如梦似幻_2049613798604066818.json, 图片生成/文生图/Kook_Zimage_瑶光_2033767418278977537.json, 图片生成/文生图/Kook_Zimage_瑶光_2115627771476135937.json, 图片生成/文生图/Zimage一键生成海报_2034875531174354946.json, 图片生成/文生图/不花钱的电商海报高清生成_2068887981989130242.json, 图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2085274976416002049.json, 图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2085530271390199810.json, 图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2087799263668559874.json, 图片生成/文生图/电商海报高清生成优化版-图片+文字生成-Zimage_2033966725204545538.json, 图片生成/文生图/艺术人像摄影-Zimage_4K_2087105070633676802.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079100341446070274.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079369962627616770.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079377171252080641.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079730282101559297.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079857385543393282.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2080096513530880001.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2080453494531772418.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2080471533251809281.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2081545679805181954.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2084533180983504897.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2085162400310976514.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2086629449675661313.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2086650912705171457.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2086973204760973314.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2086991002576973826.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2087815411504082945.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2088521538239819777.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2089902158815780866.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2090680995036094465.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2093173213751762945.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2094957876140929025.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2096784007345299458.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2096841564227198978.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2098219020905435138.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2100741922146050049.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2102918572434616322.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2104497308594434049.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2110614899280924673.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2079015020062662657.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2079031918133338114.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2079128435426942978.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2081910703044255745.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094970335052525570.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094975307181813762.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094979782537728001.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094982779284054018.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094985648724856834.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2079187188364955650.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2079187557425963009.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2079532949934002177.json, 图片生成/文生图/艺术人像摄影-Zimage_文生图_2116482143370178562.json, 图片生成/文生图/艺术人像摄影-Zimage_文生图_2116490874791223297.json, 图片生成/文生图/艺术人像摄影-Zimage_文生图_2116728648999981057.json, 平台全量/超级海报生成器-Zimage_kook瑶光版_2033787476887740418.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler

> 由 `engine/knowledge_consolidation` 从 56 个 workflow 归纳得出（图片生成/图生图/万能图像洗图-Zimage_kook瑶光版_2034186472865140737.json、图片生成/图生图/不花钱的电商海报高清生成_2066449995951333377.json、图片生成/文生图/Kook_Zimage_如梦似幻_2049613798604066818.json、图片生成/文生图/Kook_Zimage_瑶光_2033767418278977537.json、图片生成/文生图/Kook_Zimage_瑶光_2115627771476135937.json…）

- **类型**：Text To Image
- **样本数**：56
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 56 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
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
- `SaveImage` —— 53/56 个有
- `PhotoShakeNode` —— 50/56 个有
- `CR Text` —— 48/56 个有
- `PreviewImage` —— 15/56 个有
- `KOOK_SaveJPGImage` —— 8/56 个有
- `GetNode` —— 6/56 个有
- `Image Comparer (rgthree)` —— 6/56 个有
- `LoadImage` —— 6/56 个有
- `SetNode` —— 6/56 个有
- `Text` —— 5/56 个有
- `RH_LLMAPI_NODE` —— 3/56 个有
- `ShowText|pysssss` —— 3/56 个有
- `ImageConcanate` —— 1/56 个有
- `RH_LLMAPI_Pro_Node` —— 1/56 个有
- `easy showAnything` —— 1/56 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 56 | 3% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 56 | 26% |
| 采样算法 | res_2s_ode | - | 56 | 86% |
| 调度器 | bong_tangent | - | 56 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 56 | 100% |
| 宽度 | 1080 | 1080 - 1480 | 56 | 95% |
| 高度 | 1384 | 1384 - 1920 | 56 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 56/56 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，56 个样本，取值分散，一致性仅 3%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，56 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 res_2s_ode，56 个样本，一致性 86%
- 调度器 最常用 bong_tangent，56 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，56 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1480，56 个样本，取值集中（一致性 95%）
- 高度 中位数 1384，观测区间 1384 - 1920，56 个样本，取值集中（一致性 89%）
- 高发问题（56/56 个样本）：Steps较低可能导致细节不足
