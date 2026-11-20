---
name: text_to_image_lora_sampler_clip_346
type: Text To Image
frequency: 6
level: strong
coverage: 0.854167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/双图服装替换工作流｜全能图片2官方稳定版_2095583561020698625.json, 图片生成/图生图/商品图一键抠图透明底 Qwen-Image-2.1自动识别主体_2104347960355151874.json, 图片生成/图生图/商用版人物介绍产品四宫格 全能图片2图生图排版_2094236619254616065.json, 图片生成/图生图/商用版全能图片2｜人物介绍产品四宫格图生图生成_2094355396973649921.json, 图片生成/图生图/真2K白底图产品图生成 电商产品展示背景处理方案_2109740581042876418.json, 图片生成/文生图/Qwen 2.1洗图工作流，文生图反推提示词处理工具_2108319840565030913.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_346

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/双图服装替换工作流｜全能图片2官方稳定版_2095583561020698625.json、图片生成/图生图/商品图一键抠图透明底 Qwen-Image-2.1自动识别主体_2104347960355151874.json、图片生成/图生图/商用版人物介绍产品四宫格 全能图片2图生图排版_2094236619254616065.json、图片生成/图生图/商用版全能图片2｜人物介绍产品四宫格图生图生成_2094355396973649921.json、图片生成/图生图/真2K白底图产品图生成 电商产品展示背景处理方案_2109740581042876418.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/6 个有
- `QwenImage21Cache` —— 3/6 个有
- `RH_RhartImageNG31FlashOfficialImageToImage` —— 3/6 个有
- `TextEncodeQwenImage21` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `KOOK_SaveJPGImage` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `SeedGenerator` —— 1/6 个有
- `TextGenerate` —— 1/6 个有
- `VAEEncode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
