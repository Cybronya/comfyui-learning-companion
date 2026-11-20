---
name: image_to_image_sampler_clip_unet_3
type: Image To Image
frequency: 40
level: strong
coverage: 0.998325
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWen-edit 海报模特首饰展示_1959182670829924353.json, 图片生成/图生图/Qwen Edit图像编辑V1_1957765074305871874.json, 图片生成/图生图/Qwen Edit非常规Kontext方法图像编辑8步加速V1_1960012793477017602.json, 图片生成/图生图/Qwen edit 图像遮罩修改_1959187243724386305.json, 图片生成/图生图/Qwen edit 图像遮罩修改_1959238839569166338.json, 图片生成/图生图/Qwen- Edit 服装展示｜模特试穿_1957996644358926337.json, 图片生成/图生图/Qwen-Edit PVC玩偶手办_1958001637711392770.json, 图片生成/图生图/Qwen-Edit 动漫转真人_1979430035075534849.json, 图片生成/图生图/Qwen-Edit 参考角色一致性 最强好用版_1957999870541967361.json, 图片生成/图生图/Qwen-Edit 吉卜力动漫风格转换_1958041359359913986.json, 图片生成/图生图/Qwen-Edit 图片去除水印｜水印消除_1959188505371029505.json, 图片生成/图生图/Qwen-Edit 多图融合｜电商海报 CFGNORM_1970751059075493890.json, 图片生成/图生图/Qwen-Edit 多图融合｜电商海报_1970751035130191874.json, 图片生成/图生图/Qwen-Edit 超自然发型设计_1959207405462695938.json, 图片生成/图生图/Qwen-Image-Edit 简易风格转换｜吉卜力_1959206801424199682.json, 图片生成/图生图/Qwen-edit IP形象三视图_1958015187636858881.json, 图片生成/图生图/Qwen-edit 一键线稿上色_1959205764835520513.json, 图片生成/图生图/Qwen-edit 人像写真｜光影打光_1959179294004162562.json, 图片生成/图生图/Qwen-edit 人物换装_1959183646030770177.json, 图片生成/图生图/Qwen-edit 人物换装_1959240143938990082.json, 图片生成/图生图/Qwen-edit 人物换装｜图像换背景_1958453861004558337.json, 图片生成/图生图/Qwen-edit 动漫线稿上色_1958000793205059586.json, 图片生成/图生图/Qwen-edit 动漫线稿上色_1958002599666528258.json, 图片生成/图生图/Qwen-edit 图像编辑_1959178152402694145.json, 图片生成/图生图/Qwen-edit 图像编辑｜简易工作流_1958043600904925186.json, 图片生成/图生图/Qwen-edit 明星手持产品｜代言海报_1959180375752912898.json, 图片生成/图生图/Qwen-edit 电商产品换背景_1957998637181808642.json, 图片生成/图生图/Qwen-edit 电商模特时装_1959207774158794754.json, 图片生成/图生图/Qwen-edit 简易一键3D皮克斯_1959181350832123905.json, 图片生成/图生图/Qwen-edit 简易一键3D皮克斯_1959237576928473090.json, 图片生成/图生图/Qwen-edit 老照片上色_1958037838153527298.json, 图片生成/图生图/Qwen-edit 首饰试戴｜优雅高级_1957997754230386689.json, 图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json, 图片生成/图生图/一键生成丰富表情包_1972210558072254466.json, 图片生成/图生图/一键生成表情包_1972131190742380546.json, 图片生成/图生图/动漫转真人 _ Workflow for Qwen-Edit_1958005330036797442.json, 图片生成/图生图/卡通动漫一致性 动作修改｜人物保持_1959186353315590146.json, 图片生成/图生图/最新 Qwen-edit 一键服装模特试穿_1958042179543478274.json, 图片生成/图生图/真人转动漫风格 _ Workflow for Qwen_1958700602907848706.json, 图片生成/图生图/鲜明亮丽的插画风格_1970083139890651138.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 40 个 workflow 归纳得出（图片生成/图生图/QWen-edit 海报模特首饰展示_1959182670829924353.json、图片生成/图生图/Qwen Edit图像编辑V1_1957765074305871874.json、图片生成/图生图/Qwen Edit非常规Kontext方法图像编辑8步加速V1_1960012793477017602.json、图片生成/图生图/Qwen edit 图像遮罩修改_1959187243724386305.json、图片生成/图生图/Qwen edit 图像遮罩修改_1959238839569166338.json…）

- **类型**：Image To Image
- **样本数**：40
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 40 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 39/40 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 39/40 个有
- `FluxKontextImageScale` —— 38/40 个有
- `easy imageConcat` —— 38/40 个有
- `LoraLoaderModelOnly` —— 2/40 个有
- `ModelSamplingAuraFlow` —— 2/40 个有
- `CFGNorm` —— 1/40 个有
- `FluxGuidance` —— 1/40 个有
- `ImageConcanate` —— 1/40 个有
- `LoraLoader` —— 1/40 个有
- `PreviewImage` —— 1/40 个有
- `ReferenceLatent` —— 1/40 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 40 | 90% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 40 | 90% |
| 采样算法 | euler | - | 40 | 100% |
| 调度器 | normal | - | 40 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 40 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/40 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，40 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，40 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler，40 个样本，一致性 100%
- 调度器 最常用 normal，40 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，40 个样本，取值集中（一致性 100%）
