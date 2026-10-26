---
name: text_to_image_sampler_clip_unet_77
type: Text To Image
frequency: 9
level: strong
coverage: 0.871222
common_nodes: [CLIPTextEncode, CR Prompt Text, CR Text Replace, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081.json, 图片生成/文生图/美少女量贩式生成_1994800940983181313.json, 图片生成/文生图/量贩版 ZIT-D-OPSD美少女文生图（自动化批量出图）_2066140658238316545.json, 图片生成/文生图/（小情绪量贩版）Z-Image Art自动扩写文生图V1_2017609951325196290.json, 图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json, 图片生成/文生图/（量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1994411563819864066.json, 图片生成/文生图/（量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2056786094817112066.json, 图片生成/文生图/（量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2064906233831841794.json, 图片生成/文生图/（量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2065067678041198593.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081.json、图片生成/文生图/美少女量贩式生成_1994800940983181313.json、图片生成/文生图/量贩版 ZIT-D-OPSD美少女文生图（自动化批量出图）_2066140658238316545.json、图片生成/文生图/（小情绪量贩版）Z-Image Art自动扩写文生图V1_2017609951325196290.json、图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Replace`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `Text Concatenate` —— 8/9 个有
- `LayerUtility: PurgeVRAM` —— 7/9 个有
- `Seed (rgthree)` —— 7/9 个有
- `ClipLoaderGGUF` —— 5/9 个有
- `PreviewAny` —— 5/9 个有
- `QwenImageEngineer` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `CLIPLoader` —— 4/9 个有
- `ImageScaleBy` —— 2/9 个有
- `SeedVR2LoadDiTModel` —— 2/9 个有
- `SeedVR2LoadVAEModel` —— 2/9 个有
- `SeedVR2VideoUpscaler` —— 2/9 个有
- `GetImageSize+` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageCASharpening+` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `RunningHub Deepcleaner` —— 1/9 个有
- `TTP_Image_Assy` —— 1/9 个有
- `TTP_Image_Tile_Batch` —— 1/9 个有
- `TTP_Tile_image_size` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 9 | 100% |
| 高度 | 1920 | 1920 - 1920 | 9 | 100% |
| 采样步数 | 10 | 10 - 10 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
