---
name: unknown_workflow_upscale_10
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.690833
common_nodes: [LoadImage, SaveImage, SeedVR2, SeedVR2ExtraArgs]
problems: []
missing: []
members: [图片生成/图生图/B5、SeedVR2 V2 + 放大模型  —— 和风整理_1991030278124707841.json, 图片生成/图生图/SeedVR2-V2_高清修复_1979466745759043586.json, 图片生成/图生图/SeedVR2放大工作流无LORA_2106293919716827137.json, 图片生成/图生图/WanAn_seedVR2-V2_1990356586835136514.json, 图片生成/图生图/图像放大（可看清毛孔）_1988799951931052033.json, 图片生成/图生图/高清放大_2017481297899298817.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/B5、SeedVR2 V2 + 放大模型  —— 和风整理_1991030278124707841.json、图片生成/图生图/SeedVR2-V2_高清修复_1979466745759043586.json、图片生成/图生图/SeedVR2放大工作流无LORA_2106293919716827137.json、图片生成/图生图/WanAn_seedVR2-V2_1990356586835136514.json、图片生成/图生图/图像放大（可看清毛孔）_1988799951931052033.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2ExtraArgs`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `ImageUpscaleWithModel` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `SeedVR2BlockSwap` —— 5/6 个有
- `UpscaleModelLoader` —— 5/6 个有
- `PlaySound|pysssss` —— 2/6 个有
- `FlashVSRNode` —— 1/6 个有
- `ImageSharpen` —— 1/6 个有
- `Int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
