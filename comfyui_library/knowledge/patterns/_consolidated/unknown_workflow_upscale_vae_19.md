---
name: unknown_workflow_upscale_vae_19
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.825143
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: ["图片生成/图生图/SeedVR2.5万能高清放大.文字放大4K_8K,双重无损_2079023943951929345.json", "图片生成/图生图/SeedVR2.5万能高清放大.文字放大4K_8K,双重无损_2079876987853819905.json", 图片生成/图生图/SeedVR2.5分块高清放大_2029462605076635650.json, 图片生成/图生图/SeedVR2.5双重无损高清放大_2064897439508815874.json, 图片生成/图生图/SeedVR2.5双重无损高清放大_2064919630879223810.json, 图片生成/图生图/SeedVR2_8K_超清放大_高清放大_新版V2.5.15_7B_FP16_2006709977993449474.json, 图片生成/图生图/无损超清双倍增强器eedVR2.5_1995105861876035586.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_19

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/SeedVR2.5万能高清放大.文字放大4K_8K,双重无损_2079023943951929345.json、图片生成/图生图/SeedVR2.5万能高清放大.文字放大4K_8K,双重无损_2079876987853819905.json、图片生成/图生图/SeedVR2.5分块高清放大_2029462605076635650.json、图片生成/图生图/SeedVR2.5双重无损高清放大_2064897439508815874.json、图片生成/图生图/SeedVR2.5双重无损高清放大_2064919630879223810.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `easy int` —— 6/7 个有
- `数学运算_孤海` —— 2/7 个有
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
