---
name: text_to_image_lora_sampler_clip_239
type: Text To Image
frequency: 8
level: strong
coverage: 0.889125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Boogu Edit图像编辑优化版图生图工作流，局部重绘图生图处理工具_2103988876833542145.json, 图片生成/图生图/Boogu Edit图像编辑优化版图生图工作流，局部重绘图生图处理方案_2103990521432731649.json, 图片生成/图生图/Boogu+VR2.5光学眼镜场景｜OpticScene质感写真｜镜片反光都真实_2102607039821336578.json, 图片生成/图生图/boogu edit优化改图工作流｜上传图输提示词精准局部重绘_2103692889040707585.json, 图片生成/图生图/boogu edit优化版图像编辑，图生图局部重绘稳出图_2112332507399147522.json, 图片生成/图生图/boogu edit图像编辑优化版｜图生图局部重绘多用途｜日常修图好帮手_2112055812716843010.json, 图片生成/图生图/boogu edit图像编辑优化版｜局部重绘图生图细致改图_2103691242205966338.json, 图片生成/图生图/图像4K超清放大工作流｜SeedVR2图生图画质增强处理_2097387593599115266.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_239

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Boogu Edit图像编辑优化版图生图工作流，局部重绘图生图处理工具_2103988876833542145.json、图片生成/图生图/Boogu Edit图像编辑优化版图生图工作流，局部重绘图生图处理方案_2103990521432731649.json、图片生成/图生图/Boogu+VR2.5光学眼镜场景｜OpticScene质感写真｜镜片反光都真实_2102607039821336578.json、图片生成/图生图/boogu edit优化改图工作流｜上传图输提示词精准局部重绘_2103692889040707585.json、图片生成/图生图/boogu edit优化版图像编辑，图生图局部重绘稳出图_2112332507399147522.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `CR Prompt Text` —— 7/8 个有
- `DF_Get_image_size` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `KSamplerSelect` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 7/8 个有
- `SamplerCustom` —— 7/8 个有
- `TextEncodeBooguEdit` —— 7/8 个有
- `ImageConcanate` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `PrimitiveInt` —— 2/8 个有
- `SeedVR2LoadDiTModel` —— 2/8 个有
- `SeedVR2LoadVAEModel` —— 2/8 个有
- `SeedVR2VideoUpscaler` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
