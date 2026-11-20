---
name: image_to_image_sampler_clip_unet_7
type: Image To Image
frequency: 21
level: strong
coverage: 0.915714
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/05Kontext动漫风格转绘（新海诚风格）_1947092181813485569.json, 图片生成/图生图/20250711-教程版3种方式去马赛克对比工作流_1943272337959493633.json, 图片生成/图生图/360度全景图-3D旋转预览_Kontext-DEV-LORA_1940463300813680641.json, 图片生成/图生图/3D Chibi可爱风格转绘_1941419070581587970.json, 图片生成/图生图/3D+Chibi可爱风格转绘_2015676038226907138.json, 图片生成/图生图/3视图_Kontext-DEV-LORA_1940674502839742465.json, 图片生成/图生图/Emoji风格_Kontext-DEV-LORA_1951666575273308162.json, 图片生成/图生图/Flux Kontext Dev主体变色及放大修复（角色_物品）_1938524454505111554.json, 图片生成/图生图/Flux Kontext Dev主体换背景及放大修复（角色_物品_电商）_1938527176453218306.json, 图片生成/图生图/Flux Kontext Dev主体文字消除（可去水印）_1938524674248605698.json, 图片生成/图生图/Flux Kontext Dev主体新增及放大修复（角色_物品）_1938514358500810754.json, 图片生成/图生图/Flux Kontext Dev主体旋转多视图及放大修复（物品，角色）_1938545325747720193.json, 图片生成/图生图/Flux Kontext Dev主体移除及放大修复（角色_物品）_1938525727098601473.json, 图片生成/图生图/Flux Kontext Dev二阶段三图融合及修复放大_1938597675900325889.json, 图片生成/图生图/Flux Kontext Dev二阶段破损老照片修复上色及放大_1938580086860009473.json, 图片生成/图生图/Flux Kontext Dev图像扩展及放大修复_1938545690908020737.json, 图片生成/图生图/Kontext Presets 官方预设词｜图生图_1945761686198558722.json, 图片生成/图生图/Kontext官方预设13种提示词并自动优化_1944538008895016962.json, 图片生成/图生图/kontext去水印_1948707962933129217.json, 图片生成/图生图/黑森林官方Kontext Presets预设模板_Janus7B精准图像编辑_1944320832053104642.json, 图片生成/图生图/黑森林官方Kontext Presets预设模板_LLM-API精准图像编辑_1943859932489744385.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/05Kontext动漫风格转绘（新海诚风格）_1947092181813485569.json、图片生成/图生图/20250711-教程版3种方式去马赛克对比工作流_1943272337959493633.json、图片生成/图生图/360度全景图-3D旋转预览_Kontext-DEV-LORA_1940463300813680641.json、图片生成/图生图/3D Chibi可爱风格转绘_1941419070581587970.json、图片生成/图生图/3D+Chibi可爱风格转绘_2015676038226907138.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 20/21 个有
- `ImageConcatMulti` —— 19/21 个有
- `LoraLoaderModelOnly` —— 12/21 个有
- `PreviewImage` —— 12/21 个有
- `PMRF` —— 10/21 个有
- `RH_Translator` —— 10/21 个有
- `EmptySD3LatentImage` —— 7/21 个有
- `GetImageSizeAndCount` —— 7/21 个有
- `ImageScaleDownToSize` —— 5/21 个有
- `LoadKontextPresets` —— 5/21 个有
- `easy showAnything` —— 5/21 个有
- `RH_LLMAPI_NODE` —— 4/21 个有
- `Text Concatenate` —— 3/21 个有
- `Image Padding` —— 2/21 个有
- `TeaCache` —— 2/21 个有
- `CR SDXL Aspect Ratio` —— 1/21 个有
- `CR Simple Image Compare` —— 1/21 个有
- `JanusImageUnderstanding` —— 1/21 个有
- `JanusModelLoader` —— 1/21 个有
- `PanoramaViewerNode` —— 1/21 个有
- `easy imageRemBg` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 21 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 21 | 100% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
