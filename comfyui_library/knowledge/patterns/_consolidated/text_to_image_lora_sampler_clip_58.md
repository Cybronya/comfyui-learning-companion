---
name: text_to_image_lora_sampler_clip_58
type: Text To Image
frequency: 17
level: strong
coverage: 0.898176
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Zen Image Edit写实图像编辑｜图生图修图 其它图片处理一步到位_2104064412368850945.json, 图片生成/图生图/Zen Image Edit图像编辑｜图生图写实修图 其它图片处理全搞定_2104053107750686722.json, 图片生成/图生图/aigc-image-2.5图生图九图模式｜太平风图片批量处理_2106956375321567233.json, 图片生成/图生图/image 2.5图生图_2101659679536537601.json, 图片生成/图生图/image 2.5图生图工作流｜老图翻新重绘｜画质细节双重增强_2101867652611403778.json, 图片生成/图生图/image qwen image 2 1 character sheet with clothes_2108666622264303617.json, 图片生成/图生图/image qwen image 2 1 character sheet1 角色设定图生成_2108668112957698049.json, 图片生成/图生图/image2.5全能编辑器｜图生图修图改图一气呵成｜细节重绘不伤原图_2099110738114736130.json, 图片生成/图生图/qwen2.1漫剧角色三视图，图生图多角度设定一键出_2112290266672619522.json, 图片生成/图生图/qwen2.1漫剧角色三视图｜上传图像即出角色资产三视图｜漫剧创作必备_2112106203827490817.json, 图片生成/图生图/全能图片2.5全能编辑 文生图图生图多功能处理_2098835900410195969.json, 图片生成/图生图/千问2.1图像编辑多图参考｜精准修改指哪改哪｜其它图片处理全能_2104810356660064258.json, 图片生成/图生图/千问图生图基础工作流｜简单高效图片处理｜新手也能一键出图_2104749587016806402.json, 图片生成/图生图/商品图一键抠图透明底 Qwen-Image-2.1自动识别主体_2104347960355151874.json, 图片生成/图生图/美少女写实图生图 Qwen Image2.1参考图高质量重绘_2104285634960646145.json, 图片生成/文生图/Qwen Image 2.1自助捏脸肖像生成｜人物资产一套带走_2111760751525449729.json, 图片生成/文生图/Qwen Image 2.1自助捏脸，人物肖像资产生成利器_2111965062415081474.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Zen Image Edit写实图像编辑｜图生图修图 其它图片处理一步到位_2104064412368850945.json、图片生成/图生图/Zen Image Edit图像编辑｜图生图写实修图 其它图片处理全搞定_2104053107750686722.json、图片生成/图生图/aigc-image-2.5图生图九图模式｜太平风图片批量处理_2106956375321567233.json、图片生成/图生图/image 2.5图生图_2101659679536537601.json、图片生成/图生图/image 2.5图生图工作流｜老图翻新重绘｜画质细节双重增强_2101867652611403778.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 16/17 个有
- `LoadImage` —— 15/17 个有
- `TextEncodeQwenImage21` —— 10/17 个有
- `ResolutionSelector` —— 9/17 个有
- `ComfySwitchNode` —— 6/17 个有
- `CR Prompt Text` —— 5/17 个有
- `QwenImage21Cache` —— 5/17 个有
- `RH_RhartImageG25SunburstImageToImage` —— 5/17 个有
- `Image Comparer (rgthree)` —— 4/17 个有
- `easy cleanGpuUsed` —— 4/17 个有
- `SaveImageAdvanced` —— 3/17 个有
- `FacialCustomization` —— 2/17 个有
- `QwenImage21_T2IPromptRewrite` —— 2/17 个有
- `ZenImageEditCheckpointLoader` —— 2/17 个有
- `ZenImageEditEncodeAdvanced` —— 2/17 个有
- `easy showAnything` —— 2/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `Text` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（18/17 个样本）：Steps较低可能导致细节不足
