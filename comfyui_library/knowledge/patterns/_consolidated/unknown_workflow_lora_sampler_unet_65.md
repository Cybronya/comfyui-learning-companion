---
name: unknown_workflow_lora_sampler_unet_65
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.961444
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511+镜头选择——智能多角度生成_2010728304810139649.json, 图片生成/图生图/87time # 56 QW 多图编辑_1976202631595081729.json, 图片生成/图生图/Qwen Image Edit 2511多角度分镜生成(产品物体摄影等)  一键智能多角度工作流_2010974483972104193.json, 图片生成/图生图/Qwen-edit-2511-风格迁移_2048735908886749185.json, 图片生成/图生图/Qwen-edit-2511-风格迁移_2058012369846095873.json, 图片生成/图生图/【无需3D建模】单图直出建筑规划多视角_2067507419391021058.json, 图片生成/图生图/一图智能智能多角度生成可视化调整角度距离_2014227495960190977.json, 图片生成/图生图/一次6张，多角度图生成_2013237988104343554.json, 图片生成/图生图/单图转多角度视图_2061682280850087938.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_65

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/2511+镜头选择——智能多角度生成_2010728304810139649.json、图片生成/图生图/87time # 56 QW 多图编辑_1976202631595081729.json、图片生成/图生图/Qwen Image Edit 2511多角度分镜生成(产品物体摄影等)  一键智能多角度工作流_2010974483972104193.json、图片生成/图生图/Qwen-edit-2511-风格迁移_2048735908886749185.json、图片生成/图生图/Qwen-edit-2511-风格迁移_2058012369846095873.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenMultiangleCameraNode` —— 6/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 6/9 个有
- `easy imageSize` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `RHHiddenNodes` —— 4/9 个有
- `TextEncodeQwenImageEditPlus` —— 3/9 个有
- `Float` —— 2/9 个有
- `ImpactInt` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `ReplaceString` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `TextConcat` —— 1/9 个有
- `easy promptLine` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 9 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1280 | 512 - 1280 | 9 | 65% |
| 高度 | 720 | 512 - 720 | 9 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，9 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 512 - 1280，9 个样本
- 高度 中位数 720，观测区间 512 - 720，9 个样本，取值集中（一致性 85%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
