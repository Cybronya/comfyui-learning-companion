---
name: unknown_workflow_sampler_unet_vae_88
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.9225
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FIBO2_Image_Edit 图像编辑 ComfyUI 工作流_2114558633513152513.json, 图片生成/图生图/FIBO2_Image_Edit_图像编辑_ComfyUI_工作流_2115431493135851521.json, 图片生成/图生图/FIBO2_Image_Edit_图像编辑_ComfyUI_工作流_2115656917216489473.json, 图片生成/图生图/Qwen21_1底图5参考_带宽高_2112762005873582081.json, 图片生成/图生图/千问2.1图像编辑工作流｜多图参考精准修改_2104511260204290049.json, 图片生成/图生图/参考图一键调色_2112107742885404674.json, 图片生成/图生图/参考图一键调色_2116660935522873345.json, 图片生成/图生图/多参考图生成图片 1参考图_2113249997767663617.json, 图片生成/图生图/多参考图生成图片 1底图-1参考图_2113249672428081154.json, 图片生成/图生图/多参考图生成图片 1底图-2参考图_2113249688706183170.json, 图片生成/图生图/多参考图生成图片 1底图-3参考图_2113249697853956097.json, 平台全量/Qwen-2.1 抠图_2103378102855491586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_88

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/FIBO2_Image_Edit 图像编辑 ComfyUI 工作流_2114558633513152513.json、图片生成/图生图/FIBO2_Image_Edit_图像编辑_ComfyUI_工作流_2115431493135851521.json、图片生成/图生图/FIBO2_Image_Edit_图像编辑_ComfyUI_工作流_2115656917216489473.json、图片生成/图生图/Qwen21_1底图5参考_带宽高_2112762005873582081.json、图片生成/图生图/千问2.1图像编辑工作流｜多图参考精准修改_2104511260204290049.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 9/12 个有
- `PreviewImage` —— 8/12 个有
- `ImageScale` —— 7/12 个有
- `Label (rgthree)` —— 4/12 个有
- `ImageScaleToTotalPixels` —— 3/12 个有
- `QwenImage21Cache` —— 3/12 个有
- `TextEncodeFibo2` —— 3/12 个有
- `GetImageSize` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 25 | 12 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 63% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 25，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
