---
name: unknown_workflow_upscale_vae_31
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.808286
common_nodes: [Image Comparer (rgthree), LayerUtility: PurgeVRAM V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy int]
problems: []
missing: []
members: ["图片生成/图生图/SeedVR2.5万能高清放大.文字放大4K_8K,双重无损_2079023943951929345.json", "图片生成/图生图/SeedVR2.5万能高清放大.文字放大4K_8K,双重无损_2079876987853819905.json", 图片生成/图生图/SeedVR2.5双重无损高清放大_2064897439508815874.json, 图片生成/图生图/SeedVR2.5双重无损高清放大_2064919630879223810.json, 图片生成/图生图/SeedVR2_8K_超清放大_高清放大_新版V2.5.15_7B_FP16_2006709977993449474.json, 平台全量/SeedVR2.5高清放大+4K+8K_2101916754762096642.json, "平台全量/万物皆可放大！文字放大！4K 8K,双重无损图片处理高清放大SeedVR2.5_2078179624550486018.json"]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_31

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/SeedVR2.5万能高清放大.文字放大4K_8K,双重无损_2079023943951929345.json、图片生成/图生图/SeedVR2.5万能高清放大.文字放大4K_8K,双重无损_2079876987853819905.json、图片生成/图生图/SeedVR2.5双重无损高清放大_2064897439508815874.json、图片生成/图生图/SeedVR2.5双重无损高清放大_2064919630879223810.json、图片生成/图生图/SeedVR2_8K_超清放大_高清放大_新版V2.5.15_7B_FP16_2006709977993449474.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `数学运算_孤海` —— 4/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
