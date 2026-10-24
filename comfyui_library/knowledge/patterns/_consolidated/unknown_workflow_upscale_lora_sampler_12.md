---
name: unknown_workflow_upscale_lora_sampler_12
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.998714
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【直出】换装4K_2073290298790526976.json, 图片生成/图生图/一键换装FireRed+SD高清_2059969177762484226.json, 图片生成/图生图/一键换装直出4K-Qwen-edit_2008486174893019137.json, 图片生成/图生图/千问4K换装-阿浩_2042485507476688898.json, 图片生成/图生图/完美换装直出4K_2037356484362772481.json, 图片生成/图生图/小白_2013300621142663169.json, 图片生成/图生图/换装_2052270067211096065.json, 图片生成/图生图/换装直出4K-Qwen-edit_2039712959525560322.json, 图片生成/图生图/换装直出4K-Qwen-edit_2047191622722523138.json, 图片生成/图生图/换装直出4K-Qwen-edit_2049031061207781377.json, 图片生成/图生图/换装直出4K-Qwen-edit_2050863641242677249.json, 图片生成/图生图/换装直出4K，千问换装直出高清，超级稳定_2012359707448578050.json, 图片生成/图生图/换装直出4K，千问换装直出高清，超级稳定_2019323639937634306.json, 图片生成/文生图/千问超级稳定【换装】直出4K，直出高清4k_2049849215886610434.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/【直出】换装4K_2073290298790526976.json、图片生成/图生图/一键换装FireRed+SD高清_2059969177762484226.json、图片生成/图生图/一键换装直出4K-Qwen-edit_2008486174893019137.json、图片生成/图生图/千问4K换装-阿浩_2042485507476688898.json、图片生成/图生图/完美换装直出4K_2037356484362772481.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 13/14 个有
- `ImageScaleToTotalPixels` —— 13/14 个有
- `Seed (rgthree)` —— 13/14 个有
- `easy cleanGpuUsed` —— 13/14 个有
- `easy clearCacheAll` —— 13/14 个有
- `PreviewImage` —— 1/14 个有
- `Text` —— 1/14 个有
- `ZML_AnyTypeSwitch` —— 1/14 个有
- `easy boolean` —— 1/14 个有
- `easy imageBatchToImageList` —— 1/14 个有
- `孤海图像组合批次` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 14 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | sgm_uniform | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，14 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
