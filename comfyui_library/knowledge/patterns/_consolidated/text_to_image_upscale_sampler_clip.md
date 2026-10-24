---
name: text_to_image_upscale_sampler_clip
type: Text To Image
frequency: 65
level: moderate
coverage: 0.961769
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/很棒的动漫模型ANIMA文生图-自动提示词_2056029257322778625.json, 图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2085274976416002049.json, 图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2085530271390199810.json, 图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2087799263668559874.json, 图片生成/文生图/文生图-艺术人像摄影-Zimage_Kook版_2079401388609724418.json, 图片生成/文生图/文生图-艺术人像摄影-Zimage_Kook版_2087797024384176130.json, 图片生成/文生图/文生图-艺术人像摄影-Zimage_Kook版_2094592360981286913.json, 图片生成/文生图/艺术人像摄影-Zimage_2079834947250122753.json, 图片生成/文生图/艺术人像摄影-Zimage_4K_2087105070633676802.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079094992911552513.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079100341446070274.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079369962627616770.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079377171252080641.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079730282101559297.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2079857385543393282.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2080096513530880001.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2080453494531772418.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2080471533251809281.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2080552083677335553.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2081545679805181954.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2081640212320575489.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2082387647414231042.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2084533180983504897.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2085162400310976514.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2086629449675661313.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2086650912705171457.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2086973204760973314.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2086991002576973826.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2087815411504082945.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2088521538239819777.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2089902158815780866.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2090680995036094465.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2093173213751762945.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2094957876140929025.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2096784007345299458.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2096841564227198978.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2098219020905435138.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2100741922146050049.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2102918572434616322.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2104375192104562690.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2104497308594434049.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2110614899280924673.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2079015020062662657.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2079031918133338114.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2079128435426942978.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2081910703044255745.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094970335052525570.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094975307181813762.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094979782537728001.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094982779284054018.json, 图片生成/文生图/艺术人像摄影-Zimage_Kook版_2094985648724856834.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2077757530842947586.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2078020927580884993.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2079187188364955650.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2079187557425963009.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2079532949934002177.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻_2082352391269212161.json, 图片生成/文生图/艺术人像摄影文生图｜Z-Image Kook版人像写真生成_2097469971596140545.json, 图片生成/文生图/艺术人像摄影超写实高清4K -Zimage_梦幻出片1_2094608432228814850.json, 图片生成/文生图/艺术人像摄影超写实高清4K_-Zimage_梦幻出片1_2084906889938296834.json, 图片生成/文生图/艺术人像摄影超写实高清4K_-Zimage_梦幻出片1_2084913862234697730.json, 图片生成/文生图/顶级艺术人像摄影-Zimage_如梦似幻-Kook版_2078129341376057346.json, 视频生成/图生视频/艺术人像摄影-Zimage_4K_2085548054337380353.json, 视频生成/图生视频/艺术人像摄影-Zimage_Kook版 (2)_2085250585183477762.json, 视频生成/图生视频/艺术人像摄影-Zimage__2084823694760833026.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip

> 由 `engine/knowledge_consolidation` 从 65 个 workflow 归纳得出（图片生成/文生图/很棒的动漫模型ANIMA文生图-自动提示词_2056029257322778625.json、图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2085274976416002049.json、图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2085530271390199810.json、图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2087799263668559874.json、图片生成/文生图/文生图-艺术人像摄影-Zimage_Kook版_2079401388609724418.json…）

- **类型**：Text To Image
- **样本数**：65
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 65 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `RunningHub Deepcleaner`
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
- `CR Text` —— 64/65 个有
- `LoraLoaderModelOnly` —— 64/65 个有
- `PhotoShakeNode` —— 64/65 个有
- `PreviewImage` —— 26/65 个有
- `孤海注释` —— 7/65 个有
- `JjkText` —— 2/65 个有
- `LoadImage` —— 2/65 个有
- `DuckHideNode` —— 1/65 个有
- `EmptyImage` —— 1/65 个有
- `INTConstant` —— 1/65 个有
- `Image Comparer (rgthree)` —— 1/65 个有
- `JoinStringMulti` —— 1/65 个有
- `PreviewAny` —— 1/65 个有
- `RH_LLMAPI_Pro_Node` —— 1/65 个有
- `solarL_SaveImagesToZip` —— 1/65 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 65 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 65 | 29% |
| 采样算法 | res_2s_ode | - | 65 | 97% |
| 调度器 | bong_tangent | - | 65 | 97% |
| 重绘幅度 | 1 | 1 - 1 | 65 | 100% |
| 宽度 | 1080 | 80 - 1920 | 65 | 85% |
| 高度 | 1384 | 80 - 1384 | 65 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 65/65 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，65 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，65 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 res_2s_ode，65 个样本，一致性 97%
- 调度器 最常用 bong_tangent，65 个样本，一致性 97%
- 重绘幅度 中位数 1，观测区间 1 - 1，65 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 80 - 1920，65 个样本，取值集中（一致性 85%）
- 高度 中位数 1384，观测区间 80 - 1384，65 个样本，取值集中（一致性 88%）
- 高发问题（65/65 个样本）：Steps较低可能导致细节不足
