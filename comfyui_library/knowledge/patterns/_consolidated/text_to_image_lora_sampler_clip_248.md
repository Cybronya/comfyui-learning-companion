---
name: text_to_image_lora_sampler_clip_248
type: Text To Image
frequency: 8
level: strong
coverage: 0.85325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102508530350772225.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102517800026861570.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102546574596460545.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102548100928856066.json, 图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json, 图片生成/图生图/Qwen_Image_2.1图像编辑｜图生图实操经验版｜稳定可靠_2102313763641847810.json, 图片生成/图生图/老孙AI出品Qwen Image 2.1图像编辑｜图生图实操经验版｜稳定可靠_2102264426807255042.json, 图片生成/图生图/角色资产四视图一键生成｜SeedVR2高清放大加持｜设定图图生图标配_2102265852648312834.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_248

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102508530350772225.json、图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102517800026861570.json、图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102546574596460545.json、图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102548100928856066.json、图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `DF_Text_Box` —— 5/8 个有
- `GH_ImageVideoComparer` —— 5/8 个有
- `图像缩放V2_孤海` —— 5/8 个有
- `GoohaiUniversalSlider` —— 4/8 个有
- `easy ifElse` —— 4/8 个有
- `布尔孤海` —— 4/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `Text` —— 2/8 个有
- `CM_FloatToInt` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `GoohaiRatioAndResolution` —— 1/8 个有
- `ImpactMinMax` —— 1/8 个有
- `KepStringLiteral` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `SaveImageAdvanced` —— 1/8 个有
- `SeedVR2LoadDiTModel` —— 1/8 个有
- `SeedVR2LoadVAEModel` —— 1/8 个有
- `SeedVR2VideoUpscaler` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
