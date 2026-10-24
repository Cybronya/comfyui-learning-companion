---
name: unknown_workflow_upscale_lora_sampler_29
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8355
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageResizeAdvanced, ImageResizeKJv2, ImageScaleToTotalPixels, Image_Channel_Apply, InspyrenetRembg, KSampler, LoadImage, LoraLoaderModelOnly, NunchakuQwenImageDiTLoader, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/4K图一键换背景_2046869023970824194.json, 图片生成/图生图/一键换背景-直出4K-Qwn-Edit-2509图生图_2095110025311244290.json, 图片生成/图生图/一键换背景-直出4K-Qwn-Edit-2509图生图_2095130329572007938.json, 图片生成/图生图/一键换背景-直出4K-Qwn-Edit-2509图生图_2097151899630923777.json, 图片生成/图生图/一键换背景-直出4K-Qwn-Edit-2509图生图_2097246376882167809.json, 图片生成/图生图/保姆级教程！图片模糊变清晰+一键抠图换背景，小白也能秒上手。_2060989178808193026.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/4K图一键换背景_2046869023970824194.json、图片生成/图生图/一键换背景-直出4K-Qwn-Edit-2509图生图_2095110025311244290.json、图片生成/图生图/一键换背景-直出4K-Qwn-Edit-2509图生图_2095130329572007938.json、图片生成/图生图/一键换背景-直出4K-Qwn-Edit-2509图生图_2097151899630923777.json、图片生成/图生图/一键换背景-直出4K-Qwn-Edit-2509图生图_2097246376882167809.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageResizeAdvanced`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `Image_Channel_Apply`
- `InspyrenetRembg`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImitationHueNode` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy clearCacheAll` —— 5/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `lay_image_mul` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 5 | 6 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 5，6 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
