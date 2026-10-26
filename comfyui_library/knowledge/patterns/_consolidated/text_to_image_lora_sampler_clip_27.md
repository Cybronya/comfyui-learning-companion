---
name: text_to_image_lora_sampler_clip_27
type: Text To Image
frequency: 22
level: weak
coverage: 0.917045
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/PS API插件图生图编辑 edit2511版本对接_2098281737645289474.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑，图生图实测体验_2111251715113709570.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑｜单图多图改图修图迁移换装_2097944852406300674.json, 图片生成/图生图/Qwen-Image-Edit一键转宫崎骏风｜风格迁移动漫感拉满_2111089910420688898.json, 图片生成/图生图/Qwen-Image-Edit图片编辑｜一键宫崎骏风格转换图生图_2093111534082936834.json, 图片生成/图生图/Qwen_Image_Edit_2511图像编辑｜单图多图改图修图迁移换装_2098209289214193666.json, 图片生成/图生图/qwen2511去水印图像编辑｜最新写实图生图处理_2093462241126473730.json, 图片生成/图生图/一键换衣｜千问qwen2511最新图像编辑写实换装_2089821472830349313.json, 图片生成/图生图/一键转宫崎骏风格动漫｜Qwen-Image-Edit图生图_2095501283846352897.json, 图片生成/图生图/三视图真人动漫人物一致性 图生图处理工具_2100302408483164161.json, 图片生成/图生图/三视图真人动漫人物一致性 图生图处理生成工具_2100684736732680194.json, 图片生成/图生图/千问Qwen2511图像编辑模型 一键智能换装换衣_2098105005101375489.json, 图片生成/图生图/千问qwen2511一键换衣｜最新图像编辑换装图生图_2092380662576799745.json, 图片生成/图生图/千问qwen2511换装图像编辑｜服装替换图生图工作流_2097767445095337985.json, 图片生成/图生图/图像重打光工作流｜Qwen2511光影重塑图生图处理_2096332924449812482.json, 图片生成/图生图/换衣服背景_2108501932456374273.json, 图片生成/图生图/换装千问qwen2511最新图像编辑｜图生图换装一键完成_2097958405175599106.json, 图片生成/图生图/换装千问qwen2511最新图像编辑｜图生图换装一键完成_2098230078110003202.json, 图片生成/图生图/换装新体验｜千问qwen2511最新图像编辑图生图_2089820045437394945.json, 图片生成/图生图/提示词替换人物工作流｜描述一句即可换人｜图生图智能人物替换_2112115364392955906.json, 图片生成/图生图/真人动漫三视图｜人物一致性图生图写实出图_2092900266537480193.json, 图片生成/图生图/真人动漫人物一致性｜三视图图生图写实生成_2092710922988118017.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/PS API插件图生图编辑 edit2511版本对接_2098281737645289474.json、图片生成/图生图/Qwen Image Edit 2511图像编辑，图生图实测体验_2111251715113709570.json、图片生成/图生图/Qwen Image Edit 2511图像编辑｜单图多图改图修图迁移换装_2097944852406300674.json、图片生成/图生图/Qwen-Image-Edit一键转宫崎骏风｜风格迁移动漫感拉满_2111089910420688898.json、图片生成/图生图/Qwen-Image-Edit图片编辑｜一键宫崎骏风格转换图生图_2093111534082936834.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 22 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 21/22 个有
- `SaveImage` —— 21/22 个有
- `solarL_SaveImagesToZip` —— 21/22 个有
- `孤海注释` —— 21/22 个有
- `FluxKontextMultiReferenceLatentMethod` —— 19/22 个有
- `ImageScaleToTotalPixels` —— 19/22 个有
- `TextEncodeQwenImageEditPlus` —— 19/22 个有
- `VAEEncode` —— 18/22 个有
- `ImageConcanate` —— 16/22 个有
- `CR Text` —— 13/22 个有
- `Image Comparer (rgthree)` —— 6/22 个有
- `EmptySD3LatentImage` —— 4/22 个有
- `SDXL Empty Latent Image` —— 4/22 个有
- `ImageConcatMulti` —— 3/22 个有
- `TextEncodeQwenImageEdit` —— 3/22 个有
- `CompressImages` —— 1/22 个有
- `QwenMultiangleLightningNode` —— 1/22 个有
- `SeedVR2LoadDiTModel` —— 1/22 个有
- `SeedVR2LoadVAEModel` —— 1/22 个有
- `SeedVR2VideoUpscaler` —— 1/22 个有
- `easy imageScaleDownToSize` —— 1/22 个有
- `easy showAnything` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 22 | 71% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 22 | 83% |
| 采样算法 | er_sde | - | 22 | 95% |
| 调度器 | beta | - | 22 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 1024 | 22 | 0% |
| 高度 | 80 | 80 - 1024 | 22 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 44/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，22 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，22 个样本，取值集中（一致性 83%）
- 采样算法 最常用 er_sde，22 个样本，一致性 95%
- 调度器 最常用 beta，22 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，22 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，22 个样本，取值分散，一致性仅 0%
- 高发问题（44/22 个样本）：Steps较低可能导致细节不足
