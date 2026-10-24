---
name: text_to_image_lora_sampler_clip_249
type: Text To Image
frequency: 7
level: weak
coverage: 0.884571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/18个月宝宝睡衣产品套图｜居家场景模特产品展示6张图_2104489945556668418.json, 图片生成/图生图/1香2蕉2API图生图｜接口直连出图稳定，批量生产省心之选_2107359008972689410.json, 图片生成/图生图/4K图像高清放大｜seedvr 2图生图一键提升画质_2092156503158517761.json, 图片生成/图生图/4K图像高清放大｜seedvr_2图生图一键提升画质_2092605288389111810.json, 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json, 图片生成/图生图/图像4K超清放大工作流｜SeedVR2图生图画质增强处理_2097387593599115266.json, 图片生成/图生图/图生图高清放大｜seedvr 2 轻松把图片拉到4K超清画质_2097847522336268290.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_249

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/18个月宝宝睡衣产品套图｜居家场景模特产品展示6张图_2104489945556668418.json、图片生成/图生图/1香2蕉2API图生图｜接口直连出图稳定，批量生产省心之选_2107359008972689410.json、图片生成/图生图/4K图像高清放大｜seedvr 2图生图一键提升画质_2092156503158517761.json、图片生成/图生图/4K图像高清放大｜seedvr_2图生图一键提升画质_2092605288389111810.json、图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `solarL_SaveImagesToZip` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `SeedVR2LoadDiTModel` —— 5/7 个有
- `SeedVR2LoadVAEModel` —— 5/7 个有
- `SeedVR2VideoUpscaler` —— 5/7 个有
- `PrimitiveInt` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `Image Stitch` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/7 个有
- `RH_RhartImageG2ImageToImage_Batch` —— 1/7 个有
- `ResizeAndPadImage` —— 1/7 个有
- `RunningHub Deepcleaner` —— 1/7 个有
- `StringConstantMultiline` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1920 | 7 | 0% |
| 高度 | 80 | 80 - 1080 | 7 | 0% |
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 69% |
| 采样算法 | er_sde | - | 7 | 86% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1920，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1080，7 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
