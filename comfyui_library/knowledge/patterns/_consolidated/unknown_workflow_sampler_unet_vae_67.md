---
name: unknown_workflow_sampler_unet_vae_67
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.922417
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/参考图一键调色_2112107742885404674.json, 图片生成/图生图/多参考图生成图片 1参考图_2113249997767663617.json, 图片生成/图生图/多参考图生成图片 1底图-1参考图_2113249672428081154.json, 图片生成/图生图/多参考图生成图片 1底图-2参考图_2113249688706183170.json, 图片生成/图生图/多参考图生成图片 1底图-3参考图_2113249697853956097.json, 图片生成/图生图/多参考图生成图片 1底图-4参考图_2113249722726182913.json, 图片生成/图生图/多参考图生成图片 1底图-5参考图_2112078134458806274.json, 图片生成/图生图/（10图）qwen-image-2.1多图编辑_2107971848804855810.json, 图片生成/图生图/（五图编辑）Qwen-image-2.1-单图编辑_2104871202018914306.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json, 视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_67

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/参考图一键调色_2112107742885404674.json、图片生成/图生图/多参考图生成图片 1参考图_2113249997767663617.json、图片生成/图生图/多参考图生成图片 1底图-1参考图_2113249672428081154.json、图片生成/图生图/多参考图生成图片 1底图-2参考图_2113249688706183170.json、图片生成/图生图/多参考图生成图片 1底图-3参考图_2113249697853956097.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/12 个有
- `QwenImage21Cache` —— 6/12 个有
- `ImageScale` —— 5/12 个有
- `CR Text` —— 3/12 个有
- `GetImageSize` —— 2/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `EmptyLatentImage` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有
- `VNCCS_PoseStudio` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 12 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，12 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
