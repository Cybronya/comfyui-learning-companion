---
name: image_to_image_sampler_clip_unet_3
type: Image To Image
frequency: 32
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWen-edit 海报模特首饰展示_1959182670829924353.json, 图片生成/图生图/Qwen Edit图像编辑V1_1957765074305871874.json, 图片生成/图生图/Qwen Edit非常规Kontext方法图像编辑8步加速V1_1960012793477017602.json, 图片生成/图生图/Qwen edit 图像遮罩修改_1959187243724386305.json, 图片生成/图生图/Qwen edit 图像遮罩修改_1959238839569166338.json, 图片生成/图生图/Qwen- Edit 服装展示｜模特试穿_1957996644358926337.json, 图片生成/图生图/Qwen-Edit PVC玩偶手办_1958001637711392770.json, 图片生成/图生图/Qwen-Edit 动漫转真人_1979430035075534849.json, 图片生成/图生图/Qwen-Edit 参考角色一致性 最强好用版_1957999870541967361.json, 图片生成/图生图/Qwen-Edit 吉卜力动漫风格转换_1958041359359913986.json, 图片生成/图生图/Qwen-Edit 图片去除水印｜水印消除_1959188505371029505.json, 图片生成/图生图/Qwen-Edit 多图融合｜电商海报 CFGNORM_1970751059075493890.json, 图片生成/图生图/Qwen-Edit 多图融合｜电商海报_1970751035130191874.json, 图片生成/图生图/Qwen-Edit 超自然发型设计_1959207405462695938.json, 图片生成/图生图/Qwen-Image-Edit 简易风格转换｜吉卜力_1959206801424199682.json, 图片生成/图生图/Qwen-edit IP形象三视图_1958015187636858881.json, 图片生成/图生图/Qwen-edit 一键线稿上色_1959205764835520513.json, 图片生成/图生图/Qwen-edit 人像写真｜光影打光_1959179294004162562.json, 图片生成/图生图/Qwen-edit 人物换装_1959183646030770177.json, 图片生成/图生图/Qwen-edit 人物换装_1959240143938990082.json, 图片生成/图生图/Qwen-edit 人物换装｜图像换背景_1958453861004558337.json, 图片生成/图生图/Qwen-edit 动漫线稿上色_1958000793205059586.json, 图片生成/图生图/Qwen-edit 动漫线稿上色_1958002599666528258.json, 图片生成/图生图/Qwen-edit 图像编辑_1959178152402694145.json, 图片生成/图生图/Qwen-edit 图像编辑｜简易工作流_1958043600904925186.json, 图片生成/图生图/Qwen-edit 明星手持产品｜代言海报_1959180375752912898.json, 图片生成/图生图/Qwen-edit 电商产品换背景_1957998637181808642.json, 图片生成/图生图/Qwen-edit 电商模特时装_1959207774158794754.json, 图片生成/图生图/Qwen-edit 简易一键3D皮克斯_1959181350832123905.json, 图片生成/图生图/Qwen-edit 简易一键3D皮克斯_1959237576928473090.json, 图片生成/图生图/Qwen-edit 老照片上色_1958037838153527298.json, 图片生成/图生图/Qwen-edit 首饰试戴｜优雅高级_1957997754230386689.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（图片生成/图生图/QWen-edit 海报模特首饰展示_1959182670829924353.json、图片生成/图生图/Qwen Edit图像编辑V1_1957765074305871874.json、图片生成/图生图/Qwen Edit非常规Kontext方法图像编辑8步加速V1_1960012793477017602.json、图片生成/图生图/Qwen edit 图像遮罩修改_1959187243724386305.json、图片生成/图生图/Qwen edit 图像遮罩修改_1959238839569166338.json…）

- **类型**：Image To Image
- **样本数**：32
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 32 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 31/32 个有
- `easy imageConcat` —— 31/32 个有
- `FluxKontextImageScale` —— 30/32 个有
- `ModelSamplingAuraFlow` —— 2/32 个有
- `CFGNorm` —— 1/32 个有
- `FluxGuidance` —— 1/32 个有
- `ImageConcanate` —— 1/32 个有
- `LoraLoader` —— 1/32 个有
- `LoraLoaderModelOnly` —— 1/32 个有
- `ReferenceLatent` —— 1/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 32 | 89% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 32 | 89% |
| 采样算法 | euler | - | 32 | 100% |
| 调度器 | normal | - | 32 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 32 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，32 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，32 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler，32 个样本，一致性 100%
- 调度器 最常用 normal，32 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，32 个样本，取值集中（一致性 100%）
