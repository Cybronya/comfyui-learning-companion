---
name: text_to_image_lora_sampler_clip_258
type: Text To Image
frequency: 7
level: strong
coverage: 0.856429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489.json, 图片生成/图生图/Qwen Image 2.1最强开源图像编辑多图模特换装图生图处理工具_2102088091476512769.json, 图片生成/图生图/Qwen Image 2.1纯净官流编辑｜40步无PE稳定出图_2103104435521155074.json, 图片生成/图生图/Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082.json, 图片生成/图生图/Qwen image2.1抠图去背景，图生图去水印一步到位_2110505250099646465.json, 图片生成/图生图/QwenImage2.1角色三视图生成｜bf16展开版图生图精准出图_2106197248026697729.json, 图片生成/图生图/Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_258

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489.json、图片生成/图生图/Qwen Image 2.1最强开源图像编辑多图模特换装图生图处理工具_2102088091476512769.json、图片生成/图生图/Qwen Image 2.1纯净官流编辑｜40步无PE稳定出图_2103104435521155074.json、图片生成/图生图/Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082.json、图片生成/图生图/Qwen image2.1抠图去背景，图生图去水印一步到位_2110505250099646465.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `GetImageSize` —— 3/7 个有
- `ResolutionSelector` —— 3/7 个有
- `Fast Bypasser (rgthree)` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `PixaromaSeed` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `GroupSwitcher` —— 1/7 个有
- `NuiKr.OpenPoseEditor` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有
- `PixaromaRunTimer` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
