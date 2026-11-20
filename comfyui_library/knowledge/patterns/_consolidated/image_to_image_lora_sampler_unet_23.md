---
name: image_to_image_lora_sampler_unet_23
type: Image To Image
frequency: 17
level: strong
coverage: 0.632059
common_nodes: [CFGNorm, CLIPLoader, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Edit 2509_转二次元3D手办风格（Anyto3Dfigure）_1999188815258546178.json, 图片生成/图生图/Qwen  最强 动漫 转 真人 写实真人 高清放大_2009936800520867842.json, 图片生成/图生图/Qwen Edit_图转3D渲染风格_1997967874390155266.json, 图片生成/图生图/Qwen image Edit 2511图像编辑工作流_2003529388635398145.json, 图片生成/图生图/Qwen-史上最强动漫转写实真人-Anything to Real Characters_1991953881183703042.json, 图片生成/图生图/【推荐】Edit 2509_转二次元3D手办风格（Anyto3Dfigure）_2008549502336114690.json, 图片生成/图生图/【推荐】一键转二次元手办正式版_2008557296925806594.json, 图片生成/图生图/一键转二次元手办_2033094077641662465.json, 图片生成/图生图/动漫人物转真人（上传图片即可）_2034460014009651202.json, 图片生成/图生图/动漫转真人 漫展  二次元 专用_2034186126080086018.json, 图片生成/图生图/动漫转真人 漫展  二次元 专用_2034207299950088193.json, 图片生成/图生图/动漫转真人-极致真实一键转真人_2031234025892880385.json, 图片生成/图生图/动漫转真人-极致真实（漫展和大博主都在用）_2029178379903180801.json, 图片生成/图生图/动漫转真人（漫展和大博主都在用）_2042917129619509249.json, 图片生成/图生图/幻模工坊_一键转二次元手办正式版_2000535766075834370.json, 图片生成/图生图/最强动漫转真人_2034095236443545602.json, 图片生成/图生图/绅士需要的动漫转真人-好！_2037561602001608705.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_23

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Edit 2509_转二次元3D手办风格（Anyto3Dfigure）_1999188815258546178.json、图片生成/图生图/Qwen  最强 动漫 转 真人 写实真人 高清放大_2009936800520867842.json、图片生成/图生图/Qwen Edit_图转3D渲染风格_1997967874390155266.json、图片生成/图生图/Qwen image Edit 2511图像编辑工作流_2003529388635398145.json、图片生成/图生图/Qwen-史上最强动漫转写实真人-Anything to Real Characters_1991953881183703042.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 16/17 个有
- `DF_Integer` —— 16/17 个有
- `ImageColorMatchAdobe+` —— 16/17 个有
- `ImageResize+` —— 16/17 个有
- `ImpactMinMax` —— 16/17 个有
- `SeedVR2` —— 16/17 个有
- `SeedVR2BlockSwap` —— 16/17 个有
- `SimpleMath+` —— 16/17 个有
- `TTP_Image_Assy` —— 16/17 个有
- `TTP_Image_Tile_Batch` —— 16/17 个有
- `Fast Groups Muter (rgthree)` —— 9/17 个有
- `PreviewImage` —— 9/17 个有
- `Image Comparer (rgthree)` —— 8/17 个有
- `Fast Groups Bypasser (rgthree)` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 17 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | res_2m | - | 17 | 76% |
| 调度器 | sgm_uniform | - | 17 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，17 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，17 个样本，一致性 76%
- 调度器 最常用 sgm_uniform，17 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
