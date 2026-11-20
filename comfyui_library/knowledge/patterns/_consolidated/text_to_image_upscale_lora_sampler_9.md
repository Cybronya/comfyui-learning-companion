---
name: text_to_image_upscale_lora_sampler_9
type: Text To Image
frequency: 15
level: weak
coverage: 0.8272
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/角色资产4格图免提示词 Qwen-Image2.1放大处理工具_2113405844221157377.json, 图片生成/图生图/4K图像高清放大｜seedvr 2图生图一键提升画质_2092156503158517761.json, 图片生成/图生图/4K图像高清放大｜seedvr_2图生图一键提升画质_2092605288389111810.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json, 图片生成/图生图/MiniMax H3人像参考图专用生成器 人像图生图处理工具_2113024918748225538.json, 图片生成/图生图/Minimax H3人像参考图专用生成器｜写真质感一图即出_2112823108011909121.json, 图片生成/图生图/Moss Prompt文生图图生图 双模式图像生成处理工具_2114135139465908225.json, 图片生成/图生图/Qwen Image2.1角色资产4格详图 SEEDVR2高清放大处理工具_2113048870426075138.json, 图片生成/图生图/角色资产4格详图制作Qwen Image 2.1工作流，图生图其它图片处理工具_2107887078867558401.json, 图片生成/文生图/MOSS SFT角色设计文生图 NB级图像生成处理工具_2114090024579981314.json, 图片生成/文生图/MOSS-Prompt RH版角色定妆照生成，文生图人设立绘质感精致_2114475089633828865.json, 图片生成/文生图/MOSS-Prompt_RH版角色定妆照生成，文生图人设立绘质感精致_2116827554547060738.json, 图片生成/文生图/MOSS一键人物三视图生成工作流，输入单图快速出全身多角度设定_2114445738783633409.json, 图片生成/文生图/Moss一键人物三视图_2113674193341607938.json, 图片生成/文生图/Moss一键人物三视图工作流｜文生图直出多角度人设图_2114279345836613634.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/角色资产4格图免提示词 Qwen-Image2.1放大处理工具_2113405844221157377.json、图片生成/图生图/4K图像高清放大｜seedvr 2图生图一键提升画质_2092156503158517761.json、图片生成/图生图/4K图像高清放大｜seedvr_2图生图一键提升画质_2092605288389111810.json、图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json、图片生成/图生图/MiniMax H3人像参考图专用生成器 人像图生图处理工具_2113024918748225538.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 14/15 个有
- `ImageScaleToTotalPixels` —— 13/15 个有
- `solarL_SaveImagesToZip` —— 13/15 个有
- `PreviewImage` —— 12/15 个有
- `PrimitiveStringMultiline` —— 12/15 个有
- `ResolutionSelector` —— 12/15 个有
- `孤海注释` —— 12/15 个有
- `Image Comparer (rgthree)` —— 11/15 个有
- `LoadImage` —— 11/15 个有
- `ComfySwitchNode` —— 8/15 个有
- `TextEncodeQwenImage21` —— 8/15 个有
- `EmptyFlux2LatentImage` —— 7/15 个有
- `INTConstant` —— 7/15 个有
- `SkipLayerGuidanceDiTSimple` —— 7/15 个有
- `Fast Groups Bypasser (rgthree)` —— 6/15 个有
- `QwenImage21Cache` —— 5/15 个有
- `PreviewAny` —— 4/15 个有
- `CR Prompt Text` —— 3/15 个有
- `GetNode` —— 3/15 个有
- `PrimitiveBoolean` —— 3/15 个有
- `RH_LLMAPI_Pro_Node` —— 3/15 个有
- `SetNode` —— 3/15 个有
- `easy saveText` —— 3/15 个有
- `FastGroupsBypassSwitch` —— 1/15 个有
- `RunningHub Deepcleaner` —— 1/15 个有
- `TextEncodeQwenImageEditPlus` —— 1/15 个有
- `TextGenerate` —— 1/15 个有
- `忽略多组孤海` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1920 | 15 | 0% |
| 高度 | 80 | 80 - 1080 | 15 | 0% |
| 采样步数 | 4 | 4 - 25 | 15 | 7% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 71% |
| 采样算法 | er_sde | - | 15 | 87% |
| 调度器 | beta | - | 15 | 87% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1920，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1080，15 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 25，15 个样本，取值分散，一致性仅 7%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 87%
- 调度器 最常用 beta，15 个样本，一致性 87%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（14/15 个样本）：Steps较低可能导致细节不足
