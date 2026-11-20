---
name: text_to_image_lora_sampler_clip_42
type: Text To Image
frequency: 20
level: strong
coverage: 0.8992
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Zen Image Edit写实图像编辑｜图生图修图 其它图片处理一步到位_2104064412368850945.json, 图片生成/图生图/Zen Image Edit图像编辑｜图生图写实修图 其它图片处理全搞定_2104053107750686722.json, 图片生成/图生图/aigc-image-2.5图生图九图模式｜太平风图片批量处理_2106956375321567233.json, 图片生成/图生图/image 2.5图生图_2101659679536537601.json, 图片生成/图生图/image 2.5图生图工作流｜老图翻新重绘｜画质细节双重增强_2101867652611403778.json, 图片生成/图生图/image qwen image 2 1 character sheet with clothes_2108666622264303617.json, 图片生成/图生图/image qwen image 2 1 character sheet1 角色设定图生成_2108668112957698049.json, 图片生成/图生图/image2.5全能编辑器｜图生图修图改图一气呵成｜细节重绘不伤原图_2099110738114736130.json, 图片生成/图生图/qwen2.1漫剧角色三视图，图生图多角度设定一键出_2112290266672619522.json, 图片生成/图生图/qwen2.1漫剧角色三视图｜上传图像即出角色资产三视图｜漫剧创作必备_2112106203827490817.json, 图片生成/图生图/qwen_image_2.1单图编辑｜换装无偏移角色一致性_2105234290983399426.json, 图片生成/图生图/千问2.1节日表情包生成｜图生图趣味处理｜节庆斗图素材批量做_2104746467230568450.json, 图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json, 图片生成/文生图/Qwen Image 2.1 PE多宫格生图｜一张出九宫排版素材_2103032143940243457.json, 图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010.json, 图片生成/文生图/Qwen-Image-2.1-Turbo七步出图｜亚洲人像写真文生图极速版_2111055095529041921.json, 视频生成/图生视频/Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673.json, 视频生成/图生视频/Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506.json, 视频生成/图生视频/Remove模型Qwen_Image_2.1_PE姿势编辑工作流，人物类特效擦除图生图_2108739961490071554.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Zen Image Edit写实图像编辑｜图生图修图 其它图片处理一步到位_2104064412368850945.json、图片生成/图生图/Zen Image Edit图像编辑｜图生图写实修图 其它图片处理全搞定_2104053107750686722.json、图片生成/图生图/aigc-image-2.5图生图九图模式｜太平风图片批量处理_2106956375321567233.json、图片生成/图生图/image 2.5图生图_2101659679536537601.json、图片生成/图生图/image 2.5图生图工作流｜老图翻新重绘｜画质细节双重增强_2101867652611403778.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 20 个 workflow 都包含：
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
- `孤海注释` —— 17/20 个有
- `ResolutionSelector` —— 16/20 个有
- `LoadImage` —— 15/20 个有
- `TextEncodeQwenImage21` —— 14/20 个有
- `CR Prompt Text` —— 13/20 个有
- `ComfySwitchNode` —— 12/20 个有
- `QwenImage21Cache` —— 10/20 个有
- `QwenPERewriteT8` —— 9/20 个有
- `easy cleanGpuUsed` —— 8/20 个有
- `easy showAnything` —— 8/20 个有
- `PreviewImage` —— 5/20 个有
- `RH_RhartImageG25SunburstImageToImage` —— 4/20 个有
- `EmptyImage` —— 3/20 个有
- `Color Grading JK` —— 2/20 个有
- `Image Comparer (rgthree)` —— 2/20 个有
- `QwenImage21BlockCacheT8` —— 2/20 个有
- `QwenImage21SageAttentionT8` —— 2/20 个有
- `QwenImage21SpectrumT8` —— 2/20 个有
- `ZenImageEditCheckpointLoader` —— 2/20 个有
- `ZenImageEditEncodeAdvanced` —— 2/20 个有
- `AIO_Preprocessor` —— 1/20 个有
- `JjkShowText` —— 1/20 个有
- `Text` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（24/20 个样本）：Steps较低可能导致细节不足
