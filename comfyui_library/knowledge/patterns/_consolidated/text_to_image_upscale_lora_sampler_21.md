---
name: text_to_image_upscale_lora_sampler_21
type: Text To Image
frequency: 9
level: strong
coverage: 0.725556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图一键虚拟试穿服装展示换装处理生成工具_2101393041541132289.json, 图片生成/图生图/图生图一键虚拟试穿生成 服装展示换装套系_2095835014322810881.json, 图片生成/图生图/图生图一键虚拟试穿生成 服装展示换装套系_2100852214012145666.json, 图片生成/图生图/服装展示换装套系｜图生图一键虚拟试穿生成_2090526196059697154.json, 图片生成/图生图/短剧人物三视图｜参考图生成正侧背角色设定图_2089309758296780801.json, 图片生成/文生图/Krea2美学视觉文生图加SeedVR2高清出图工作流，文生图高质量文本到图像_2107579414744752130.json, 数字人/数字人/Krea2熟颜世绘Lora模型 写实美少女文生图风格化生成_2099181814492524545.json, 数字人/数字人/krea2熟颜世绘｜尺素数字人文生图美少女生成_2091288163825311745.json, 数字人/数字人/尺素出品krea2熟颜世绘｜美少女文生图有味道，质感细腻很出片_2099462000886771713.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/图生图一键虚拟试穿服装展示换装处理生成工具_2101393041541132289.json、图片生成/图生图/图生图一键虚拟试穿生成 服装展示换装套系_2095835014322810881.json、图片生成/图生图/图生图一键虚拟试穿生成 服装展示换装套系_2100852214012145666.json、图片生成/图生图/服装展示换装套系｜图生图一键虚拟试穿生成_2090526196059697154.json、图片生成/图生图/短剧人物三视图｜参考图生成正侧背角色设定图_2089309758296780801.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 8/9 个有
- `GetNode` —— 5/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `LoadImage` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `INTConstant` —— 4/9 个有
- `LayerUtility: ImageReel` —— 4/9 个有
- `LayerUtility: ImageReelComposit` —— 4/9 个有
- `Text` —— 4/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `RH_RhartImageG2ImageToImage` —— 1/9 个有
- `easy imageSizeBySide` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（18/9 个样本）：Steps较低可能导致细节不足
