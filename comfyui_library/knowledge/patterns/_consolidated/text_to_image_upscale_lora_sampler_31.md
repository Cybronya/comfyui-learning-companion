---
name: text_to_image_upscale_lora_sampler_31
type: Text To Image
frequency: 3
level: strong
coverage: 0.848333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GH_ImageVideoComparer, JjkText, KSampler, KSamplerAdvanced, LayerFilter: GaussianBlur, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageSizeByLongerSide, solarL_SaveImagesToZip, 图像缩放V2_孤海, 孤海注释, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: [LayerFilter: GaussianBlur, 图像缩放V2_孤海, 数学运算_孤海, easy imageSizeByLongerSide]
members: [图片生成/图生图/2102178943565656066.json, 图片生成/文生图/VOSR2+SeedVR2双模型高清修复｜放大细节增强工作流_2108436387690278913.json, 视频生成/图生视频/VOSR2+SEEDVR2极速高清修复视频处理生成工具_2104440069619802114.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2102178943565656066.json、图片生成/文生图/VOSR2+SeedVR2双模型高清修复｜放大细节增强工作流_2108436387690278913.json、视频生成/图生视频/VOSR2+SEEDVR2极速高清修复视频处理生成工具_2104440069619802114.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GH_ImageVideoComparer`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LayerFilter: GaussianBlur`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy imageSizeByLongerSide`
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `孤海注释`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `GoohaiUniversalSlider` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `DF_Integer` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: GaussianBlur、图像缩放V2_孤海、数学运算_孤海、easy imageSizeByLongerSide
